import threading as t
def print_number():
    for i in range(100):
        print(i)

print("Main Thread")
t1=t.Thread(target=print_number)
t1.start()
t1.join*9

t2=t.Thread(target=print_number)
t2.start()

t3=t.Thread(target=print_number)
t3.start()

t4=t.Thread(target=print_number)
t4.start()