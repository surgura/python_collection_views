import pytest
from collection_views import ImmutableViewList


def test_init() -> None:
    lst = [1, 2, 3, 4]
    view = ImmutableViewList(lst)
    assert len(view) == len(lst)


def test_index() -> None:
    lst = [1, 2, 3, 4]
    view = ImmutableViewList(lst)
    assert view.index(3) == lst.index(3)


def test_count() -> None:
    lst = [1, 1, 2, 3]
    view = ImmutableViewList(lst)
    assert view.count(1) == lst.count(1)


def test_copy() -> None:
    lst = [1, 2, 3]
    view = ImmutableViewList(lst)
    copy = view.copy()
    assert copy == lst
    assert copy is not lst


def test_getitem() -> None:
    lst = [1, 2, 3]
    view = ImmutableViewList(lst)
    assert view[1] == lst[1]
    assert view[1:2] == lst[1:2]


def test_str_repr() -> None:
    lst = [1, 2, 3]
    view = ImmutableViewList(lst)
    assert str(view) == str(lst)
    assert repr(view) == repr(lst)


def test_add() -> None:
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    view1 = ImmutableViewList(lst1)
    view2 = ImmutableViewList(lst2)
    assert view1 + view2 == lst1 + lst2
    assert view1 + lst2 == lst1 + lst2


def test_mul() -> None:
    lst = [1, 2, 3]
    view = ImmutableViewList(lst)
    assert view * 3 == lst * 3
    assert 3 * view == 3 * lst


def test_iter() -> None:
    lst = [1, 2, 3]
    view = ImmutableViewList(lst)
    for v, l in zip(view, lst):
        assert v == l


def test_reversed() -> None:
    lst = [1, 2, 3]
    view = ImmutableViewList(lst)
    for v, l in zip(reversed(view), reversed(lst)):
        assert v == l


def test_eq() -> None:
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    view1 = ImmutableViewList(lst1)
    view2 = ImmutableViewList(lst2)
    assert view1 == lst1
    assert view1 != lst2
    assert view1 != view2


def test_lt() -> None:
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 4]
    view1 = ImmutableViewList(lst1)
    view2 = ImmutableViewList(lst2)
    assert (view1 < view2) == (lst1 < lst2)


def test_le() -> None:
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    view1 = ImmutableViewList(lst1)
    view2 = ImmutableViewList(lst2)
    assert (view1 <= view2) == (lst1 <= lst2)


# ... add more tests as necessary ...

if __name__ == "__main__":
    pytest.main()
