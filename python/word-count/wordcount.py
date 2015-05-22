def word_count(phrase):
	words = phrase.split() 
	length = len(words)
	result = {}
	temp = []

	#iterate over list of words
	for word in words:
		#compares word with a temp list to see if its repeated
		if word in temp:
			continue
		else:
			#adds word to temp list
			temp.append(word)
			count = 0
			#compares word with other words in list 
			for i in words:
				if word == i:
					count = count +1
			result[word] = count

	return result



