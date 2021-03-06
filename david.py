import os
import re
import nltk
from PyDictionary import PyDictionary
import webcolors
import json
import urllib

BOT_NAME = "ADINA"
###########################################################
#   File name: main.py
#   Author: David Moyal / Shlomo Maghen / Samuel Jefroykin
#   Last updated : 01/18/2017
###########################################################
dictionary = PyDictionary('headline', 'title', 'image', 'picture', 'paragraph', 'text', 'url-link', 'link', 'access', 'redirection', 'button', 'box', 'video', 'map', 'footer','big','small','medium')

synonyms = dictionary.getSynonyms()
title_syn = synonyms[1]['title'] + synonyms[0]['headline'] + ['headline', 'title', 'name', 'haedline', 'tilte', 'tile']
image_syn = synonyms[2]['image'] + synonyms[3]['picture'] + ['image', 'picture' , 'img','pic','imge']
paragraph_syn = synonyms[4]['paragraph'] + synonyms[5]['text'] + ['paragraph', 'text' , 'txt' , 'par', 'texte']
link_syn = synonyms[6]['url-link'] + synonyms[7]['link'] + synonyms[8]['access'] + synonyms[9]['redirection'] + ['link', 'url link' , 'access', 'redirection' , 'lnk']
button_syn = synonyms[10]['button'] + ['button' , 'buton','buttn']
navigation_bar_syn = ['navbar', 'navigation bar', 'nav bar']
video_syn = synonyms[12]['video'] + ['video', 'vidoe']
map_syn = synonyms[13]['map'] + ['map', 'mp','amp']
footer_syn = synonyms[14]['footer'] + ['footer','footre']
big_syn = synonyms[15]['big'] + ['big','bg','large']
small_syn = synonyms[16]['small'] + ['small','smll','smal']
med_syn = synonyms[17]['medium'] + ['med','medium']



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
	sentence = json_obj["user_input"]
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
	return failure()


def has_color(sentence):
	tokens = tokenized(sentence)
	for token in tokens:
		if token in webcolors.CSS3_NAMES_TO_HEX:
			return webcolors.name_to_hex(token)
	return False

def find_size(sentence):
    tokens = tokenized(sentence)
    size = ''
    for token in tokens:
        if token in small_syn:
            size = 'small'
        if token in med_syn:
            size = 'medium'
        if token in big_syn:
            size = 'large'
    return size


def has_url(sentence):
    tokens = sentence.split()
    for token in tokens:

        if '.' not in token or len(token) < 3:
            continue
        if "http" not in token:
            token = "http://" + token
        try:
           urllib.urlopen(token)
           if 'youtube' in token:
           		token = token.replace("watch?v=", 'embed/')	
           return token
        except:
            continue
    return False


def failure():
	return json.dumps({"response": "I am sorry, I did not understand, it might be the wine..."})


def add_video(json_obj):
	# required fields
	fields = ["src"]
	
	sentence = json_obj["user_input"]
	url = has_url(sentence)
	
	json_obj["type"] = "video"
	json_obj["tag"] = "iframe"
	json_obj["function"] = "add_video"

	if url:
		json_obj["src"] = url
		json_obj["response"] = "Done. I added your video!"
		json_obj["done"] = "true"
		return json.dumps(json_obj)
	
	for field in fields:
		if field not in json_obj:
			json_obj["needs"] = field
			json_obj["response"] = "What is the link to your video?"
			return json.dumps(json_obj)
		elif "src" in json_obj:
			if not url:
				json_obj["response"] = "That was not a valid link. Try again."
				return json.dumps(json_obj)
			else:
				json_obj["src"] = url
		else:
			new_object = {"done": "true", "tag": "iframe", "type": "video",
				"src": json_obj["link"], "response": "Done. I added your video!"}
			# del json_obj["needs"]
			# del json_obj["function"]
			# json_obj["response"] = "Done. I added your video!"
			# json_obj["done"] = "true"
			return json.dumps(new_object)


def add_map(json_obj):
	# the required fields for a map
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
			new_object = {"type":"title", "tag": "h1", "innerHTML":json_obj["user_input"],
				"done": "true", "response": "Great Title!!"}
			return json.dumps(new_object)

