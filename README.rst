==========
redis-hash
==========

Hash interface for redis-py

Installation
============

.. code:: bash

    pip install redis redis_hash


Usage
=====

First you need to instantiate the redis client from the ``redis`` package:


.. code:: python

    >> from redis import StrictRedis
    >> redis_client = StrictRedis(host='localhost', port=6379, db=0)

Then create your hash passing the client and the hash key:

.. code:: python

    >> from redis_hash import RedisHash
    >> redis_hash = RedisHash(redis_client, 'hash_name')

Now your can handle your hash like a ``dict``:

.. code:: python

    >> redis_hash['foo'] = 'bar'
    >> len(redis_hash)
    1
    >>> for k, v in redis_hash:
            print(k, v)
    foo bar
    >>> redis_hash['foo']
    b'bar'
    >>> list(redis_hash)
    [(b'foo', b'bar')]
    >> del redis_hash['foo']
    >> len(redis_hash)
    0
