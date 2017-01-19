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
navigation_bar_syn = ['navbar','navigation bar']
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


def find_color(sentence):
	tokens = tokenized(sentence)
	color = ''
	for token in tokens:
		if token in webcolors.CSS3_NAMES_TO_HEX:
			color = webcolors.name_to_hex(token)
	return color

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
    tokens = tokenized(sentence)
    for token in tokens:
        print token
        if '.' not in token or len(token) < 3:
            continue
        if "http" not in token:
            token = "http://" + token
        try:
           urllib.urlopen(token)
           return token
        except:
            continue
    return False


def failure():
	return json.dumps({"response": "I am sorry, I did not understand, it might be the wine..."})


def add_video(json_obj):
	fields = ["link"]
	
	sentence = json_obj["user_input"]
	url = has_url(sentence)
	
	if url:
		json_obj["link"] = url
		json_obj["response"] = "Done. I added your video!"
		json_obj["done"] = "true"
		return json.dumps(json_obj)
	
	for field in fields:
		if field not in json_obj:
			json_obj["needs"] = field
			json_obj["function"] = "add_video"
			json_obj["response"] = "What is the link to your video?"
			return json.dumps(json_obj)
		elif "link" in json_obj:
			if not url:
				json_obj["response"] = "That was not a valid link. Try again."
				return json.dumps(json_obj)
			else:
				json_obj["link"] = url
		else:
			del json_obj["needs"]
			del json_obj["function"]
			json_obj["response"] = "Done. I added your video!"
			json_obj["done"] = "true"
			return json.dumps(json_obj)


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
