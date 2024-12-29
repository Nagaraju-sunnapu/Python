# program for finding the number of threads active in the program 
import threading 
print("name of the active thread=",threading.current_thread().name)
print("number of the active threads=",threading.active_count())