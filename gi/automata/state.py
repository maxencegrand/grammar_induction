class State:

    def __init__(self, id: int):
        """
        Represents a State in a
        finite state acceptor.

        :param id: label of the state
        :type id: str
        """
        self.__id = id

    @property
    def id(self):
        return self.__id

    def __hash__(self):
        return hash(self.__id)

    def __eq__(self, other):
        return self.__id == other.id

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

    def __le__(self, other):
        return self.id <= other.id

    def __ge__(self, other):
        return self.id >= other.id

    def __ne__(self, other):
        return self.id != other.id

    def __str__(self):
        return self.id
