handle = open('asya.txt',encoding="utf8")

letters = dict()
#look through the history of messages
for ln in handle:
	words = ln.split()
	for word in words:
		ltrs = list(word)
		for lt in ltrs:
			lt = lt.lower()
			if lt.isalpha():
				letters[lt] = letters.get(lt, 0) + 1

lst = list()		

for k,v in list(letters.items()):
	lst.append((v,k))
#sort the most popular words	
lst.sort(reverse=True)
for k,v in lst:
	print(k,v)	