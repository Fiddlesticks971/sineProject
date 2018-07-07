from billiard import Process
from time import sleep

def f(x):
    for i in range(0,4):
        print("this is thread {}".format(x))

def main():
    ProcessList=[]
    for i in range(0,100):
        ProcessList.append(Process(target=f,args=(i,)))
    for p in ProcessList:
        p.start()
    sleep(5)
    for p in ProcessList:
        p.join()
    print("main finished")

main()

                           
                        
