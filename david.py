###########################################################
#   File name: main.py
#   Author: David Moyal / Shlomo Maghen / Samuel Jefroykin
#   Last updated : 01/18/2017
###########################################################

import os
import nltk
from PyDictionary import PyDictionary
import webcolors


BOT_NAME = "ADINA"

dictionary = PyDictionary('headline', 'title', 'image', 'picture', 'paragraph', 'text', 'url-link', 'link', 'access', 'redirection', 'button', 'box', 'video', 'map', 'footer')

synonyms = dictionary.getSynonyms()
title_syn = synonyms[1]['title'] + synonyms[0]['headline'] + ['headline', 'title', 'name']
image_syn = synonyms[2]['image'] + synonyms[3]['picture'] + ['image', 'picture']
paragraph_syn = synonyms[4]['paragraph'] + synonyms[5]['text'] + ['paragraph', 'text']
link_syn = synonyms[6]['url-link'] + synonyms[7]['link'] + synonyms[8]['access'] + synonyms[9]['redirection'] + ['link', 'url link' , 'access', 'redirection']
button_syn = synonyms[10]['button'] + ['button']
text_box_syn = synonyms[11]['box'] + ['textbox']
navigation_bar_syn = ['navbar', 'navigation bar']
video_syn = synonyms[12]['video'] + ['video']
map_syn = synonyms[13]['map'] + ['map']
footer_syn = synonyms[14]['footer'] + ['footer']


def introduction():
	return "Hello, I am %s. I just had a glass of wine. I am here to help you build a website. Should we start?" % BOT_NAME


def tokenized(sentence):
	tokens = nltk.word_tokenize(sentence.lower())
	return tokens


def entities_tokens(tokens):
	tagged = nltk.pos_tag(tokens)
	entities = nltk.chunk.ne_chunk(tagged)
	return entities


def get_element(sentence):
	tokens = tokenized(sentence.lower())
	for token in tokens:
		if token in title_syn:
			add_title(sentence)
		if token in image_syn:
			add_image(sentence)
		if token in paragraph_syn:
			add_paragraph(sentence)
		if token in link_syn :
			add_link(sentence)
		if token in button_syn :
			add_button(sentence)
		if token in text_box_syn:
			add_text_box(sentence)
		if token in navigation_bar_syn :
			add_navbar(sentence)
		if token in video_syn:
			add_video(sentence)
		if token in map_syn:
			add_map(sentence)
		if token in footer_syn:
			add_footer(sentence)
	return failure()  # not found


# def color_find_attributes(token,tokens):
# 	color = ''
# 	for token in tokens:
# 		if token in webcolors.CSS3_NAMES_TO_HEX:
# 			color = webcolors.name_to_hex(token)
# 	if color == '':
# 		ask_color()
# 	# find the parameters
# 	return 0


def failure():
	return 'I am sorry, I did not understand, it might be the wine...'


def add_text_box(sentence):
	return 0


def add_map(sentence):
	return 0


def add_footer(sentence):
	return 0


def add_video(sentence):
	return 0


def add_title(sentence):
	text = get_input_from_user("text")
	render(text=text)


def add_navbar(sentence):
	return 0


def add_image(sentence):
	return 0


def add_paragraph(sentence):
	return 0


def add_button(sentence):
	return 0


def add_link(sentence):
	return 0 


def get_input_from_user(text):
	"""
	get the next message from the user
	"""
	# construct a message
	message = "What is the %s" % text
	# display the message to the user
	display_chat_message(message)

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