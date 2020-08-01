name=input("What is your name? ")
ego=input("How big is your ego? ")
f= open("your_ego.txt", 'w+')
x="User's name: "+name+"\n" 
x=x+"User's ego: "+ego+"\n"
x=x+"*******************"+"\n"
if ego == "small":
	x=x+name+"\n"
elif ego == "medium":
	x=x+name * 10
elif ego == "large":
	x=x+name * 100
else: 
	x=x+"User has no ego" 
print(x,file=f)	
print(x)
f.close