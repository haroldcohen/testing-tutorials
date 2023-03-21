class UnitOfWorkMemento:
    """UnitOfWorkMemento"""

    def __init__(self, state: int):
        self.state = state

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            attributes_to_compare = list(filter(lambda a: not a.startswith("_"), dir(self)))
            for attribute in attributes_to_compare:
                if getattr(self, attribute) != getattr(other, attribute):
                    return False
            return True
        return False
