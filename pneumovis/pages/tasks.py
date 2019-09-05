"""
Tasks class to run background tasks on a schedule while the server is running. 
Tasks are to be run sequentially in a thread parallel to the server thread.
"""
import threading    # for parallel thread
import time         # for sleeping
running = True
print("Starting background tasks...")

def task_start():
    print("Tasks are being re-run")

def run_tasks():
    global running
    while(running):
        task_start()


        time.sleep(600)

task_thread = threading.Thread(target=run_tasks, args=(), kwargs={})
task_thread.setDaemon(True)
task_thread.start()