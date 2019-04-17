class ChessCoordinate:

    _interned = {}

    def __new__(cls, file, rank):  # use named postitional arguments
        """
        def new(cls, *args, **kwargs) - appears implicitly is a class method,
        it accepts cls as it's first argument rather than self.
        In fact new is especially cased static method that happens
        to take the type of the class as its first argument (cls) - the type of
        the object to be created.
        Secondly it accepts any addition that we pass to the constructor.
        Puprose of __new__ is to allocate a new object.
        """

        if len(file) != 1:
            raise ValueError("{} component file {!r} does not have a length of one.".format(
                cls.__name__, file))

        if file not in 'abcdefgh':
            raise ValueError("{} component file {!r} is out of range.".format(
                cls.__name__, file))

        if rank not in range(1, 9):
            raise ValueError("{} component rank {!r} is out of range.".format(
                cls.__name__, rank))

        # Once the arguments are validated, we use them to create a single
        # tuple objectfrom file and rank to use as a key, and check if there is
        # an enty against this key tuple in a dictionary _interned, we attached
        # as a class attribute.
        key = (file, rank)

        if key not in cls._interned:
            # Only if the tuple key is not present in the dictionary do we
            # allocate a new instance by calling onject.__new__
            obj = super().__new__(cls)
            obj._file = file
            obj._rank = rank
            # insert new instance into the dictionary
            cls._interned[key] = obj

        return cls._interned[key]

    @property
    def file(self):
        return self._file

    @property
    def rank(self):
        return self._rank

    def __repr__(self):
        return "{}(file={}, rank={})".format(
            self.__class__.__name__, self.file, self.rank)

    def __str__(self):
        return '{}{}'.format(self.file, self.rank)


def starting_board():
    return {'♕♖': ChessCoordinate('a', 1),
            '♕♘': ChessCoordinate('b', 1),
            '♕♗': ChessCoordinate('c', 1),
            '♕♕': ChessCoordinate('d', 1),
            '♔♔': ChessCoordinate('e', 1),
            '♔♗': ChessCoordinate('f', 1),
            '♔♘': ChessCoordinate('g', 1),
            '♔♖': ChessCoordinate('h', 1),
            '♕♖♙': ChessCoordinate('a', 2),
            '♕♘♙': ChessCoordinate('b', 2),
            '♕♗♙': ChessCoordinate('c', 2),
            '♕♕♙': ChessCoordinate('d', 2),
            '♔♔♙': ChessCoordinate('e', 2),
            '♔♗♙': ChessCoordinate('f', 2),
            '♔♘♙': ChessCoordinate('g', 2),
            '♔♖♙': ChessCoordinate('h', 2),
            '♛♜': ChessCoordinate('a', 8),
            '♛♞': ChessCoordinate('b', 8),
            '♛♝': ChessCoordinate('c', 8),
            '♛♛': ChessCoordinate('d', 8),
            '♚♚': ChessCoordinate('e', 8),
            '♚♝': ChessCoordinate('f', 8),
            '♚♞': ChessCoordinate('g', 8),
            '♚♜': ChessCoordinate('h', 8),
            '♛♜♟': ChessCoordinate('a', 7),
            '♛♞♟': ChessCoordinate('b', 7),
            '♛♝♟': ChessCoordinate('c', 7),
            '♛♛♟': ChessCoordinate('d', 7),
            '♚♚♟': ChessCoordinate('e', 7),
            '♚♝♟': ChessCoordinate('f', 7),
            '♚♞♟': ChessCoordinate('g', 7),
            '♚♜♟': ChessCoordinate('h', 7),
            }


def main():
    # check how many memory utilized to store 320000 instances of the
    # ChessCoordinate with interning technique.
    # Creating 10000 chessboards dictionaries
    boards = [starting_board() for _ in range(10000)]
    pass


if __name__ == '__main__':
    main()
