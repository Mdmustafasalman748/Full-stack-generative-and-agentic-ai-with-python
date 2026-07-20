from multiprocessing import Process
import time
def brew_chai(name):
    print(f"Start of {name} chai brewing")
    time.sleep(3)
    print(f"End of {name} chai brewing")
    
if __name__=="__main__":
    chai_makers=[
        Process(target=brew_chai, args=(f"chai maker {i}",)) for i in range(3)
    ]
    
    #start all processes
    for p in chai_makers:
        p.start()
        
    #wait for all processes to finish
    for p in chai_makers:
        p.join()
        
    print("All chai served")