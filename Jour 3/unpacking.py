from typing import List, Any, Tuple

type_coords = Tuple[int, int, int]
l:List[Tuple[bool, str, type_coords]] = [
    (True, "message", (1, 2, 3)),
    (False, "casse", (1, 1, 1)),
    (True, "super", (-1, 3, 5)),
]

status, b, c = l[0]
for status, _, (_, coord_y, _) in l:
    print(status, coord_y)