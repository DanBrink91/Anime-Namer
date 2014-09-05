import re
import random
import json

# Takes a string and returns a list of words
def tokenize(sentence):
	
	# Get rid of extra marks and lowercase the string
	sentence = re.sub(r'[\.\!\:\,\?\n]', "", sentence.lower())
	
	# Replace - or _ with a space
	sentence = re.sub(r'[\_\-]', " ", sentence)
	
	return [token for token in sentence.split(' ') if token != ""] 

with open("anime.txt", "r") as animes_file:
	tokens = [tokenize(name) for name in animes_file.readlines()]

words = {}
unique = 0
for token_list in tokens:
	# Add so words[token] = [token_after]
	for i in range(len(token_list) - 1):
		word = token_list[i]
		word_after = token_list[i+1]
		
		if word in words:
			words[word].append(word_after)
		else:
			words[word] = [word_after]
with open("parsed.json", "w") as parsed:
	parsed.write(json.dumps(words, indent=4))

first_words = [token[0] for token in tokens]

min_length = 1
max_length = 6
names_to_produce = 200
for i in range(names_to_produce):
	number_of_tokens = random.randrange(min_length, max_length)
	
	title = [random.choice(first_words)]
	for n in range(number_of_tokens - 1):
		try:
			title.append(random.choice(words[title[len(title)-1]]))
		except KeyError:
			title.append(random.choice(words.keys()))
	print " ".join(title)
