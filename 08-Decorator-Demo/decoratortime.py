# Exercise Name:
# 	08-Decorator-Demo
# Description:
# 	Create a decorator called 'time_this' and use it to measure time taken to run functions

# For example, running:
# 	@time_this
# 	def sleeper_func(sleeptime):
# 	    print(f'sleeping for {sleeptime}')
# 	    sleep(sleeptime)
# 	    return 'Woke up!'

# 	sleeper_func(2)

# Sould output the following in the console:
# 	--> Running sleeper_func
# 	sleeping for 2
# 	--> sleeper_func ran in 2.002105236053467 seconds

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
