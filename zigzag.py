# animate a zigzag
# write from memory only

import time, sys

indent = 0
increase = True

try:
    while True:
        print('.' * indent + 'Ohai')
        indent += 1 if increase else -1
        if indent == 10:
            increase = False
        elif indent == 0:
            increase = True
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()