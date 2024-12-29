# program for showing the internal flow of the mainthread
import threading 
def welcome():
	print("line-4-->welcome() executed by:",threading.current_thread().name)
	
def hello():
	print("line-7-->welcome() executed by:",threading.current_thread().name)
	
def hi():
	print("line-10-->welcome() executed by:",threading.current_thread().name)
	
# main program
print("-"*50)
print("line-14-->program execution started by :",threading.current_thread().name)
print("-"*50)
welcome()
print("line-15")
hello()
print("line-17")
hi()
print("-"*50)
print("line-22-->program execution ended by:",threading.current_thread().name)
print("-"*50)