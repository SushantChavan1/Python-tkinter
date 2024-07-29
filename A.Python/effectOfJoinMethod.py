import threading
def show():
     for i in range(5):
          print(f'In thread {i}')
print("Main Thread")
my_thread=threading.Thread(target=show)
my_thread.start()
my_thread.join()
print("Main Thread Exit")