import time
import threading
import datetime

shutdown_event = threading.Event()

def dowork():
    while not shutdown_event.is_set():
        print(datetime.datetime.now())
        time.sleep(1.0)
    print 'ending dowork'

def main():

    t = threading.Thread(target=dowork(), args=(), name='worker')
    t.start()

    print("Instance started")

    try:
        while t.isAlive():
            t.join(timeout=1.0)
            print 'ending main'
    except (KeyboardInterrupt, SystemExit):
        shutdown_event.set()
    pass

if __name__ == '__main__':
    main()
