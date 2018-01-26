def mapper():
	for line in sys.stdin:
		# tonekise
		data = line.strip().split(" ")
		for i in data:
			# clean data, remove upper case and punctuation 
			cleaned_data = i.translate(string.maketrans("",""),string.punctuation).lower()
			# creat key value pairs
			print "{0}\t{1}".format(cleaned_data,1)