import threading
print("Current Thread")
print("Curreant Running Thread::",threading.current_thread().getName)
if threading.current_thread()==threading.main_thread():
    print("Current htread is main")
else:
    print("Not main thread")