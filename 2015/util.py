import time


def read_data(filepath):
    rows = []
    with open(filepath, 'r') as infile:
        for line in infile:
            rows.append(line.rstrip())

    return rows


def read_data_as_int(filepath):
    rows = []
    with open(filepath, 'r') as infile:
        for line in infile:
            rows.append(int(line.rstrip()))

    return rows


def log(msg, log_msg=False):
    if log_msg:
        print(msg)


# Below used like: util.measure_time_for(lambda: run_me(input, input2))
# def measure_time_for(func):
#     start_time = time.time()
#     func()
#     elapsed_time = time.time() - start_time
#     print('Operation %s took=%s seconds' % (func, elapsed_time))


def measure_time_for(func, *args):
    start_time = time.time()
    func(*args)
    elapsed_time = time.time() - start_time
    print('Operation %s took=%s seconds' % (func.__name__, elapsed_time))


# Better timeit decorator
# Credits goes to https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator
def timeit(f):
    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print('func:%r args:[%r, %r] took: %2.4f sec' % (f.__name__, args, kw, te-ts))
        return result

    return timed