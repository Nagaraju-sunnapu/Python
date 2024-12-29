# program for demonstrating the current_thread() infromation
import threading 
t1=threading.current_thread()
print("default thread information=",t1)
print("default threadname=",t1.name)
print("---------------------OR-----------------------")
print("default thread name=",threading.current_thread().name)
