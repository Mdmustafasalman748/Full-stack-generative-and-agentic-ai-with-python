import threading
import time
def brew_chai():
    print(f"{threading.current_thread().name} started brewing")
    count=0
    for _ in range(100_00_000):
        count+=1
    print(f"{threading.current_thread().name} finished brewing")
    
thread1=threading.Thread(target=brew_chai, name="Barista 1")
thread2=threading.Thread(target=brew_chai, name="Barista 2")
start_time=time.time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Total time taken: {time.time()-start_time:.2f} seconds")