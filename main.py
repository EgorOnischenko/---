

nested_list = [
		['a', 'b', 'c'],
		['d', 'e', 'f', 'h', False],
		[1, 2, None],
	]

for item in nested_list:
	for k in item:
		print(k)

print()


flatList = [item for elem in nested_list for item in elem]
print(flatList)