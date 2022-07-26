"""
students = {
    "bob": [2, 2, 2],
    "joe": [1, 1],
    "adam": [4],
    "sam": [5, 5, 5],
    "tom": [],
}

Problem: print out students in descending order of their average marks.
Lists with the marks may be empty

# sam [5, 5, 5] 5
# adam [4, 3] 3.5
# bob [1, 2, 3] 2
"""
from typing import Dict, List
import sys


students = {
    "bob": [2, 2, 2],
    "joe": [1, 1],
    "adam": [4],
    "sam": [5, 5, 5],
    "tom": [],
}


def solution(students: Dict[str, List[int]]) -> None:
    avg_marks = {k: sum(v)/len(v) if v else 0 for k, v in students.items()}

    avg_gen = iter(sorted(avg_marks.items(),
                          key=lambda item: item[1],
                          reverse=True))

    for n, avg in avg_gen:
        print(n, students[n], avg)


if __name__ == '__main__':
    solution(students)
