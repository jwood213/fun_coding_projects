name=input("What is your name? ")
ego=input("How big is your ego? ")
f= open("your_ego.txt", 'w+')
x="User's name: "+name+"\n" 
x=x+"User's ego: "+ego+"\n"
x=x+"*******************"+"\n"
if ego == "small":
	x=x+name+"\n"
elif ego == "medium":
	for y in range(1,11):
		x=x+str(y)+" "+name+"\n"
elif ego == "large":
	x=x+name * 100
else: 
	x=x+"User has no ego" 
print(x,file=f)	
print(x)
f.close