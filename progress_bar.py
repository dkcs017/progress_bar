import sys
import time

block=u'\u2588'
def __init__progressbar(width):
    sys.stdout.write("[{blank}]".format(blank=" "*width))
    sys.stdout.flush()
    sys.stdout.write("\b"*(width+1))

def __update__progressbar(fill):
    sys.stdout.write(fill)
    sys.stdout.flush()

def __finish__progressbar():
    sys.stdout.write("\n")


if __name__ == '__main__':
    size=50
    __init__progressbar(size)
    for i in range(size):
        __update__progressbar(block)
	time.sleep(0.2)
    __finish__progressbar()
