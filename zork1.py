from sys import exit

def forest():
	print "Welcome to dark forest!\n There is two path way ahead which way you want go?"
	next = raw_input(">")
	if "0" in next :
		print "You are near to the canve you want explore it ?"
	if "1" in next :
		print "You are under the way to the most dangerous jounney in the wrold\n You still want go? "
	
forest()