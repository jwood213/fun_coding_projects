#ego problem
import random

#start input
name=input("What is your name? ")
print("How big is your ego?")
egoinput=input("(Small, Medium, Large) ")
#end input

allTitles = ["Mr.", "Mrs.", "Dr.", "Lord", "Sir"]
titleIndex = int(random.choice("01234"))
titleToUse = allTitles[titleIndex]

#start output
#header
ego=egoinput.lower()
if ego == "s":
	ego = "small"
elif ego == "m":
	ego = "medium"
elif ego == "l":
	ego = "large"

f= open("your_ego.txt", 'w+')
x="Current cup of coffee: "+str(random.choice("2345"))+"\n"
x=x+"User's name: "+titleToUse+" "+name+"\n"
namereveresed=name[::-1]
x=x+"User's name reversed: "+namereveresed+"\n"
x=x+"User's ego: "+ego+"\n"
#end header
#separator
namelength = len(name)
titleLength = len(titleToUse)
separator = "***"+titleLength*"*"+namelength*"*"+"*"+namelength*"*"
x=x+separator+"\n"
#body
nameline = titleToUse+" "+name+" "+namereveresed+"\n"
if ego == "small":
	x=x+"1 "+nameline
elif ego == "medium":
	for y in range(1,11):
		x=x+str(y)+" "+nameline
elif ego == "large":
	for y in range(1,101):
		x=x+str(y)+" "+nameline
else: 
	x=x+"User has no ego" 

#print to file
print(x,file=f)	

#print to screen
print("\n\n"+x)
f.close