from billiard import Pool

def f(x):
    return x*x

def main():
    p=Pool(5)
    A=[]
    for i in range(0,100):
        A.append(i)
    print(p.map(f,A))
main()    
