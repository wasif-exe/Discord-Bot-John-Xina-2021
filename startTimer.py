import threading
import random
interval = 5


def myPeriodicFunction():
    interval = random.randint(1,15)
    print ("This loops on a random time this time %d seconds" % interval)
    

def startTimer():
    
    threading.Timer(interval, startTimer).start()
    myPeriodicFunction()
    