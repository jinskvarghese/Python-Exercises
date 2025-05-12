import time

def time_this(func):
    def wrapper(*args, **kwargs):
        print(f"--> Running {func.__name__}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"--> {func.__name__} ran in {end_time - start_time:.9f} seconds")
        return result
    return wrapper

@time_this
def sleeper_func(sleeptime):
    print(f"sleeping for {sleeptime}")
    time.sleep(sleeptime)
    return 'Woke up!'

sleeper_func(2)
