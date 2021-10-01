import threading
import time

class myThread (threading.Thread):
   def __init__(self, name, delay):
      threading.Thread.__init__(self)
      self.name = name
      self.delay = delay
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, 5, self.delay)
      print ("Exiting " + self.name)

def print_time(threadName, counter, delay):
   while counter:
      if (counter == 0):
         threadName.exit()
      time.sleep(delay)
      print (threadName + ":" + time.ctime(time.time()))
      counter -= 1

# Initializing Threads
thread1 = myThread("Thread-1", 1)
thread2 = myThread("Thread-2", 2)
thread3 = myThread("Thread-3", 3)
thread4 = myThread("Thread-4", 4)


# Starting Thread Process
thread1.start()
thread2.start()
thread3.start()
thread4.start()

print ("Exiting Main Thread \n")
