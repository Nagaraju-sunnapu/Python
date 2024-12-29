# program for demonstrating the dead lock concept by using the oops
import threading,time
class multable:
	def table(self,n):
		#step--2 get the lock
		L.acquire()
		if(n<=0):
			print("{}-->{} invalid input".format(threading.current_thread().name,n))
		else:
			print("-"*50)
			print("{}--> mul table for:{}".format(threading.current_thread().name,n))
			print("-"*50)
			for i in range(1,11):
				print("{}-->{}x{}={}".format(threading.current_thread().name,n,i,n*i))
				time.sleep(0.25)
			print("-"*50)
		L.release()
# main program 
# step-1--creat a lock object 
L=threading.Lock()
# creat a sub-thread
t1=threading.Thread(target=multable().table,args=(18,))
t2=threading.Thread(target=multable().table,args=(-34,))
t3=threading.Thread(target=multable().table,args=(-21,))
t4=threading.Thread(target=multable().table,args=(16,))
# dispatch the sub threads
t1.start()
t2.start()
t3.start()
t4.start()