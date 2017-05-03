# -*- coding: utf-8 -*-
import nltk

file_object  = open('testfile.txt', 'r')
output_object  = open('output.txt', 'w')

def word_to_output(pair): #format word/tag-pair and write it to output
	if pair[1] in ["NN", "NNS", "NNP", "NNPS", "PRP", "PRP$", "WP", "WP$"]:
		tag="NOUN"
	elif pair[1] in ["JJ", "JJR", "JJS"]:
		tag="ADJ"
	elif pair[1] in ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]:
		tag="VERB"
	elif pair[1] in ["RB", "RBR", "RBS"]:
		tag="ADVERB"
	else: tag = pair[1]
	output_object.write(pair[0] + "(" + tag + ") ")
	if pair[0] == ".":
		output_object.write("\n")
	

for line in file_object:
	line = nltk.word_tokenize(line)
	line = nltk.pos_tag(line)
	ner = nltk.ne_chunk(line, binary=False)
	for subtree in ner: 
		if type(subtree) is nltk.Tree: #named entity
			output_object.write("[NER] ")
			for pair in subtree:
				word_to_output(pair)
			output_object.write("[" + subtree.label() + "] ")
		else: #not a named entity
			word_to_output(subtree)	
			



