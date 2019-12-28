import threading,time

x=0
def increment():
    global x
    x+=1

def thread_stack():
    for x in range(10000):
        increment()

def main_task():
    global x
    x=0
    t1=threading.Thread(target=thread_stack,name="Thread1")
    time.sleep(1)
    t2=threading.Thread(target=thread_stack,name="Thread2")
    time.sleep(1)
    t3=threading.Thread(target=thread_stack,name="Thread3")
    time.sleep(1)
    t4=threading.Thread(target=thread_stack,name="Thread4")

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    #t1.join()
    t2.join()
    # t3.join()
    # t4.join()

if __name__ == '__main__':
    for i in range(10):
        main_task()
        time.sleep(1)
        print("Iteration{0}:x={1}".format(i,x))

