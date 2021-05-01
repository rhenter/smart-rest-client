=================
Smart REST Client
=================

|PyPI latest| |PyPI Version| |PyPI License| |Docs| |CicleCI Status| |Coverage| |Docs| |Open Source? Yes!|

Smart API Client é um Wrapper para realizar solicitações para Rest APIs usando objetos para solicitar endpoints e seus métodos"

Para mais informações, veja nossa documentação em `Github Pages <https://rhenter.github.io/smart-rest-client/>`_

Configurações
=============

* Crie um arquivo chamado clients.py com o seguinte conteudo para que você possa importa-lo de qualquer lugar no seu projeto:

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
  api_client = api_client_factory('production', api_settings)


.. note::
   - The name of this variable will be the name of the client that you can use throughout your project
   - It is recommended that the production use a set of configurations without configurations.py to change the simple way or the name of the API without the need to create several.
   - In our case, we have the option of "production" and "localhost", the factory generates the customer according to the name used and the parameters identified in it


* Now we are going to list the data using the normal Django template system

Let's imagine which client is located in a folder called clients on project folder (folder containing the settings.py file)

Uso
===

Para cada endpoint o client vai criar a seguinte estrutura:

Example to ``/user/users/``

- Create:

.. code-block:: text

  usage: api_client.user.users.create(data=data)
  return: Fazer uma chamada POST de dados (dict) para /user/users/

- List:

.. code-block:: python

  usage: api_client.user.users.list()
  return: Fazer uma chamada GET para /user/users/

- Get/Retrieve/Detail:

.. code-block:: python

  usage: api_client.user.users.get(id=123)
  return: Fazer uma chamada GET para /user/users/123/

- Update:

.. code-block:: python

  uso: api_client.user.users.update(id=123, data=data, partial=False)
  return: Fazer uma chamada UPDATE or PATCH de dados (dict) para /user/users/123/

- Delete:

.. code-block:: python

  uso: api_client.user.users.delete(id=123)
  return: Fazer uma chamada GET para /user/users/123/


Examplo
=======

- Importe o api_client do seu arquivo client.py

.. code-block:: python

    >> from client import api_client
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


Documentação
============

Veja nossa documentação em `Github Pages <https://rhenter.github.io/smart-rest-client/>`_

Contribuir
==========

Por favor envie pull request, eles serão muito apreciados.


1. Faço o Fork do repo `repository <https://github.com/rhenter/smart-rest-client>`_ on GitHub.
2. Crie uma Branch fora da master
3. Instale as dependências. ``pip install -r requirements-dev.txt``
5. Crie um Pull Request com a sua contribuição

.. |Docs| image:: https://img.shields.io/static/v1?label=DOC&message=GitHub%20Pages&color=%3CCOLOR%3E
   :target: https://rhenter.github.io/smart-rest-client/
.. |PyPI Version| image:: https://img.shields.io/pypi/pyversions/smart-rest-client.svg?maxAge=60
   :target: https://pypi.python.org/pypi/smart-rest-client
.. |PyPI License| image:: https://img.shields.io/pypi/l/smart-rest-client.svg?maxAge=120
   :target: https://github.com/rhenter/smart-rest-client/blob/master/LICENSE
.. |PyPI latest| image:: https://img.shields.io/pypi/v/smart-rest-client.svg?maxAge=120
   :target: https://pypi.python.org/pypi/smart-rest-client
.. |CicleCI Status| image:: https://circleci.com/gh/rhenter/smart-rest-client.svg?style=svg
   :target: https://circleci.com/gh/rhenter/smart-rest-client
.. |Coverage| image:: https://codecov.io/gh/rhenter/smart-rest-client/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/rhenter/smart-rest-client
.. |Open Source? Yes!| image:: https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github
   :target: https://github.com/rhenter/smart-rest-client