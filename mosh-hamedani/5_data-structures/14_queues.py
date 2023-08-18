#FIFO - First In First Out
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft() #We don't have this method in list object
print(queue)
if not queue:
    print("empty")


























