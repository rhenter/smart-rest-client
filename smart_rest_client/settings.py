"""
Settings for API Client are all namespaced in the API_CLIENT setting.
For example your project's `settings.py` file might look like this:

API_CLIENT = {
    'API': {
        'NAME': 'API NAME',
        'BASE_URL': 'https://example.com/v1',
        'ENDPOINTS': [
            '/order/orders',
            '/user/users',
            ...
        ],
        'AUTHENTICATION_ACCESS_TOKEN': 'header' or 'url'
        'AUTHENTICATION_ACCESS_TOKEN_TYPE': 'Bearer', 'Token', ...
    },
}

This module provides the `api_client_setting` object, that is used to access
Smart Rest Client settings, checking for user settings first, then falling
back to the defaults.
"""
from typing import Dict, List

DEFAULT_SETTINGS_KEY = 'API_CLIENT'
API_DEFAULTS = {
    'AUTHENTICATION_ACCESS_TOKEN': None,
    'AUTHENTICATION_ACCESS_TOKEN_TYPE': 'Bearer',
    'AUTHENTICATION_METHOD': 'header',
    'AUTHENTICATION_URL_EXTRA_PARAMS': [],
    'AUTHENTICATION_URL_KEY': 'token',
    'BASE_URL': None,
    'ENDPOINTS': [],
    'LOCALE': 'en',
    'NAME': None,
    'URL_APPEND_SLASH': True,
    'TIMEOUT': 3,
    'PAGE_SIZE': 100,
    'SLUG_FIELD': 'id'
}

REQUIRED_KEYS = ['NAME', 'BASE_URL', 'ENDPOINTS']


class APIClientSettings:
    """
    A settings object that allows Smart Rest Client settings to be accessed as
    properties. For example:

        from smart_rest_client.settings import smart_rest_client
        print(smart_rest_client.API)

    Any setting with string import paths will be automatically resolved
    and return the class, rather than the string literal.
    """

    def __init__(self, user_settings: dict = None) -> None:
        self.user_settings = user_settings
        self.api_defaults = API_DEFAULTS
        self._cached_attrs = set()
        self.apis = self._set_apis()
        self.configs = self._get_defaults_configs()

    def _get_api_configs(self, api_settings: dict) -> Dict:
        configs = {}

        for req_attr in REQUIRED_KEYS:
            if req_attr not in api_settings:
                raise AttributeError(f"Key Required: '{req_attr}'")

        for user_attr in api_settings:
            if user_attr not in self.api_defaults:
                raise AttributeError(f"Invalid API setting: '{user_attr}'")

        for attr in self.api_defaults:
            try:
                # Check if present in user settings
                val = api_settings[attr]
            except KeyError:
                # Fall back to defaults
                val = self.api_defaults[attr]

            if attr == 'BASE_URL' and not val.startswith('http'):
                raise AttributeError(f"Invalid Base URL: '{val}'. Please add a URL with http or https as prefix.")

            configs[attr] = val
            # Cache the result
            self._cached_attrs.add(attr)
        return configs

    def _get_defaults_configs(self) -> Dict:
        configs = {}

        for user_attr in self.user_settings:
            if user_attr != 'API' and user_attr not in self.api_defaults:
                raise AttributeError(f"Invalid Global Setting: '{user_attr}'")

        for attr in self.api_defaults:
            try:
                # Check if present in user settings
                val = self.user_settings[attr]
            except KeyError:
                # Fall back to defaults
                val = self.api_defaults[attr]

            configs[attr] = val
            # Cache the result
            self._cached_attrs.add(attr)
        return configs

    def _set_apis(self) -> List[dict]:
        api_settings = self.user_settings.get('API', '')
        if not api_settings:
            return []

        apis = []
        if isinstance(api_settings, dict):
            apis.append(self._get_api_configs(api_settings))
        elif isinstance(api_settings, list):
            for api in api_settings:
                apis.append(self._get_api_configs(api))
        return apis

    @property
    def api_names(self) -> list:
        return [api['NAME'] for api in self.apis]

    def __repr__(self) -> str:
        return '<APIClientSettings>'

    def __str__(self) -> str:
        names = ' '.join([name.title() for name in self.api_names])
        return f'APIClientSettings: {names}'
