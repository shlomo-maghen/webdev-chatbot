import os
import nltk
from PyDictionary import PyDictionary
import webcolors
import json

BOT_NAME = "ADINA"
###########################################################
#   File name: main.py
#   Author: David Moyal / Shlomo Maghen / Samuel Jefroykin
#   Last updated : 01/18/2017
###########################################################
dictionary = PyDictionary('headline', 'title', 'image', 'picture', 'paragraph', 'text', 'url-link', 'link', 'access', 'redirection', 'button', 'box', 'video', 'map', 'footer')

synonyms = dictionary.getSynonyms()
title_syn = synonyms[1]['title'] + synonyms[0]['headline'] + ['headline', 'title', 'name']
image_syn = synonyms[2]['image'] + synonyms[3]['picture'] + ['image', 'picture']
paragraph_syn = synonyms[4]['paragraph'] + synonyms[5]['text'] + ['paragraph', 'text']
link_syn = synonyms[6]['url-link'] + synonyms[7]['link'] + synonyms[8]['access'] + synonyms[9]['redirection'] + ['link', 'url link' , 'access', 'redirection']
button_syn = synonyms[10]['button'] + ['button']
navigation_bar_syn = ['navbar','navigation bar']
video_syn = synonyms[12]['video'] + ['video']
map_syn = synonyms[13]['map'] + ['map']
footer_syn = synonyms[14]['footer'] + ['footer']

def introduction():
	return """Hello, I am %s. I just had a glass of wine. 
				I am here to help you build a website. 
				Should we start?" % BOT_NAME"""

def tokenized(sentence):
	tokens = nltk.word_tokenize(sentence.lower())
	return tokens


def entities_tokens(tokens):
	tagged = nltk.pos_tag(tokens)
	entities = nltk.chunk.ne_chunk(tagged)
	return entities


def get_element(json_obj):
	if "function" in json_obj:
		return globals()[json_obj["function"]](json_obj)
	sentence = json_obj["chat_text"]
	tokens = tokenized(sentence.lower())
	
	for token in tokens:
		if token in title_syn:
			return add_title(json_obj)
		elif token in image_syn:
			return add_image(json_obj)
		elif token in paragraph_syn:
			return add_paragraph(json_obj)
		elif token in link_syn:
			return add_link(json_obj)
		elif token in button_syn:
			return add_button(json_obj)
		elif token in navigation_bar_syn :
			return add_navbar(json_obj)
		elif token in video_syn:
			return add_video(json_obj)
		elif token in map_syn:
			return add_map(json_obj)
		elif token in footer_syn:
			return add_footer(json_obj)
	print "failure"
	return failure()


def color_find_attributes(token,tokens):
	color = ''
	for token in tokens:
		if token in webcolors.CSS3_NAMES_TO_HEX:
			color = webcolors.name_to_hex(token)
	if color == '':
		ask_color()
	# find the parameters
	return 0

def failure():
	return json.dumps({"response": "I am sorry, I did not understand, it might be the wine..."})


def add_video(json_obj):
	# the required fields for a video
	fields = ["link"]
	for field in fields:
		if field not in json_obj:
			json_obj["needs"] = field
			json_obj["function"] = "add_video"
			json_obj["response"] = "What is the link to your video?"
			return json.dumps(json_obj)
		else:
			del json_obj["needs"]
			del json_obj["function"]
			json_obj["response"] = "Done. I added your video!"
			json_obj["done"] = "true"
			return json.dumps(json_obj)


def add_map(json_obj):
	# the required fields for a video
	fields = ["location"]
	for field in fields:
		if field not in json_obj:
			json_obj["needs"] = field
			json_obj["function"] = "add_map"
			json_obj["response"] = "Give me the location you want to display (address)?"
			return json.dumps(json_obj)
		else:
			del json_obj["needs"]
			del json_obj["function"]
			json_obj["response"] = "Got it! Your map is ready ;)"
			json_obj["done"] = "true"
			return json.dumps(json_obj)


