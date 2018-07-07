from billiard import Process, Queue
import os

def f(q,x):
    q.put("process:{} value:{}".format(os.getpid(),x))

def main():
    q = Queue()
    x=[1,2,3,4,5]
    pl=[]
    for i in x:
        pl.append(Process(target=f,args=(q,i,)))
    for p in pl:
        p.start()
        p.join()
    for i in x:
       print(q.get())

main()
