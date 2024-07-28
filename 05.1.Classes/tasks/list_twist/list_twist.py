from collections import UserList
import typing as tp


class ListTwist(UserList[tp.Any]):
    """
    List-like class with additional attributes:
        * reversed, R - return reversed list
        * first, F - insert or retrieve first element;
                     Undefined for empty list
        * last, L -  insert or retrieve last element;
                     Undefined for empty list
        * size, S -  set or retrieve size of list;
                     If size less than list length - truncate to size;
                     If size greater than list length - pad with Nones
    """

    @property
    def reversed(self) -> list[tp.Any]:
        return self.data[::-1]

    @property
    def R(self):
        return self.reversed

    @property
    def first(self) -> tp.Any:
        if self.data:
            return self.data[0]
        else:
            return None

    @property
    def F(self):
        return self.first

    @first.setter
    def first(self, value: tp.Any) -> None:
        if self.data:
            self.data[0] = value
        else:
            self.data.append(value)

    @F.setter
    def F(self, value: tp.Any):
        self.first = value

    @property
    def last(self) -> tp.Any:
        if self.data:
            return self.data[-1]
        else:
            return None

    @last.setter
    def last(self, value: tp.Any) -> None:
        if self.data:
            self.data[-1] = value
        else:
            self.data.append(value)

    @property
    def L(self):
        return self.last

    @L.setter
    def L(self, value: int):
        self.last = value

    @property
    def size(self) -> int:
        return len(self.data)

    @size.setter
    def size(self, n: int) -> None:
        dif: int = len(self.data) - n
        if dif > 0:
            while len(self.data) - n != 0:
                self.data.pop()
        elif dif < 0:
            while len(self.data) - n != 0:
                self.data.append(None)

    @property
    def S(self):
        return self.size

    @S.setter
    def S(self, n: int):
        self.size = n
