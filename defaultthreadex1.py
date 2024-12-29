# program for showing the default thread present in python program 
import threading 
tname=threading.current_thread().name
print("default thread name=",tname)
noth=threading.active_count()
print("default number of threads present in python program=",noth)