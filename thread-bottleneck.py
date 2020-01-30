import time
import threading

def fib(n):
  if n == 0 or n == 1:
    return 1
  return fib(n - 1) + fib(n - 2)

def do():
  thread_name = threading.currentThread().getName()
  for iteration in range(5):
    n = 32
    start = time.time()
    value = fib(n)
    time_taken = format(time.time() - start, '.2f')
    print(f"thread {thread_name}: iteration {iteration}: calculated fib({n}) = {value} in {time_taken} seconds")


def test_thread(count):
  print(f"running test_thread with {count} iterations")

  threads = [threading.Thread(target=do, name=str(t)) for t in range(count)]
  for t in threads:
    t.start()
  for t in threads:
    t.join()


if __name__ == '__main__':
  test_thread(1)
  test_thread(2)
  test_thread(3)
