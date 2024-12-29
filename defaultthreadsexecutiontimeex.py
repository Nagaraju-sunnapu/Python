# program for demonstrating the internal flow of main thread only with execution time
import threading,time
def squares(lst):
	for val in lst:
		print("{}-->square({})={}".format(threading.current_thread().name,val,val**2))
		time.sleep(1)
		
def cubes(lst):
	for val in lst:
		print("{}-->cubes({})={}".format(threading.current_thread().name,val,val**3))
		time.sleep(1)
		
# main program 
bt=time.time()
print("-"*50)
print("program execution started by:",threading.current_thread().name)
print("-"*50)
lst=[10,5,9,2,11]
squares(lst)
print("-----------------------------------------------------------------------------")
cubes(lst)
print("-----------------------------------------------------------------------------")
print("program execution ended by:",threading.current_thread().name)
print("-----------------------------------------------------------------------------")
et=time.time()
print("execution of the program with only main thread without subthreads=",(et-bt))
		
