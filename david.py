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

dictionary=PyDictionary('headline','title','image','picture','paragraph','text','url-link','link','access','redirection','button','box','video','map','footer')

synonyms = dictionary.getSynonyms()
title_syn = synonyms[1]['title'] + synonyms[0]['headline'] + ['headline','title']
image_syn = synonyms[2]['image'] + synonyms[3]['picture'] + ['image','picture']
paragraph_syn = synonyms[4]['paragraph'] + synonyms[5]['text'] + ['paragraph','text']
link_syn = synonyms[6]['url-link'] + synonyms[7]['link'] + synonyms[8]['access'] + synonyms[9]['redirection'] + ['link','url link','access','redirection']
button_syn = synonyms[10]['button'] + ['button']
text_bar_syn = synonyms[11]['box'] + ['textbox']
navigation_bar_syn = ['navbar','navigation bar']
video_syn = synonyms[12]['video'] + ['video']
map_syn = synonyms[13]['map'] + ['map']
footer_syn = synonyms[14]['footer'] + ['footer']

def tokenized(sentence):
	tokens = nltk.word_tokenize(sentence.lower())
	return tokens

def entities_tokens(tokens):
	tagged = nltk.pos_tag(tokens)
	entities = nltk.chunk.ne_chunk(tagged)
	return entities

def categorized(sentence):
    tokens = tokenized(sentence.lower())
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
			category = 'navbar'
        elif token in video_syn:
            category = 'video'
        elif token in map_syn:
            category = 'map'
        elif token in footer_syn:
            category = 'footer'
    return category

def call_function(category):
    if category == 'title':
        add_title()
    elif category == 'button':
        add_button()
    elif category == 'footer':
        add_footer()
    elif category == 'map':
        add_map()
    elif category == 'image':
        add_image()
    elif category == 'link':
        add_link()
    elif category == 'navbar':
        add_navbar()
    elif category == 'paragraph':
        add_paragraph()
    elif category == 'text_bar':
        add_text_bar()
    elif category == 'video':
        add_video()
    else:
        failure()

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
    print 'Error'
    
def add_text_bar():
    return 0

def add_map():
    return 0

def add_footer():
    return 0

def add_video():
    return 0


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


def add_paragraph():
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
