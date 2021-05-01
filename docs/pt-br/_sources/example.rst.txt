Base Settings
=============

* Create a clients.py file in the core folder of your project, if you haven't, created it within your project folder to be simple to be imported from anywhere in the project with the following content:

.. code-block:: python

  from smart_rest_client.client import api_client_factory
  from smart_rest_client.settings import APIClientSettings

  API_CLIENT_SETTINGS = {
      'API': [
        {
            'NAME': 'production',
            'BASE_URL': 'https://example.com',
            'ENDPOINTS': [
                '/v1/order/orders',
                '/v1/user/users',
                ...
            ],
            'AUTHENTICATION_ACCESS_TOKEN': 'TOKEN'
        },
        {
            'NAME': 'localhost',
            'BASE_URL': 'http://localhost:8001',
            'ENDPOINTS': [
                '/v1/order/orders',
                '/v1/user/users',
                ...
            ],
            'AUTHENTICATION_ACCESS_TOKEN': 'TOKEN'
        }
      ]
    }


  api_settings = APIClientSettings(API_CLIENT_SETTINGS)
  local_api_client = api_client_factory('localhost', api_settings)
  production_api_client = api_client_factory('production', api_settings)


.. note::
   - The name of this variable will be the name of the client that you can use throughout your project
   - It is recommended that the production use a set of configurations without configurations.py to change the simple way or the name of the API without the need to create several.
   - In our case, we have the option of "production" and "localhost", the factory generates the customer according to the name used and the parameters identified in it


Let's imagine which client is located in a folder called clients on project folder (folder containing the settings.py file)

Example
=======

- Import the api_client from your client.py file

.. code-block:: python

    >> from client import production_api_client as api_client
    >> result = api_client.user.users.list()
    >>
    >> # Use the result as object
    >> print(result.as_obj())
    UserUsers(
        previous=None,
        count=1,
        next=None,
        results=[
            NamelessModel(occupation=None, full_name='Admin System',
                image=None, cpf='', is_superuser=True, cellphone='', email='', sex=None, username='admin', birthdate='09/09/1999',
                logged_as='', id=1, is_temp=False, is_active=True)
        ]
    )
    >>
    >> # Use the result as dict
    >> print(result.as_dict())
    {'count': 1,
     'next': None,
     'previous': None,
     'results': [{'id': 1,
       'username': 'admin',
       'full_name': 'Admin System',
       'sex': None,
       'birthdate': '09/09/1999',
       'cpf': '',
       'cellphone': '',
       'email': '',
       'image': None,
       'occupation': None,
       'logged_as': '',
       'is_superuser': True,
       'is_active': True,
       'is_temp': False}
      ]
     }

