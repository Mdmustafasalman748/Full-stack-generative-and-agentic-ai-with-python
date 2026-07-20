import threading
import time
def boil_milk():
    print(f"Boiling milk")
    time.sleep(2)
    print(f"Milk boiled...")

def toast_bun():
    print(f"Toasting bun")
    time.sleep(3)
    print(f"Done with bun toast...")

start=time.time()
thread1=threading.Thread(target=boil_milk)
thread2=threading.Thread(target=toast_bun)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end=time.time()

print(f"Total time taken: {end-start:.2f} seconds")