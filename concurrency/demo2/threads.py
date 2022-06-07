from threading import Thread
import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

t1 = Thread(target=do_something)
t2 = Thread(target=do_something)

t1.start()
t2.start()

# blocks execution until these threads have finished
t1.join()
t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
