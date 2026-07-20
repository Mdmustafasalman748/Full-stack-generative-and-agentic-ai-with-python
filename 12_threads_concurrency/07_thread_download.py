import threading
import requests
import time
def download(ur):
    print(f"Started downloading from {ur}")
    resp=requests.get(ur)
    print(f"Finished downloading from {url}, size: {len(resp.content)} bytes")

urls=[
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg"
]
start=time.time()
threads=[]
for url in urls:
    t=threading.Thread(target=download, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end=time.time()
print(f"Total time taken: {end-start:.2f} seconds")