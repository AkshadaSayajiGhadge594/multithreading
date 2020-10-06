import threading

print("--------Demonstration of Multithreading-------");

def fun(number):	
	for i in range(number):
		print(i);

def gun(number):	
	for i in range(number):
		print(i);

if __name__=="__main__":
	number=5
	thread1=threading.Thread(target=fun,args=(number,));
	thread2=threading.Thread(target=gun,args=(number,));

	thread1.start();
	print("")
	thread2.start();
	
	thread1.join();
	thread2.join();
