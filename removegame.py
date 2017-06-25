"""In this game there is a hidden history of sad things. The goal is to find all hidden items and remove them. 
Eventually you will also add to the list nice things. On the other side of the cube the game exists with the lists switchedso you add bad things and remove good ones"""
#data
from apikeys import KEY
#from addgame import sad_history_hidden_list
import json
import ast
import requests
from pprint import pprint


def test_API():
	"""tests the API for debugging"""
# url = "http://words.bighugelabs.com/api/2/9c9544b6b2ed603d85b76727c53008d2/flower/json"
# response = requests.get(url)
# if response.status_code != requests.codes.ok:
# 	print "nope"
# else:
#  	dict = response.json()
#  	#print dict["verb"]
#  	print dict["verb"]
# 	print "yes"
pass


#pprint(dict.get("noun")) #debug



	

def synonym_pop(sad_history_hidden_list, synonyms, what_user_wants_to_find, game_in_play):
	pass

def find_item_in_list(what_user_wants_to_find, sad_history_hidden_list):
	try_again = False	
	if what_user_wants_to_find in sad_history_hidden_list:
		index = sad_history_hidden_list.index(what_user_wants_to_find)
		sad_history_hidden_list.pop(index)
		print what_user_wants_to_find.upper() + " has been removed from history"
		#print sad_history_hidden_list
		try_again = True	
	else:
		#pulls dictionary of synonyms
		search_word_url = "http://words.bighugelabs.com/api/2/9c9544b6b2ed603d85b76727c53008d2//json"
		index = search_word_url.find ("/json")
		url = search_word_url[:index] + what_user_wants_to_find + search_word_url[index:]
		response_for_word = requests.get(url)
		if response_for_word.status_code != requests.codes.ok:
			print "I do not recognize that as a word. Try again?"
			try_again = None
		else:
			dict = ast.literal_eval(response_for_word.content)
			nouns = (dict.get('noun'))
			#pprint(nouns.get("syn"))#debug prints 
			synonyms = (nouns.get("syn"))
			#print synonyms
			for item in synonyms:
				if item in sad_history_hidden_list:
					index = sad_history_hidden_list.index(item)
					sad_history_hidden_list.pop(index)
					print "Close enough! " + item.upper() + " has been removed from history"
					print "%d items are left in history that need to be removed" %len(sad_history_hidden_list)
					try_again = True
						#print item #debugging only
	if try_again == False:
		print "That item is not in this history. Try again?"
	
		

def main(sad_history_hidden_list):
	"""Driver"""
sad_history_hidden_list =["bombs", "sadness", 'war', "trauma", "rape", "fear", "racism", "korean war", "apartied", "flower"]#this will eventually be online

game_in_play = True
synonyms = [""]
if game_in_play:
	while game_in_play:
		if len(sad_history_hidden_list) > 0:
			what_user_wants_to_find = raw_input("What would you like to find and remove from history? ")
			what_user_wants_to_find = what_user_wants_to_find.lower()
		if what_user_wants_to_find == "q":
			exit()
		else: 
			find_item_in_list(what_user_wants_to_find, sad_history_hidden_list)
	if len(sad_history_hidden_list) == 0:
		print "You win."
		exit()


 #runs the main function
if __name__=='__main__':
	main()








	
	


	



	