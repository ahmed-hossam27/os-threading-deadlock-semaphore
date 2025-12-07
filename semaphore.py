import threading
import time

semaphore = threading.Semaphore(2)

def access_resource(name):
    print(f"{name} is waiting...")
    with semaphore:
        print(f"{name} entered")
        time.sleep(2)
        print(f"{name} exited")

threads = []
for i in range(5):
    t = threading.Thread(target=access_resource, args=(f"Thread {i+1}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Semaphore example completed.")
