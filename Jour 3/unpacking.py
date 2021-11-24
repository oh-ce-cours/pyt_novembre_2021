from typing import List, Union

l:List[Union[bool, str, tuple]] = [
    [True, "message", (1, 2, 3)],
    [False, "casse", (1, 1, 1)],
    [True, "super", (-1, 3, 5)],
]

status, _, (_, coord_y, _) = l[0]