def add_footer(json_obj):
	# the required fields for a footer
	fields = ["color"]
	for field in fields:
		if field not in json_obj:
			json_obj["needs"] = field
			json_obj["function"] = "add_footer"
			json_obj["response"] = "What color would you like for the footer?"
			return json.dumps(json_obj)
		else:
			del json_obj["needs"]
			del json_obj["function"]
			json_obj["response"] = "Footer it is..."
			json_obj["done"] = "true"
			return json.dumps(json_obj)


def add_title(json_obj):
	# the required fields for a title
	fields = ["title"]
	for field in fields:
		if field not in json_obj:
			json_obj["needs"] = field
			json_obj["function"] = "add_title"
			json_obj["response"] = "What title would you like?"
			return json.dumps(json_obj)
		else:
			del json_obj["needs"]
			del json_obj["function"]
			json_obj["response"] = "What a good title!"
			json_obj["done"] = "true"
			return json.dumps(json_obj)


def add_navbar(json_obj):
	# the required fields for a navbar
	fields = ["color"]
	for field in fields:
		if field not in json_obj:
			json_obj["needs"] = field
			json_obj["function"] = "add_navbar"
			json_obj["response"] = "What color do you want for the navbar?"
			return json.dumps(json_obj)
		else:
			del json_obj["needs"]
			del json_obj["function"]
			json_obj["response"] = "You've got a nice navigation bar now!"
			json_obj["done"] = "true"
			return json.dumps(json_obj)


def add_image(json_obj):
	# the required fields for an image
	fields = ["link"]
	for field in fields:
		if field not in json_obj:
			json_obj["needs"] = field
			json_obj["function"] = "add_image"
			json_obj["response"] = "What is the link to your image?"
			return json.dumps(json_obj)
		else:
			del json_obj["needs"]
			del json_obj["function"]
			json_obj["response"] = "Your website is now more vivid ;)"
			json_obj["done"] = "true"
			return json.dumps(json_obj)


def add_paragraph(json_obj):
	# the required fields for a paragraph
	fields = ["text"]
	for field in fields:
		if field not in json_obj:
			json_obj["needs"] = field
			json_obj["function"] = "add_paragraph"
			json_obj["response"] = "What is the text for your paragraph?"
			return json.dumps(json_obj)
		else:
			del json_obj["needs"]
			del json_obj["function"]
			json_obj["response"] = "Yeah, it's better than Lorem Ipsum. Paragraph added."
			json_obj["done"] = "true"
			return json.dumps(json_obj)


def add_button(json_obj):
	# the required fields for a button
	fields = ["text"]
	for field in fields:
		if field not in json_obj:
			json_obj["needs"] = field
			json_obj["function"] = "add_button"
			json_obj["response"] = "What is the text for the button?"
			return json.dumps(json_obj)
		else:
			del json_obj["needs"]
			del json_obj["function"]
			json_obj["response"] = "Damn, I want to click on that button!"
			json_obj["done"] = "true"
			return json.dumps(json_obj)


def add_link(json_obj):
	# the required fields for a link
	fields = ["link"]
	for field in fields:
		if field not in json_obj:
			json_obj["needs"] = field
			json_obj["function"] = "add_link"
			json_obj["response"] = "What is the link you want to add?"
			return json.dumps(json_obj)
		else:
			del json_obj["needs"]
			del json_obj["function"]
			json_obj["response"] = "Link linked! Kuddoz"
			json_obj["done"] = "true"
			return json.dumps(json_obj)


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


def render(type, data):
	if type == 'title':
		return
	elif type == 'button':
		return
	elif type == 'footer':
		return
	elif type == 'map':
		return
	elif type == 'image':
		return
	elif type == 'link':
		return
	elif type == 'navbar':
		return
	elif type == 'paragraph':
		return
	elif type == 'text_bar':
		return
	elif type == 'video':
		return
	else:
		failure()


def get_all_fields(fields):
	responses = {}
	for field in fields:
		response = get_input_from_user(field)
		responses[field] = response
	return responses
