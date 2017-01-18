###########################################################
#   File name: main.py
#   Author: David Moyal / Shlomo Maghen / Samuel Jefroykin
#   Last updated : 01/18/2017
###########################################################


BOT_NAME = "ADINA"

import os
# import nltk
# from PyDictionary import PyDictionary
# import webcolors

def introduction():
	return "Hello, I am %s. I just had a glass of wine. I am here to help you build a website. Should we start?" % BOT_NAME

# dictionary=PyDictionary('headline','title')

# title_syn = dictionary.getSynonyms()
# title_syn = title_syn[1]['title']+title_syn[0]['headline']


# sentence = 'insert blue title'

# tokens = nltk.word_tokenize(sentence)
# print tokens

# tagged = nltk.pos_tag(tokens)
# entities = nltk.chunk.ne_chunk(tagged)
# print entities

# def find_keyword(tokens):
#     for token in tokens:
#         if token in title_syn:
#             title_function_find_attributes(token,tokens)



# def title_function_find_attributes(token,tokens):
#     color = ''
#     for token in tokens:
#         if token in webcolors.CSS3_NAMES_TO_HEX:
#             color = webcolors.name_to_hex(token)
#     if color == '':
#         ask_color()
#     # find the parameters
#     return 0

def add_title(text=None):
	if text is None:
		text = get_input_from_user("text")
	render_title(text=text)

def add_navbar():
	return 0


def add_image():
	fields = ["url"]
	responses = get_all_fields(fields)
	return 0


def add_text():
	return 0


def add_button():
	return 0


def add_link():
	return 0 


def get_input_from_user(text):
	"""
	get the next message from the user
	"""
	# construct a message
	message = "What is the %s" % text
	# display the message to the user
	display_chat_message(message)
	response = get_response() #implement


def display_chat_message(message):
	# display the message to the user
	return

def get_all_fields(fields):
	responses = {}
	for field in fields:
		response = get_input_from_user(field)
		responses[field] = response
	return responses