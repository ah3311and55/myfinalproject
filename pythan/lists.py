doc=["apple" "banana","melon","grape" "ahmad"]
for x in range (len(doc)-1,-1,-1):
	word = doc[x]
	if("a" in word):
		doc.remove(word)
print doc