from multiprocessing import Pool


class FizzBuzzer:
    def __init__(self):
        self.n = 0

    def foo(self, _):
        self.n += 1
        if (self.n % 3) == 0:
            x = f"{self.n}  buzz"
        else:
            x = f"{self.n} fizz"
        print(f"input {_}", end=" ")
        print(f"n = {self.n}", end=" --> ")
        print(x)
        return x


if __name__ == "__main__":
    FB = FizzBuzzer()
    with Pool() as P:
        result_with_parallel = P.map(FB.foo, range(21))

    print(list(result_with_parallel))

    result = map(FB.foo, range(21))
    print(list(result))

    # for i in range(21):
    #     FB.foo(i)
