"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
items = [100, 'hello', '100', '100', 100]
def frequencies(items): 
	newList = []

	for i in items:
	
		if i not in newList:
			if type(i) is not str:
				n = str(i)
				index = items.index(i)
				items[index] = n
				newList.append(n)
			else:
				newList.append(i)
			
	frequencies = {}
	for x in newList:
		frequencies[x] = items.count(x)
	return frequencies

print(frequencies(items))
