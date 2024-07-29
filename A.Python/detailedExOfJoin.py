import threading
def show():
    print("Good Morning")
print("Main Thread")
for i in range(5):
    my_thread=threading.Thread(target=show)
    my_thread.start()
    my_thread.join()
print("Main Thread Exit")