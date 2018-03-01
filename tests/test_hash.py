from unittest import mock

import pytest

from redis_hash import RedisHash


class FakeRedisClient:
    def __init__(self):
        self._store = {}
        kwargs = {'host': 'host', 'port': '6969', 'db': 0}
        self.connection_pool = mock.Mock(connection_kwargs=kwargs)

    def hget(self, hash_name, key):
        return self._store.get(key).encode('utf-8')

    def hset(self, hash_name, key, value):
        self._store[key] = value

    def hdel(self, hash_name, key):
        del self._store[key]

    def hscan_iter(self, hash_name):
        for k, v in self._store.items():
            yield k.encode('utf-8'), v.encode('utf-8')

    def hlen(self, hash_name):
        return len(self._store)


@pytest.fixture
def redis_hash():
    return RedisHash(FakeRedisClient(), 'hashish')


def test_redis_hash(redis_hash):
    assert redis_hash._client
    assert redis_hash._hash_name
    assert 'hash_name' in repr(redis_hash)
    assert "host='" in repr(redis_hash)

    assert len(redis_hash) == 0
    redis_hash['foo'] = 'fooz'
    assert redis_hash['foo'] == b'fooz'
    assert len(redis_hash) == 1

    redis_hash['bar'] = 'barz'
    assert redis_hash['bar'] == b'barz'
    assert len(redis_hash) == 2

    assert list(redis_hash) == [(b'foo', b'fooz'), (b'bar', b'barz')]

    del redis_hash['bar']
    assert len(redis_hash) == 1
    del redis_hash['foo']
    assert len(redis_hash) == 0
