import threading
import time
def cup_heavy():
    print(f"Crunching some numbers...")
    total=0
    for i in range(10**7):
        total+=i
    print("DONE")
start=time.time()
threads=[threading.Thread(target=cup_heavy) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]
print(f"Total time taken: {time.time()-start:.2f} seconds")