from time import time


class Timer:

    times = []
    item_length = 1

    def __init__(self):
        pass

    @classmethod
    def measure(cls, function):
        def wrapper(*args):
            start = time()
            result = function(*args)
            cls.times.append([len(cls.times)] + list(args) + [time() - start])
            return result

        return wrapper

    def get_max_duration(self):
        return max(self.times, key=lambda x: x[-1])[-1] if len(self.times) > 0 else 0

    def get_min_duration(self):
        return min(self.times, key=lambda x: x[-1])[-1] if len(self.times) > 0 else 0

    def get_max_duration_case(self):
        return max(self.times, key=lambda x: x[-1]) if len(self.times) > 0 else 0

    def get_min_duration_case(self):
        return min(self.times, key=lambda x: x[-1]) if len(self.times) > 0 else 0

    def clear_times(self):
        self.times = []


timer = Timer()
