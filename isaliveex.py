# program for finding the sub-thread is under execution or not
import threading,time
def squares(lst):
	for val in lst:
		print("{}-->square({})={}".format(threading.current_thread().name,val,val**2))
		time.sleep(0.50)
# main program 
print("--------------------------------------------")
print("program execution started by:",threading.current_thread().name)
print("---------------------------------------------")
lst=[10,6,20,5,18,14,15]
t1=threading.Thread(target=squares,args=(lst,))
print("execution status before  t1 start()=",t1.is_alive())
print("number of active threads before start()=",threading.active_count())
t1.start()
print("execution status after  t1 start()=",t1.is_alive())
print("number of active threads after start()=",threading.active_count())
