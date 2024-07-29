import threading
import time as tm 
def show(str):
    for i in range(7):
        print("Good Morning",str)
        if(str=="sushant"):
            tm.sleep(0.9)
def show1(str):
    print("good even ", str)
print("Main Thread")
t1 = threading.Thread(target=show,args=("sushant",))
t1.start()
t1.join()


t2 = threading.Thread(target=show1, args=("Rohan",))
t2.start()
 


t3 = threading.Thread(target=show ,args=("vinayak",))
t3.start()


t4 = threading.Thread(target=show1, args=("shivtej",))
t4.start()

