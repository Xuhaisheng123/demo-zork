from sys import exit
list = []
def forest():
	print "Welcome to dark forest!\n There is two path way ahead which way you want go?"
	while True:
		next = raw_input(">")
		if "1" in next :
			print "You are near to the canve you want explore it ?"
			next1 = raw_input(">")
			if "yes" or "y" in next1:
				bear_room()
		elif "2" in next :
			print "You are under the way to the most dangerous jounney in the wrold\n You still want go? "
			next2 = raw_input(">")
		else:
			print "You need to input the right path,such as 1 or 2."
			
def bear_room():
	print "You are step into a bear's cave now!"
	print "There are some honey in the right conner and a sward near to the door"
	print "You can take the honey or you can pick up the sward"
	next = raw_input(">")
	if next == "honey":
		dead("The bear pissed off ,you are a dead man now!")
	elif next == "sward":
		pick_up(next)
		print "You pick up the sward now !"
		print "You have three options:"
		print """
		   1.Challenge the bear!
		   2.Take the honey
		   3.Run away
		"""
		next1 =raw_input("Input 1 or 2 or 3 >")
		if "1" in next1:
			print "Congratulations!You kill the bear and the honey is yours."
			pick_up("honey")
			print "All the things you have now:%s"%list
		elif "2" in next1:
			dead("The bear kills you.")
		else :
			print "You are safe now!"
			print "All the things you have now:%s"%list
			print "You want drop the sward or not?"
			input = raw_input(">")
			if input == "yes" or "y":
				drop("sward")
				print list

def dead(why):
		print why,"byebye!"
		
		input = raw_input("Do you want start again?>")
		if "y" or "yes" in input:
			forest()
		else:
			exit(0)	

def pick_up(stuff):
	flag = True
	if stuff in list:
		#if list[i]==stuff:
		flag = False
		
	if flag == True:
		list.append(stuff)
		
def drop(stuff):
	flag = False
	if stuff in list:
		#if list[i]==stuff:
		flag = True
		
	if flag == True:
		list.remove(stuff)
forest()
