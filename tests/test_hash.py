from unittest import mock

import pytest
from fakeredis import FakeStrictRedis

from redis_hash import RedisHash


@pytest.fixture
def redis_hash():
    fake_redis = FakeStrictRedis()
    kwargs = {'host': 'host', 'port': '6969', 'db': 0}
    fake_redis.connection_pool = mock.Mock(connection_kwargs=kwargs)
    return RedisHash(fake_redis, 'hashish')


@pytest.fixture
def mock_redis_hash():
    return RedisHash(mock.MagicMock(), 'hashish')


def test_redis_hash(redis_hash):
    assert redis_hash._client
    assert redis_hash._hash_name
    assert 'hash_name' in repr(redis_hash)
    assert "host='" in repr(redis_hash)

    assert len(redis_hash) == 0
    redis_hash['foo'] = 'fooz'
    assert redis_hash['foo'] == 'fooz'
    assert len(redis_hash) == 1

    redis_hash['bar'] = 'barz'
    assert redis_hash['bar'] == 'barz'
    assert len(redis_hash) == 2

    assert set(redis_hash) == {'foo', 'bar'}

    del redis_hash['bar']
    assert len(redis_hash) == 1
    del redis_hash['foo']
    assert len(redis_hash) == 0


def test_redis_hash_getitem_keyerror(redis_hash):
    with pytest.raises(KeyError):
        redis_hash['nx']


def test_redis_hash_delitem_keyerror(redis_hash):
    with pytest.raises(KeyError):
        del redis_hash['nx']


def test_redis_hash_contains(mock_redis_hash):
    key = 'eita'
    assert key in mock_redis_hash

    mock_redis_hash._client.hexists.assert_called_with(mock_redis_hash._hash_name, key)


def test_redis_hash_len(mock_redis_hash):
    assert len(mock_redis_hash)

    mock_redis_hash._client.hlen.assert_called_with(mock_redis_hash._hash_name)
