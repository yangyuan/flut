from typing import override
from flut._flut.engine import FlutValueObject, _flut_pack_value
from flut._flut.runtime import _flut_unpack_optional_field, _flut_unpack_required_field


class _Duration(FlutValueObject):
    _flut_type = "Duration"

    def __init__(
        self,
        *,
        days: int = 0,
        hours: int = 0,
        minutes: int = 0,
        seconds: int = 0,
        milliseconds: int = 0,
        microseconds: int = 0,
    ):
        super().__init__()
        self._microseconds = (
            days * 86400000000
            + hours * 3600000000
            + minutes * 60000000
            + seconds * 1000000
            + milliseconds * 1000
            + microseconds
        )

    @property
    def inMicroseconds(self) -> int:
        return self._microseconds

    @property
    def inMilliseconds(self) -> int:
        return self._microseconds // 1000

    @property
    def inSeconds(self) -> int:
        return self._microseconds // 1000000

    @property
    def inMinutes(self) -> int:
        return self._microseconds // 60000000

    @property
    def inHours(self) -> int:
        return self._microseconds // 3600000000

    @property
    def inDays(self) -> int:
        return self._microseconds // 86400000000

    @property
    def isNegative(self) -> bool:
        return self._microseconds < 0

    def abs(self) -> "_Duration":
        return _Duration(microseconds=abs(self._microseconds))

    def compareTo(self, other: "_Duration") -> int:
        if self._microseconds < other._microseconds:
            return -1
        if self._microseconds > other._microseconds:
            return 1
        return 0

    @staticmethod
    def _flut_unpack(data: dict) -> "_Duration":
        return _Duration(
            microseconds=_flut_unpack_required_field(data, "microseconds"),
        )

    @override
    def _flut_pack(self) -> dict:
        result = self._flut_base_props()
        result["microseconds"] = _flut_pack_value(self._microseconds)
        return result

    def __repr__(self):
        return f"Duration(microseconds={self._microseconds})"

    def __eq__(self, other):
        if isinstance(other, _Duration):
            return self._microseconds == other._microseconds
        return False

    def __hash__(self):
        return hash(self._microseconds)

    def __lt__(self, other):
        if isinstance(other, _Duration):
            return self._microseconds < other._microseconds
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, _Duration):
            return self._microseconds <= other._microseconds
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, _Duration):
            return self._microseconds > other._microseconds
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, _Duration):
            return self._microseconds >= other._microseconds
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, _Duration):
            return _Duration(microseconds=self._microseconds + other._microseconds)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, _Duration):
            return _Duration(microseconds=self._microseconds - other._microseconds)
        return NotImplemented

    def __neg__(self):
        return _Duration(microseconds=-self._microseconds)

    def __mul__(self, factor):
        return _Duration(microseconds=int(self._microseconds * factor))

    def __floordiv__(self, quotient):
        return _Duration(microseconds=self._microseconds // quotient)


class Duration(_Duration):
    zero = _Duration()

    microsecondsPerMillisecond = 1000
    millisecondsPerSecond = 1000
    secondsPerMinute = 60
    minutesPerHour = 60
    hoursPerDay = 24

    microsecondsPerSecond = microsecondsPerMillisecond * millisecondsPerSecond
    microsecondsPerMinute = microsecondsPerSecond * secondsPerMinute
    microsecondsPerHour = microsecondsPerMinute * minutesPerHour
    microsecondsPerDay = microsecondsPerHour * hoursPerDay

    millisecondsPerMinute = millisecondsPerSecond * secondsPerMinute
    millisecondsPerHour = millisecondsPerMinute * minutesPerHour
    millisecondsPerDay = millisecondsPerHour * hoursPerDay

    secondsPerHour = secondsPerMinute * minutesPerHour
    secondsPerDay = secondsPerHour * hoursPerDay

    minutesPerDay = minutesPerHour * hoursPerDay
