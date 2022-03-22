class Solution:
    def fb_func(self, m: int) -> str:
            if m % 3 == 0 and m % 5 == 0:
                return "FizzBuzz"
            elif m % 3 == 0 and m % 5 != 0:
                return "Fizz"
            elif m % 3 != 0 and m % 5 == 0:
                return "Buzz"
            else:
                return str(m)
            
    def fizzBuzz(self, n: int) -> List[str]:
            
        return list(map(self.fb_func, [i for i in range(1, n+1)]))
