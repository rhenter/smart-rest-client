from typing import Any
from urllib.parse import urlparse

from simple_model import Model
from simple_model.builder import model_builder


class ResponseFactory:
    """"
    Return a API Response object
    """

    def __init__(self, response: Any, endpoint: str = '', api_client=None) -> None:
        self.api_client = api_client
        self.endpoint = endpoint
        self.raw = response
        self.response_name = self._get_response_name()
        self.status_code = response.status_code

    def __repr__(self) -> str:
        return f'<APIClient {self.response_name} - Status: [{self.status_code}]>'

    def __str__(self) -> str:
        return f'{self.response_name} - Status: [{self.status_code}]>'

    def _get_response_first_name(self, endpoint: str) -> Any:
        words = [key for key in endpoint.split('/') if key]
        response_name = words[0]
        if response_name in [f'v{i}' for i in range(10)]:
            response_name = words[1]
        return response_name

    def _get_response_name(self) -> str:
        path = self.endpoint
        if path.startswith('/'):
            path = path[1:]
        words = [key for key in path.split('?')[0].split('/') if key]
        base = 0
        if words[base] in [f'v{i}' for i in range(10)]:
            base = 1

        last = -1
        if len(words) > 2:
            last = base + 1

        if words[base] == words[last]:
            response_name = words[base].title()
        else:
            response_name = f'{words[base].title()}{words[last].title()}'
        response_name = response_name.replace('-', '').replace('_', '')
        return response_name

    def as_dict(self) -> dict:
        return self.raw.json()

    def as_obj(self) -> Model:
        result = self.as_dict()
        return model_builder(result, class_name=self.response_name)

    def next(self):
        if 'next' not in self.as_dict():
            return

        next_url = self.as_dict()['next']
        url_data = urlparse(next_url)
        endpoint = url_data.path

        response = self.api_client.make_request(
            method_name='GET',
            endpoint=f'{endpoint}?{url_data.query}',
        )
        return type(self)(response=response, endpoint=endpoint, api_client=self.api_client)
