from multiprocessing import Process
from time import sleep

def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s  "%name)
        print("I'm working ...")


#p=Process(target=worker,args=(2,'Tom'))
# p=Process(target=worker,kwargs={'sec':2,'name':'Tom'})
p=Process(target=worker,args=(2,),
          kwargs={'name':'Tom'},
          daemon=True)
p.start()
sleep(5.9)
# p.join()
print("父进程结束了")





