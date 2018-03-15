=======
Changes
=======

1.0.1 / 2018-03-15
==================

* Fix RedisHash.clear_keys() on python 3.3: force dict keys conversion to set

1.0.0 / 2018-03-15
==================

* Convert redis values from binary to string
* Fix RedisHash not being able to be converted to dict
* Add clear_keys() method

0.1.0 / 2018-03-02
==================

* Use HLEN for len() and HEXISTS for contains
* Properly raises KeyError when trying to access or delete inexistent keys

0.0.2 / 2018-03-01
==================

* Add CHANGES.rst to source distribution

0.0.1 / 2018-03-01
==================

* Add initial RedisHash class
