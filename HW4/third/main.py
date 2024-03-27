import codecs
import time
from multiprocessing import Process, Queue, Pipe
from datetime import datetime


def process_a(input_queue, output_pipe):
    while True:
        message = input_queue.get()
        print(f"{datetime.now()} Process A received: {message}")
        processed_message = message.lower()
        output_pipe.send(processed_message)
        time.sleep(5)



def process_b(input_pipe, output_pipe):
    while True:
        message = input_pipe.recv()
        print(f"{datetime.now()} Process B received: {message}")

        encoded_message = encode_rot13(message)
        output_pipe.send(encoded_message)

def encode_rot13(message):
    return codecs.encode(message, 'rot_13')

def main():
    input_queue = Queue()

    pipe_a_to_b, pipe_b_to_a = Pipe()
    pipe_b_to_main, pipe_main_to_b = Pipe()

    process_a_instance = Process(target=process_a, args=(input_queue, pipe_a_to_b))
    process_b_instance = Process(target=process_b, args=(pipe_b_to_a, pipe_b_to_main))

    process_a_instance.start()
    process_b_instance.start()

    try:
        while True:
            message = input("Enter a message:\n")
            if message == '':
                break
            input_queue.put(message)
            encoded_message = pipe_main_to_b.recv()
            print(f"{datetime.now()} Main process received: {encoded_message}")

    finally:
        process_a_instance.terminate()
        process_b_instance.terminate()


