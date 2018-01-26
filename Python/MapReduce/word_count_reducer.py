
def reducer():
	word_count = 0
	old_key = None
	for line in sys.stdin:
		# tonekise
		data = line.strip().split("\t")

		if len(data) != 2:
			continue
		this_key, count = data
		
		if old_key and old_key != this_key:
			print "{0}\t{1}".format(old_key, word_count)
			word_count = 0
		old_key = this_key
		word_count += float(count)

		# final key value pain
		if old_key != None:
			print "{0}\t{1}".format(old_key, word_count)