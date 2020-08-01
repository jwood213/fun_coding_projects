name=input("What is your name? ")
ego=input("How big is your ego? ")

if ego == "small":
	print(name)
elif ego == "medium":
	print(name * 10)
elif ego == "large":
	print(name * 100)
else: 
	print("User has no ego")
with open('your_ego.txt', 'a+') as f:
	f.write('your ego')