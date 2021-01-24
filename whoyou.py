handle = open('mbox-short.txt')

authors = dict()
largest = None
for ln in handle:
	if not ln.startswith('From'):
	#if !ln.startswith('From'):
		continue
	else:
		words = ln.split()
		if len(words) > 0:
			authors[words[1]] = authors.get(words[1], 0) + 1
for key in authors:
	if largest is None or int(authors[key]) > largest:
		largest = int(authors[key])
		mail = key
print(mail,largest)			
