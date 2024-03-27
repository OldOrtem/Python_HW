import math
import concurrent.futures
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


def split_number(N, M):
    segment_size = N // M
    remainder = N % M
    start = 0
    for i in range(M):
        end = start + segment_size
        if i < remainder:
            end += 1
        yield start, end
        start = end
def worker(f, a, step, i, N):
    result = 0
    for i in range(i, N):
        result += f(a + i * step) * step
    return result


def integrate(f, a, b, *, n_jobs=1, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
        futures = []
        segments = list(split_number(n_iter, n_jobs))
        for i, (start, end) in enumerate(segments):
            futures.append(executor.submit(worker, f, a, step, start, end))

        for future in concurrent.futures.as_completed(futures):
            acc += future.result()
    return acc

def integrate_process_pool(f, a, b, *, n_jobs=1, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    with concurrent.futures.ProcessPoolExecutor(max_workers=n_jobs) as executor:
        futures = []
        segments = list(split_number(n_iter, n_jobs))
        for i, (start, end) in enumerate(segments):
            futures.append(executor.submit(worker, f, a, step, start, end))

        for future in concurrent.futures.as_completed(futures):
            acc += future.result()
    return acc

def main():
    cpu_num = 8
    n_jobs_list = list(range(1, cpu_num * 2 + 1))
    results_thread = []
    results_process = []
    for n_jobs in n_jobs_list:
        start_time = time.time()
        integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
        end_time = time.time()
        results_thread.append(end_time - start_time)
        logging.info(f'ThreadPoolExecutor with {n_jobs} workers took {end_time - start_time} seconds.')

    for n_jobs in n_jobs_list:
        start_time = time.time()
        integrate_process_pool(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
        end_time = time.time()
        results_process.append(end_time - start_time)
        logging.info(f'ProcessPoolExecutor with {n_jobs} workers took {end_time - start_time} seconds.')

    with open('artifacts/2.txt', 'w') as f:
        f.write('n_jobs\tThreadPoolExecutor\tProcessPoolExecutor\n')
        for i in range(len(n_jobs_list)):
            f.write(f'{n_jobs_list[i]}\t{results_thread[i]}\t{results_process[i]}\n')


