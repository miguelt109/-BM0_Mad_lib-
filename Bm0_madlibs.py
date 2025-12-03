import random
import time

print("put a random action")
verb=input()

print("put random adjective")
adjective=input()

print("put a random noun")
noun=input()

random_interger = random.randint(1,2)

if random_interger == 1:
	print(f"I went to store eating a {verb}")
	time.sleep(1)
	print(f"The store I went to was so {adjective} I almost pasted out.")
	time.sleep(1)
	print(f"Afterwards I went {noun} and feel asleep")

if random_interger == 2:

	print(f"i asked {noun} if they could {verb} so i can pass my class")
	time.sleep(1)
	print(f"{noun} said just ask mr O for help with {verb} its his class")
	time.sleep(1)
	print(f"i said mr is so {adjective} he wont help anyone with anything")
	time.sleep(1)
	print("the end")
	time.sleep(7)
	print("why are you still reading?")
	time.sleep(5)
	print("is this a four?")
	time.sleep(6)
	print("ok bye now")

	#hi