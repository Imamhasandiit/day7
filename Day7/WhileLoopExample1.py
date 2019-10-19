""" SYNTAX:

init variable
while condition:
   statements """
'''
i=1
while i <=5 :

	print (i, end='\t')
	#i=i+1
	i+=1

x=int(input("Enter start value : "))
y=int(input("Enter end value : "))
i=x
while i<=y: 
	print (i, end='\t')
	#i=i+1
	i+=1 
	
'''

#while message !='quit':
#	message = input("enter:")
#	print(message)
#Break
'''message = ""
while True:
	message=input("enter:")
	if message =='x':
		break
	print(message)'''
######### using boolean
'''message = ""
act=True
while act:
	message=input("enter:")
	if message =='close':
		act=False
	else:
		print(message)'''
#### Continue statement example
'''n=0
while n<10:
	n+=1
	if n%2 ==0:
		continue
		
	print(n)'''
#Fibonakki series
'''a=0
b=1
while b<50:
	print(b, end="")
	a=b
	b=a+b'''
##
a,b = 0,1
while b<50:
	print(b, end="")
	a,b =b,a+b
	
