from base import GroupBase

class CyclicGroup(GroupBase):
    def __init__(self, order):
        super().__init__(
            dimension=1,
            identity=[0.]
        )
