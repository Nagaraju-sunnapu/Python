# program for demonstrating the dead lock concept by using the function
import threading,time
class multable:
	def table(self,n):
		if(n<=0):
			print("{}-->{} invalid input".format(threading.current_thread().name,n))
		else:
			print("-"*50)
			print("{}-->{} invalid input".format(threading.current_thread().name,n))
			print("-"*50)
			for i in range(1,11):
				print("{}-->{}x{}={}".format(threading.current_thread().name,n,i,n*i))
				time.sleep(1)
			print("-"*50)
# main program 
t1=threading.Thread(target=multable().table,args=(19,))
t2=threading.Thread(target=multable().table,args=(23,))
t3=threading.Thread(target=multable().table,args=(-8,))
t4=threading.Thread(target=multable().table,args=(34,))
#dispatch the sub threads
t1.start()
t2.start()
t3.start()
t4.start()
