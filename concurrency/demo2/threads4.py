import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]  # This will look like they all complete at once..
                        # but really the printing is just waiting on do_something(5) in executor.map to finish
    # secs = [1,2,3,4,5]  # This behaves similar to threads3.py
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
