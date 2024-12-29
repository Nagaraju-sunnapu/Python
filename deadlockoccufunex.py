# program for demonstrating the dead lock concept by using the function
import threading,time
def MulTable(n):
	if(n<=0):
		print("{}-->{} invalid input".format(threading.current_thread().name,n))
	else:
		print("-"*50)
		print("{}-->mul table for:{}".format(threading.current_thread().name,n))
		print("-"*50)
		for i in range(1,11):
			print("{}-->{}x{}={}".format(threading.current_thread().name,n,i,n*i))
			time.sleep(1)
		print("-"*50)
# main program 
t1=threading.Thread(target=MulTable,args=(16,))
t2=threading.Thread(target=MulTable,args=(9,))
t3=threading.Thread(target=MulTable,args=(18,))
t4=threading.Thread(target=MulTable,args=(-10,))
# dispatch the sub threads
t1.start()
t2.start()
t3.start()
t4.start()