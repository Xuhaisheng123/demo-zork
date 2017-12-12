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
			else :
				exit(0)
		elif "2" in next :
			print "You are under the way to the most dangerous jounney in the wrold\n You still want go? "
			next2 = raw_input(">")
			if "y" or "yes" in next2:
				tree()
			else :
				exit(0)
			print "You already come down from the tree now,Let's move on "
			print "You walk in to a area of savages,"
			print "is very dangerous,you can run away or you can keep going?"
			next3 = raw_input("'yes' or 'not'>")
			if next3 == "yes" or "y":
				print "Congratulations! You are a brave man ,this is the reward for you courage:"
				print """
				1.a bow and three arrows
				2.10kg goldwhich one you want to take?"""
				next4 = raw_input(">")
				if next4 == "1":
					pick_up("bow and arrows")
				elif next4 =="2":
					pick_up("gold")
				else :
					exit(0)
				print "Do you want go on or not?"
				next = raw_input(">")
				if next == "yes" or "y":
					print "There is a tiger runs to you"
					if "bow and arrows" in list:
						print "You can using the bow to kill the tiger."
						next = raw_input("input 'y' or 'n'>")
						if next == "y":
							print "you kill the tiger the reward is 1000kg gold"
							print "you are win!"
						else :
							dead("The tiger kills you,you are dead.")
					else :
						dead("You have nothing to fight the tiger you are dead.")
				else :
					exit(0)
			if next3 == "no" or "not" or "n":
				exit(0)
				
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
		elif "3" in next1:
			print "You are safe now!"
			print "All the things you have now:%s"%list
			print "You want drop the sward or not?"
			input = raw_input(">")
			if input == "yes" or "y":
				drop("sward")
				print list
		else:
			exit(0)
	else:
		exit(0)
def dead(why):
		print why,"byebye!"
		
		input = raw_input("Do you want start again?>")
		if "y" or "yes" in input:
			forest()
		else:
			exit(0)	

def pick_up(stuff):
	print "The %s is yours now!"%stuff
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
def tree():
	print "There is a ganit tree  beside the road.\nDo you want climbing it?"
	next0 = raw_input(">")
	if "yes" or "y" or "climbing" in next0:	
		print "You are 30 meters from the ground now!"
		print "There are some eggs in the nest,you want take it?"
		next1 = raw_input(">")
		if "yes" or "y" or "taken" in next1:
			pick_up("eggs")
			print "That's what you have now:%s"%list
forest()
