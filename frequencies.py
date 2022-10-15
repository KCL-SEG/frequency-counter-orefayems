"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
items = [obj(i) for i in input().split(",")]
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
