###########################################################
#   File name: main.py
#   Author: David Moyal / Shlomo Maghen / Samuel Jefroykin
#   Last updated : 01/18/2017
###########################################################


BOT_NAME = "ADINA"

import os
import nltk
from PyDictionary import PyDictionary
import webcolors

def introduction():
	return "Hello, I am %s. I just had a glass of wine. I am here to help you build a website. Should we start?" % BOT_NAME

dictionary=PyDictionary('headline','title','image','picture','paragraph','text','url-link','link','access','redirection','button','box')

synonyms = dictionary.getSynonyms()
title_syn = synonyms[1]['title']+synonyms[0]['headline'] + ['headline','title']
image_syn = synonyms[2]['image']+synonyms[3]['picture'] + ['image','picture']
paragraph_syn = synonyms[4]['image']+synonyms[5]['picture'] + ['paragraph','text']
link_syn = synonyms[6]['url-link']+synonyms[7]['link']+synonyms[8]['access']+synonyms[9]['redirection']+ ['link','url link','access','redirection']
button_syn = synonyms[10]['button'] + ['button']
text_bar_syn = synonyms[11]['box']+ ['Textbox']
navigation_bar_syn = ['navbar','navigation bar']

def tokenized(sentence):
	tokens = nltk.word_tokenize(sentence)
	return tokens

def entities_tokens(tokens):
	tagged = nltk.pos_tag(tokens)
	entities = nltk.chunk.ne_chunk(tagged)
	return entities

def categorized(sentence):
    tokens = tokenized(sentence)
    category = ''
    for token in tokens:
        if token in title_syn:
            category = 'title'
        elif token in image_syn:
			category = 'image'
        elif token in paragraph_syn :
            category = 'paragraph'
        elif token in link_syn :
            category = 'link'
        elif token in button_syn :
			category = 'button'
        elif token in text_bar_syn :
			category = 'text_bar'
        elif token in navigation_bar_syn :
			category = 'navigation_bar'
    return category

def color_find_attributes(token,tokens):
    color = ''
    for token in tokens:
        if token in webcolors.CSS3_NAMES_TO_HEX:
            color = webcolors.name_to_hex(token)
    if color == '':
        ask_color()
    # find the parameters
    return 0

def add_title(text=None):
	if text is None:
		text = get_input_from_user("text")
	render_title(text=text)

def add_navbar():
	return 0


def add_image():
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

def display_chat_message(message):
	# display the message to the user
	return