import time
import threading

def fun_loop():
    while True:
        print("Monitoring............")
        time.sleep(1)

t1 = threading.Thread(target=fun_loop, daemon=True)
t1.start()
print("\nMain:", threading.current_thread().name)
print("\nMain: Finished Executing")