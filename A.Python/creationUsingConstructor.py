import threading
def show():
    print("I am thread created by main")
print("Mani thread")
my_Thread=threading.Thread(target=show)
my_Thread.start()
my_Thread.join()
print("Main Thread Exit")