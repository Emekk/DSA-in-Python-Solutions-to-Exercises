import typing


# C-2.24
# see "C-2.24.png"

# C-2.25
def __mul__(self, other: typing.Union[Vector, int, float]) -> Vector:
    result = Vector(len(self))
    if isinstance(other, (int, float)):
        for j in range(len(result)):
            result[j] = other * self[j]
        return result
    elif isinstance(other, Vector):
        for j in range(len(result)):
            result[j] = self[j] * other[j]
        return result
    else:
        raise TypeError("Invalid type for multiplication!")

# C-2.26
class ReversedSequenceIterator:
    def __init__(self, sequence: typing.Union[list, tuple, str]) -> None:
        self._seq = sequence
        self._k = len(self._seq)  # start from the end of the sequence

    def __next__(self) -> typing.Any:
        self._k -= 1  # advance in reversed direction
        if self._k > -1:
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        return self

# C-2.27
def __contains__(self, elem: typing.Union[int, float]) -> bool:
    if self._step < 0:
        if elem <= self._stop or elem > self._start:
            return False
    else:
        if elem >= self._stop or elem < self._start:
            return False
    return (elem - self._start) % self._step == 0


# C-2.28
# - first add a instance variable, attribute, named '_ncharge', which keeps the number of charges of the current
#     month, to the class PredatoryCreditCard.
# - increment self._ncharge by 1 in the charge() method.
# - modify the process_month() method as below
def process_month(self):
    if self._balance > 0:
        # if positive balance, convert APR to monthly multiplicative factor 
        monthly_factor = pow(1 + self._apr, 1/12) 
        self._balance *= monthly_factor
    # surcharge
    self._balance += max(0, self._nharge - 10)
    self._ncharge = 0  # reset for the next month

# C-2.29
# - first add instance variables, named '_payment_made', '_late_fee', and '_mmpp', which, respectively, keeps the 
#     total payment made in the current month, is the late fee, and is the minimum monthly payment percentage, to 
#     the class PredatoryCreditCard.
# - modify the process_month() method as below
def process_month(self):
    if self._balance > 0:
        # if positive balance, convert APR to monthly multiplicative factor 
        monthly_factor = pow(1 + self._apr, 1/12) 
        self._balance *= monthly_factor
        # minimum monthly payment
        if self._payment_made / self._balance < self._mmpp:
            self._balance += self._late_fee

# C-2.30
def _set_balance(self, b: typing.Union[int, float]) -> None:
    self._balance = b

# C-2.31
class AbsDiffProgression(Progression):
    def __init__(self, first: typing.Union[int, float] = 2, second: typing.Union[int, float] = 200):
        self.super().__init__(first)
        self._prev, self._current = self._current, second

    def __advance__(self):
        temp = self._current
        self._current = abs(self._current - self._prev)
        self._prev = temp

# C-2.32
class SqrtProgression(Progression):
    def __init__(self, start: typing.Union[int, float] = 65_536):
        self.super().__init__(start)

    def __advance__(self):
        self._current = self._current**0.5
