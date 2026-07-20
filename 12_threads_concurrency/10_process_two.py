from multiprocessing import Process
import time
def cup_heavy():
    print(f"Crunching some numbers...")
    total=0
    for i in range(10**7):
        total+=i
    print("DONE")

if __name__=="__main__":
    start=time.time()
    processes=[Process(target=cup_heavy) for _ in range(2)]
    [t.start() for t in processes]
    [t.join() for t in processes]
    print(f"Total time taken: {time.time()-start:.2f} seconds")