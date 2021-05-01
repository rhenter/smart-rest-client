Overview
========

Smart Rest Client Fis a python wrapper to perform requests to Rest APIs using objects to request endpoints and their methods

.. code-block:: text

  GET: List or Retrieve
  POST: Create
  UPDATE: Full Update
  PATCH: Partial Update


Settings
========

 in the core folder of your project, if you haven't, created it within your project folder to be simple to be imported from anywhere in the project with the following content:

.. code-block:: python

  from smart_rest_client.client import api_client_factory
  from smart_rest_client.settings import APIClientSettings

  api_client_settings = {
      'API': {
            'NAME': 'test_api',
            'BASE_URL': 'https://example.com',
            'ENDPOINTS': [
                '/v1/order/orders',
                '/v1/user/users',
                ...
            ],
            'AUTHENTICATION_ACCESS_TOKEN': 'TOKEN'
        }
    }


  api_settings = APIClientSettings(API_CLIENT_SETTINGS)
  api_client = client_factory('test_api', api_settings)



- For more information on the available configurations, see at:

.. toctree::
    :maxdepth: 2

    defaults.rst

Client Methods
==============

For each endpoint the client Factory will create the follow structure:

Example to ``/user/users/``

- Create:

.. code-block:: text

  usage: smart_rest_client.user.users.create(data=data)
  return: Response of POST of data (dict) to /user/users/

- List:

.. code-block:: python

  usage: smart_rest_client.user.users.list()
  return: Response of GET to /user/users/

- Get/Retrieve/Detail:

.. code-block:: python

  usage: smart_rest_client.user.users.get(id=123)
  return: Response of GET to /user/users/123/

- Update:

.. code-block:: python

  usage: smart_rest_client.user.users.update(id=123, data=data, partial=False)
  return: the response of UPDATE or PATCH of data (dict) to /user/users/123/

- Delete:

.. code-block:: python

  usage: smart_rest_client.user.users.delete(id=123)
  return: Response of GET to /user/users/123/

