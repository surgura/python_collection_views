"""ImmutableviewList class."""

from __future__ import annotations

import sys
from typing import Any, Generic, Iterator, List, SupportsIndex, TypeVar, Union, overload

_T = TypeVar("_T")


class ImmutableViewList(Generic[_T]):
    """An immutable view over a list."""

    _viewed_list: List[_T]

    def __init__(self, viewed_list: List[_T]) -> None:
        """
        Initialize the view over the provided list.

        :param viewed_list: The list over which this class provides an immutable view.
        """
        self._viewed_list = viewed_list

    def index(
        self, value: _T, start: SupportsIndex = 0, stop: SupportsIndex = sys.maxsize
    ) -> int:
        """
        Return the first index of the specified value between start and stop.

        :param value: Value to be searched for.
        :param start: Start of the search range.
        :param stop: End of the search range.
        :returns: Index of the first occurrence of value.
        """
        return self._viewed_list.index(value, start, stop)

    def count(self, value: _T) -> int:
        """
        Return the number of times the specified value appears in the list.

        :param value: Value to be counted.
        :returns: Number of occurrences of value.
        """
        return self._viewed_list.count(value)

    def copy(self) -> List[_T]:
        """
        Return a shallow copy of the list.

        :returns: The copy.
        """
        return self._viewed_list.copy()

    @overload
    def __getitem__(self, index: SupportsIndex) -> _T:
        """
        Return the element at the specified index.

        :param index: The index.
        :returns: The element.

        #noqa: DAR202
        """

    @overload
    def __getitem__(self, index: slice) -> List[_T]:
        """
        Return the sublist at the provided slice.

        :param index: The slice.
        :returns: The sublist.

        #noqa: DAR202
        """

    def __getitem__(self, index: Union[SupportsIndex, slice]) -> Union[_T, List[_T]]:
        """
        Return the element at the specified index or a sublist if a slice is provided.

        :param index: Index or slice.
        :returns: Element or sublist.
        """
        return self._viewed_list[index]

    def __len__(self) -> int:
        """
        Return the number of elements in the list.

        :returns: The number of elements.
        """
        return len(self._viewed_list)

    def __contains__(self, value: _T) -> bool:
        """
        Check if the list contains the specified value.

        :param value: Value to check.
        :returns: True if value is in the list, False otherwise.
        """
        return value in self._viewed_list

    def __str__(self) -> str:
        """
        Return the string representation of the list.

        :returns: The representation.
        """
        return str(self._viewed_list)

    def __repr__(self) -> str:
        """
        Return the official string representation of the object.

        :returns: The representation.
        """
        return repr(self._viewed_list)

    @overload
    def __add__(self, other: ImmutableViewList[_T]) -> List[_T]:
        """
        Return the concatenation of the list with another ImmutableViewList.

        :param other: The other ImmutableViewList.
        :returns: The concatenated list.

        #noqa: DAR202
        """

    @overload
    def __add__(self, other: List[_T]) -> List[_T]:
        """
        Return the concatenation of the list with another list.

        :param other: The other list.
        :returns: The concatenated list.

        #noqa: DAR202
        """

    def __add__(self, other: Union[ImmutableViewList[_T], List[_T]]) -> List[_T]:
        """
        Return the concatenation of the list with another list or ImmutableViewList.

        :param other: The other list or ImmutableViewList.
        :returns: Concatenated list.
        """
        if isinstance(other, ImmutableViewList):
            return self._viewed_list + other._viewed_list
        else:
            return self._viewed_list + other

    def __mul__(self, n: int) -> List[_T]:
        """
        Return the list repeated n times.

        :param n: Number of repetitions.
        :returns: Repeated list.
        """
        return self._viewed_list * n

    def __rmul__(self, n: int) -> List[_T]:
        """
        Return the list repeated n times (right multiplication).

        :param n: Number of repetitions.
        :returns: Repeated list.
        """
        return self._viewed_list * n

    def __iter__(self) -> Iterator[_T]:
        """
        Return an iterator over the elements of the list.

        :returns: The iterator.
        """
        return iter(self._viewed_list)

    def __reversed__(self) -> Iterator[_T]:
        """
        Return a reverse iterator over the elements of the list.

        :returns: The reverse iterator.
        """
        return reversed(self._viewed_list)

    def __eq__(self, other: Union[ImmutableViewList[Any], object]) -> bool:
        """
        Check if the list is equal to another object.

        :param other: The other object to compare with.
        :returns: True if equal, False otherwise.
        """
        if isinstance(other, ImmutableViewList):
            return self._viewed_list == other._viewed_list
        else:
            return self._viewed_list == other

    def __lt__(self, other: Union[ImmutableViewList[Any], List[Any]]) -> bool:
        """
        Check if the list is less than another list.

        :param other: The other list to compare with.
        :returns: True if less than, False otherwise.
        """
        if isinstance(other, ImmutableViewList):
            return self._viewed_list < other._viewed_list
        return self._viewed_list < other

    def __le__(self, other: Union[ImmutableViewList[Any], List[Any]]) -> bool:
        """
        Check if the list is less than or equal to another list.

        :param other: The other list to compare with.
        :returns: True if less than or equal to, False otherwise.
        """
        if isinstance(other, ImmutableViewList):
            return self._viewed_list <= other._viewed_list
        return self._viewed_list <= other
