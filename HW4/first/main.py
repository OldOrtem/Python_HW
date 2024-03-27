import time
import threading
import multiprocessing


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def run_sync(n):
    start_time = time.time()
    for _ in range(10):
        fibonacci(n)
    end_time = time.time()
    return end_time - start_time

def run_threading(n):
    start_time = time.time()
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=fibonacci, args=(n,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    return end_time - start_time

def run_multiprocessing(n):
    start_time = time.time()
    processes = []
    for _ in range(10):
        process = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    end_time = time.time()
    return end_time - start_time
def main():
    n = 50
    with open("artifacts/1.txt", 'w') as file:
        file.write(f"sync {run_sync(n)}\n")
        file.write(f"thread {run_threading(n)}\n")
        file.write(f"process {run_multiprocessing(n)}\n")