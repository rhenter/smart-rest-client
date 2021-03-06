from typing import Any

from .base import BaseAPI, BaseEndpoint
from .exceptions import APIConfigurationError, APINotFound
from .settings import APIClientSettings


class APIClientEndpointList:
    endpoints = []

    def __init__(self, endpoint_name: str) -> None:
        self.name = endpoint_name

    def set_endpoint(self, api: Any, endpoint_url: str) -> None:
        endpoint = BaseEndpoint(api=api, endpoint=endpoint_url)
        setattr(self, self._get_endpoint_base_name(endpoint_url), endpoint)
        self.endpoints.append(endpoint)

    def _get_endpoint_base_name(self, endpoint: str) -> Any:
        words = [key for key in endpoint.split('?')[0].split('/') if key]
        response_name = words[-1]
        if '{' in response_name:
            response_name = words[-2]
        if '-' in response_name:
            response_name = response_name.replace('-', '_')
        return response_name


class APIClient:
    """API Client Factory Class
    This class instantiates all endpoint classes
    """

    def __init__(self, **kwargs: Any) -> None:
        """API object to communicate with API.
        """
        self.api = BaseAPI(**kwargs)
        endpoints = self._get_endpoints(kwargs)
        for endpoint_name in endpoints:
            endpoint_urls = endpoints[endpoint_name]
            endpoint = APIClientEndpointList(endpoint_name)
            for endpoint_url in endpoint_urls:
                endpoint.set_endpoint(api=self.api, endpoint_url=endpoint_url)

            setattr(self, endpoint_name, endpoint)

    def __repr__(self) -> str:
        return f'<APIClient {self.api.api_name.title()}>'

    def _get_endpoints(self, kwargs: dict) -> dict:
        endpoints = {}
        for endpoint_path in kwargs['endpoints']:
            endpoint_name = self._get_endpoint_base_name(endpoint_path)
            if endpoint_name not in endpoints:
                endpoints[endpoint_name] = []
            endpoints[endpoint_name].append(endpoint_path)
        return endpoints

    def _get_endpoint_base_name(self, endpoint: str) -> str:
        words = [key for key in endpoint.split('/') if key]
        response_name = words[0]
        if response_name in [f'v{i}' for i in range(10)]:
            response_name = words[1]

        if '-' in response_name:
            response_name = response_name.replace('-', '_')

        return response_name


def api_client_factory(api_name: str = '', api_client_settings: APIClientSettings = None, **kwargs: Any) -> APIClient:
    if not api_name:
        raise APIConfigurationError('API name is required.')
    if not api_client_settings:
        raise APIConfigurationError('API Settings is required.')

    api_configs = next((api for api in api_client_settings.apis if api['NAME'] == api_name), None)
    if not api_configs:
        raise APINotFound('API name Not Found.')

    api_args = {
        'api_name': api_name,
        'base_url': kwargs.get('base_url', '') or api_configs.get('BASE_URL'),
        'access_token': kwargs.get('access_token', '') or api_configs.get('AUTHENTICATION_ACCESS_TOKEN'),
        'access_token_type': kwargs.get('access_token_type', '') or api_configs.get(
            'AUTHENTICATION_ACCESS_TOKEN_TYPE'),
        'authentication_method': kwargs.get('authentication_method', '') or api_configs.get('AUTHENTICATION_METHOD'),
        'authentication_url_extra_params': kwargs.get('authentication_url_extra_params', '') or api_configs.get(
            'AUTHENTICATION_URL_EXTRA_PARAMS'),
        'authentication_url_key': kwargs.get('authentication_url_key', '') or api_configs.get('AUTHENTICATION_URL_KEY'),
        'endpoints': kwargs.get('endpoints', '') or api_configs.get('ENDPOINTS'),
        'locale': kwargs.get('locale', '') or api_configs.get('LOCALE'),
        'url_append_slash': kwargs.get('url_append_slash', '') or api_configs.get('URL_APPEND_SLASH'),
        'timeout': kwargs.get('timeout', '') or api_configs.get('TIMEOUT'),
    }
    return APIClient(**api_args)
