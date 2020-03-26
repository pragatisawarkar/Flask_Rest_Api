import random,time,os,_random
import threading,sys
class Cake:
    def __init__(self,cid,cname,cprice):
        self.Cake_id=cid
        self.cake_Name=cname
        self.cake_Price=cprice

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)

bakery=[]
def preparecakes():
    time.sleep(5)
    return Cake(cid=random.randint(111,999),cname="AAA"+str(random.randint(1111,9999)),cprice=random.randint(300,1000))

###########--------------Producer task------------------##############
def producer_task():
    while True:
        global bakery
        cake=preparecakes()
        print(threading.current_thread().name,":",bakery)
        bakery.append(cake)

###########--------------Consumer task------------------##############
def consumer_task():
    while True:
        time.sleep(10)
        global bakery
        if len(bakery)>0:
            cake=bakery.pop(0)
            print(threading.current_thread().name,":",cake)
        else:
            print("No cakes are available for current time...")

#############-----------------Main Task------------------###################################
def main_task():
    t1=threading.Thread(name="Producer:",target=producer_task)
    t2=threading.Thread(name="Consumer:",target=consumer_task)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main_task()
    print('--------------------------------------')
    print('Final-------------state of bakery',bakery)