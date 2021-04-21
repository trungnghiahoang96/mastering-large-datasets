from time import perf_counter, sleep
from multiprocessing import Pool


def times_two(x):
  return x*2+7


def lazy_map(xs):
  return list(map(times_two, xs))


def parallel_map(xs, chunck=8500):
  with Pool(2) as P:
    x =  P.map(times_two, xs, chunck)
  return x


for i in range(0, 7):
  N = 10**i
  t1 = perf_counter()
  lazy_map(range(N))
  lm_time = perf_counter() - t1

  t1 = perf_counter()
  parallel_map(range(N))
  par_time = perf_counter() - t1
  print("""
-- N = {} --
Lazy map time:      {}
Parallel map time:  {}
""".format(N, lm_time, par_time))
