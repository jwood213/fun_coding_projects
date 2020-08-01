name=input("What is your name? ")
ego=input("How big is your ego? ")
f= open("your_ego.txt", 'w+')
x="default"
if ego == "small":
	x=name
elif ego == "medium":
	x= name * 10
elif ego == "large":
	x= name * 100
else: 
	x= "User has no ego" 
print(x,file=f)	
print(x)
f.close