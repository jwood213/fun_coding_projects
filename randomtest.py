import random

dict = {
  "two": 0,
  "three": 0,
  "four": 0,
  "five": 0,
  "unknown": 0
}

for y in range(10000):
	x=int(random.choice("2345"))
	if x == 2:
		dict["two"] = dict["two"] + 1
	elif x == 3:
		dict["three"] = dict["three"] + 1
	elif x == 4:
		dict["four"] = dict["four"] + 1
	elif x == 5:
		dict["five"] = dict["five"] + 1
	else:
		dict["unknown"] = dict["unknown"] + 1
		
print(dict)