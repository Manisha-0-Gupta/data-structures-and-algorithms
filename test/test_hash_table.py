from data_structures.hash.hash_table import HashTable


def test_empty_hashtable():
    ht = HashTable(10)

    assert len(ht.table) == 10
    assert all(bucket is None for bucket in ht.table)


def test_insert():
    ht = HashTable(10)

    ht.insert(21)
    ht.insert(32)

    assert ht.search(21) is True
    assert ht.search(32) is True
    assert ht.search(33) is False


def test_collision():
    ht = HashTable(10)

    ht.insert(21)
    ht.insert(31)

    assert ht.search(21) is True
    assert ht.search(31) is True


def test_duplicate_keys():
    ht = HashTable(10)

    ht.insert(21)
    ht.insert(21)
    ht.insert(21)

    assert ht.search(21) is True
    assert ht.table[1].length() == 1


def test_search_empty_bucket():
    ht = HashTable(10)

    assert ht.search(21) is False


def test_search_missing_key_in_collision_bucket():
    ht = HashTable(10)

    ht.insert(21)
    ht.insert(31)

    assert ht.search(41) is False


def test_delete():
    ht = HashTable(10)

    ht.insert(21)
    ht.insert(31)
    ht.insert(41)

    ht.delete(31)

    assert ht.search(31) is False
    assert ht.search(21) is True
    assert ht.search(41) is True


def test_delete_in_empty_bucket():
    ht = HashTable(10)

    ht.delete(21)

    assert ht.search(21) is False


def test_delete_nonexistent_key():
    ht = HashTable(10)

    ht.insert(21)
    ht.insert(31)

    ht.delete(41)

    assert ht.search(21) is True
    assert ht.search(31) is True
    assert ht.table[1].length() == 2


def test_delete_only_key_in_bucket():
    ht = HashTable(10)

    ht.insert(21)
    ht.delete(21)

    assert ht.search(21) is False
    assert ht.table[1].head is None


def test_invalid_key():
    ht = HashTable(10)

    for key in ["21", None, 2.5]:
        try:
            ht.insert(key)
        except TypeError:
            pass
        else:
            raise AssertionError(f"Expected TypeError for key: {key!r}")


def test_invalid_size():
    for size in (0, -1, 2.5, "10", True):
        try:
            HashTable(size)
        except ValueError:
            pass
        else:
            raise AssertionError(f"Expected ValueError for size: {size!r}")
