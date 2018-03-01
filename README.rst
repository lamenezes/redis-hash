==========
redis-hash
==========

Hash interface for redis-py

Installation
============

.. code:: bash

    pip install redis-hash


Usage
=====

.. code:: python

    from redis import StrictRedis
    from redis_hash import RedisHash

    redis_client = StrictRedis(host='localhost', port=6379, db=0)
    redis_hash = RedisHash(redis_client, 'hash_name')
    redis_hash['foo'] = 'bar'
    assert len(redis_hash) == 1
    for k, v in redis_hash:
        print(k, v)  # prints: foo bar
    redis_hash  # returns b'bar'
    list(redis_hash)  # return [(b'foo', b'bar')]
    del redis_hash['foo']
    assert len(redis_hash) == 0
