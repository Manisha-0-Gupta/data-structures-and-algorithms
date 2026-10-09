from data_structures.linked_list.linked_list import LinkedList


def test_empty_list():
    ll = LinkedList()

    assert ll.length() == 0
    assert ll.search(10) is False


def test_prepend():
    ll = LinkedList()

    ll.prepend(20)
    ll.prepend(10)

    assert ll.head.data == 10
    assert ll.head.next.data == 20
    assert ll.length() == 2


def test_append():
    ll = LinkedList()

    ll.append(10)
    ll.append(20)
    ll.append(30)

    assert ll.head.data == 10
    assert ll.head.next.data == 20
    assert ll.head.next.next.data == 30
    assert ll.length() == 3


def test_insert():
    ll = LinkedList()

    ll.append(10)
    ll.append(30)

    ll.insert(10, 20)

    assert ll.head.data == 10
    assert ll.head.next.data == 20
    assert ll.head.next.next.data == 30


def test_search():
    ll = LinkedList()

    ll.append(10)
    ll.append(20)

    assert ll.search(10) is True
    assert ll.search(20) is True
    assert ll.search(50) is False


def test_delete_middle():
    ll = LinkedList()

    ll.append(10)
    ll.append(20)
    ll.append(30)

    ll.delete(20)

    assert ll.head.data == 10
    assert ll.head.next.data == 30
    assert ll.length() == 2


def test_delete_head():
    ll = LinkedList()

    ll.append(10)
    ll.append(20)

    ll.delete(10)

    assert ll.head.data == 20
    assert ll.length() == 1


def test_delete_only_node():
    ll = LinkedList()

    ll.append(10)
    ll.delete(10)

    assert ll.head is None
    assert ll.length() == 0


def test_delete_nonexistent():
    ll = LinkedList()

    ll.append(10)
    ll.append(20)

    ll.delete(50)

    assert ll.length() == 2


def test_insert_nonexistent():
    ll = LinkedList()

    ll.append(10)
    ll.append(20)

    ll.insert(50, 30)

    assert ll.length() == 2


if __name__ == "__main__":
    test_empty_list()
    test_prepend()
    test_append()
    test_insert()
    test_search()
    test_delete_middle()
    test_delete_head()
    test_delete_only_node()
    test_delete_nonexistent()
    test_insert_nonexistent()

    print("All tests passed.")
