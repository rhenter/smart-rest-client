Development Installation
========================

Requirements
------------

- Python 3.x


Development install
-------------------

After forking or checking out:

.. code-block:: bash

    $ cd smart-rest-client/
    $ pip install -r requirements-dev.txt

The requirements-dev are only used for development, so we can easily
install/track dependencies required to run the tests using continuous
integration platforms.

The official entrypoint for distribution is the ``requirements.txt`` which
contains the minimum requirements to execute the tests.


Running tests
-------------

.. code-block:: bash

    $ make test

or:

.. code-block:: bash

    $ py.test -vv -s
