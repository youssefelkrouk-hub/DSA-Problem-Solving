import threading 
import time



# # Initialize semaphore with 0 so acquire() will wait immediately 
# signal_sem=threading.Semaphore(0) 

# Start with 1 ticket available
signal_sem_1 = threading.Semaphore(1)

print("Taking the semaphore")
signal_sem_1.acquire()  # Counter drops from 1 to 0 (succeeds immediately!)
time.sleep(2) # doing the work i this phase 
print("Release the semaphore !!")
signal_sem_1.release()  # Counter goes back up to 1
print("\n")
signal_sem=threading.Semaphore(0)
def worker_task():
    print("Worker: Starting long background task...") 
    # "Put this thread to sleep for 2 seconds, don't give it CPU time, and wake it up when time is up."
    time.sleep(2)  # Simulate heavy work  !!
    # wake up the thread after 2 seconds of sleeping 
    print("Worker: Task finished!") 
    
    # SIGNAL: Increments counter to 1 and unblocks main thread
    print("Worker: Sending signal()...")
    signal_sem.release()

def main_task():
    print("Main: Starting worker thread...")
    t = threading.Thread(target=worker_task)
    t.start()
    
    print("Main: Waiting for worker to signal completion...")
    
    # WAIT: Blocks execution here until worker calls release()
    signal_sem.acquire()
    
    print("Main: Received signal! Resuming main execution.")

# main_task()
























# import threading
# import time


# # Allow a maximum of 2 threads to enter at the same time
# max_connections = threading.Semaphore(1)


# def worker(thread_id):
#     print(f"Thread {thread_id} is waiting to enter...")
    
#     # 'with' automatically calls acquire() on entry and release() on exit
#     with max_connections:
#         print(f"--> Thread {thread_id} ENTERED the restricted zone.")
#         time.sleep(2)  # Simulate doing work 
#         print(f"<-- Thread {thread_id} LEAVING the restricted zone.")

# # Start 5 threads competing for 2 slots
# threads = []
# for i in range(1, 6):
#     t = threading.Thread(target=worker, args=(i,))
#     threads.append(t)
#     t.start()

