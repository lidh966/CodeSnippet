#### Using deque(maxlen=N) to create a fixed-sized queue ####
#### When new items are added and the queue is full, the oldest item will be automatically removed ####
from collections import deque

def search(lines, pattern, history):
    previous_lines = deque(maxlen=history)    # create a queue with fixed size of history
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)