""" Automaton is a game with a list of unfinished statements. If you want to want know more you lose. Psuedocode"""
from statements_lose_version import statements_lose_version


 #question started on




def welcome_statement(lets_play):
	"""Asks user if they want to play the game"""
	welcome_answer = raw_input ("Welcome to Automaton. Would you like to play a game about curiosity and information? Y/N ")
	if welcome_answer.upper() == "Y" :
		print "OK let's play!"
		lets_play = True
	elif welcome_answer.upper() == "N":
		print "Ok bye"
		lets_play = False
		leave_game()
	else:
		lets_play = 2
		# call function that is a loop so if it is 2, it asks a question again
		repeat_question(lets_play)
	return lets_play
	
	

def leave_game():
	exit()

def repeat_question(lets_play):
	print "Please input Y or N"
	welcome_statement(lets_play)


def leading_statement(statements,question_num,score):
	"""Asks question and fields response"""
	answer = raw_input (statements[question_num]["question"]["synopsis"]) # is a string
	options = statements[question_num]["question"]["options"] # options is a list with a dictionary in it
	lose_message = statements[question_num]["question"]["lose_message"] # is a string
	for tupletest in options:
		if answer in tupletest[1]:
			return tupletest[0] #debugging
			#checks to see if in possible answers.
			
	
		
	
def checks_move_next_question(statements, question_num, answer1, score):
	if answer1 == "YES":
				print statements[question_num]["question"]["lose_message"]
				print "Your final score was %d" %score
				leave_game()
	elif answer1 == "NO":
				score += 1 #adds score when not losing
				question_num += 1 # goes to next question

	else: 
		print "try another answer"

	return (score, question_num)
	


def main():
	"""
	this the your driver 
	"""
	statements = statements_lose_version
	total_questions = len(statements_lose_version)
	score= 0
	lets_play = None
	question_num = 0
	play = welcome_statement(lets_play)
	while play == True:
		
		answer1 = leading_statement(statements,question_num,score)
		#print answer1
		score, question_num = checks_move_next_question(statements, question_num, answer1, score)
	
	
 
 #runs the main function
if __name__=='__main__':
	main()
