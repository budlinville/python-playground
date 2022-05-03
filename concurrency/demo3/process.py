from time import time
import concurrent.futures
import time

def sleep_for_a_bit(seconds):
    print(f"Sleeping {seconds} second(s)")
    time.sleep(seconds)
    return "Done sleeping"

start = time.perf_counter()

with concurrent.futures.ProcessPoolExecutor() as executor:
    if __name__ == '__main__':
        f1 = executor.submit(sleep_for_a_bit, 1)
        f2 = executor.submit(sleep_for_a_bit, 1)
        print(f1.result())
        print(f2.result())

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} seconds')