def add_navbar(json_obj):
	# the required fields for a navbar

	fields = ["color"]
	color = has_color(json_obj["user_input"])
	if color:
		new_object = {"type":"navbar", "tag": "ul", "color": color,
					"done": "true", "response": "You've got a nice navigation bar now!"}
		return json.dumps(new_object)

	for field in fields:
		if field not in json_obj:
			json_obj["needs"] = field
			json_obj["function"] = "add_navbar"
			json_obj["response"] = "What color do you want for the navbar?"
			return json.dumps(json_obj)
		elif "color" in json_obj:
			color = has_color(json_obj["user_input"])
			if color:
				new_object = {"type":"navbar", "tag": "ul", "color": color,
					"done": "true", "response": "You've got a nice navigation bar now!"}
				return json.dumps(new_object)
			else:
				json_obj["response"] = "I didn't understand that color. Try again."
				return json.dumps(json_obj)


def add_image(json_obj):
	fields = ["src"]
	json_obj["type"] = "image"
	json_obj["tag"] = "img"
	json_obj["function"] = "add_image"
	
	sentence = json_obj["user_input"]
	url = has_url(sentence)
	
	if url:
		json_obj["src"] = url
		json_obj["response"] = "Your photo appears!"
		json_obj["done"] = "true"
		return json.dumps(json_obj)
	
	for field in fields:
		if field not in json_obj:
			json_obj["needs"] = field
			json_obj["response"] = "What is the link to your image?"
			return json.dumps(json_obj)
		elif "src" in json_obj:
			if not url:
				json_obj["response"] = "That was not a valid link. Try again."
				return json.dumps(json_obj)
			else:
				json_obj["src"] = url
		else:
			new_object = {"type":"image", "tag": "img", "src": json_obj["src"],
							"done": "true", "response": "Your website is now more vivid!"}

			return json.dumps(new_object)

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
			new_object = {"tag": "p", "type":"paragraph", "done":"true", 
				"innerHTML": json_obj["user_input"], "response": "Yeah, it's better than Lorem Ipsum. Paragraph added."}
			print new_object
			return json.dumps(new_object)


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
			new_object = {"tag": "BUTTON", "type":"button", "done":"true", 
				"innerHTML": json_obj["user_input"], "response": "Damn, I want to click on that button!"}
			return json.dumps(new_object)


def add_link(json_obj):
		# required fields
	fields = ["href"]
	
	sentence = json_obj["user_input"]
	url = has_url(sentence)
	
	json_obj["type"] = "link"
	json_obj["tag"] = "a"
	json_obj["function"] = "add_link"

	if url:
		json_obj["href"] = url
		json_obj["response"] = "You have created a portal to another site!"
		json_obj["done"] = "true"
		return json.dumps(json_obj)
	
	for field in fields:
		if field not in json_obj:
			json_obj["needs"] = field
			json_obj["response"] = "What is the url for the link?"
			return json.dumps(json_obj)
		elif "src" in json_obj:
			if not url:
				json_obj["response"] = "That was not a valid link. Try again."
				return json.dumps(json_obj)
			else:
				json_obj["href"] = url
		else:
			new_object = {"done": "true", "tag": "a", "type": "link",
				"href": url, "response": "There is now a path to another site on your site. META!"}
			# del json_obj["needs"]
			# del json_obj["function"]
			# json_obj["response"] = "Done. I added your video!"
			# json_obj["done"] = "true"
			return json.dumps(new_object)


	# fields = ["href"]
	# json_obj["type"] = "link"
	# json_obj["tag"] = "a"
	# json_obj["function"] = "add_link"
	
	# sentence = json_obj["user_input"]
	# url = has_url(sentence)
	
	# if url:
	# 	json_obj["href"] = url
	# 	json_obj["response"] = "You have created a portal to another site!"
	# 	json_obj["done"] = "true"
	# 	return json.dumps(json_obj)
	
	# for field in fields:
	# 	if field not in json_obj:
	# 		json_obj["needs"] = field
	# 		json_obj["response"] = "What link would you like to add?"
	# 		return json.dumps(json_obj)
	# 	elif "href" in json_obj:
	# 		if not url:
	# 			json_obj["response"] = "That was not a valid link. Try again."
	# 			return json.dumps(json_obj)
	# 		else:
	# 			json_obj["href"] = url
	# 	# else:
	# 	new_object = {"type":"link", "tag": "a", "href": url,
	# 					"done": "true", "response": "There is now a path to another site on your site. META!"}

	# 	return json.dumps(new_object)


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
