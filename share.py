from fbchat import Client
from fbchat.models import *
import sys
import os
import time


def send_with_messenger():
    client = Client('kim.john228@gmail.com', 'Fjohnkim0414')
    threads = client.fetchThreadList(limit=5)
    print("Threads: {}".format(threads))

    thread_id = choose_receiver(threads)
    thread_type = ThreadType.GROUP

    for file_name in os.listdir('./imgs'):
        client.sendLocalImage('./imgs/' + file_name, thread_id=thread_id, thread_type=thread_type)
        time.sleep(3)


def choose_receiver(threads_):
    for h, thread in enumerate(threads_):
        if thread.type == ThreadType.GROUP:
            print(str(h + 1) + ': ' + thread.name)
        else:
            print(str(h + 1) + ': ' + thread.first_name + ' ' + thread.last_name)

    pick = input('\nSend dank memes to which client? (1/2/3/4/5)')
    try:
        pick = int(pick)
        if pick not in range(1, 6):
            print('Error: input must be an integer between 1 and 5.')
            sys.exit(0)
    except ValueError:
        print('Error: invalid input')
        sys.exit(0)

    thread_id = threads_[pick - 1].uid
    return thread_id