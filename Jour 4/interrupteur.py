from enum import Enum
class Status(Enum):
    ON = 1
    OFF = 2
    UNKNOWN = 3


print(Status.ON)