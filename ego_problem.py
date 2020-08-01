name=input("What is your name? ")
egoinput=input("How big is your ego? ")
ego=egoinput.lower()
f= open("your_ego.txt", 'w+')
x="User's name: "+name+"\n" 
x=x+"User's ego: "+egoinput+"\n"
x=x+"*******************"+"\n"
if ego == "small":
	x=x+"1 "+name+"\n"
elif ego == "medium":
	for y in range(1,11):
		x=x+str(y)+" "+name+"\n"
elif ego == "large":
	for y in range(1,101):
		x=x+str(y)+" "+name+"\n"
else: 
	x=x+"User has no ego" 
print(x,file=f)	
print(x)
f.close