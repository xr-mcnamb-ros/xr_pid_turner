from BasePID import AbstractPID


class SamplePID(AbstractPID):
    def __init__(self):
        self._p = 300
        self._i = 0
        self._d = 200

    def setPID(self, p: int, i: int, d: int) -> None:
        self._p = p
        self._i = i
        self._d = d

    def showPID(self):
        print("P: {}\nI: {}\nD: {}".format(self._p, self._i, self._d))
        print("-" * 20)
