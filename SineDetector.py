from billiard import Process,Queue,Pipe
import time
import math

def tickTock(timePipe):
    while True:
        time.Sleep(.01)
        if timePipe.recv() == "*":
            timePipe.send(time.clock())
         

def signal(q,sigPipe,valueArray):
    while True:
        while sigPipe.recv()=="*":
            print("*")
        sigPipe.sent("*")
        output = 0
        for f in valueArray:
            output = output+ math.sin(f*time.clock())
        q.put("signal : {}".format(output))

def main():
    timePipe,sigPipe = Pipe()
    q=Queue()
    clock = Process(target=tickTock,args=(timePipe,))
    testSignal = Process(target=signal,args=(q,sigPipe,[1]))
    testSignal.start()
    while True:
        print(q.get())
main()
