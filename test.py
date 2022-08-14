class Solutin():
    def solution(start: int, target: int) -> int:
        
        queue = [start + 1, start * start]

        steps = 0
        while queue:


