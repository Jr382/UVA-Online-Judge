from time import time


class Timer:

    cases = []

    def __init__(self):
        pass

    def __iter__(self):
        for case in self.cases:
            yield case

    @classmethod
    def measure(cls, function):
        def wrapper(*args):
            start = time()
            result = function(*args)
            cls.cases.append([len(cls.cases)] + list(args) + [time() - start])
            return result

        return wrapper

    def get_max_duration(self):
        return self.get_max_duration_case()[-1]

    def get_min_duration(self):
        return self.get_min_duration_case()[-1]

    def get_max_duration_case(self):
        return max(self.cases, key=lambda x: x[-1]) if len(self.cases) > 0 else [None]

    def get_min_duration_case(self):
        return min(self.cases, key=lambda x: x[-1]) if len(self.cases) > 0 else [None]

    def clear_times(self):
        self.cases = []


timer = Timer()
