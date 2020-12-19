class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        i = 1
        while i < n+1:
            word = str(i)
            if i%3 == 0:
                word = "Fizz"
            if i%5 == 0:
                word = "Buzz"
            if i%15 == 0:
                word = "FizzBuzz"
            arr.append(word)
            i += 1
        return arr
