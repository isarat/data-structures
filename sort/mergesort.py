#merge sort

# merges left and right
def merge(left, right):
	print "Merging left " + str(left) + " and right " + str(right)
	result = []
	i,j = 0, 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i= i + 1
		else:
			result.append(right[j])
			j = j + 1

	# add the remaining
	result += left[i:]
	result += right[j:]
	return result

# partition in to two and calls merge
def sort(lst):

	if len(lst) < 2:
		return lst

	middle = len(lst)/2

	left = sort(lst[:middle])
	print "Processed left" + str(left)

	right = sort(lst[middle:])
	print "Processed right" + str(right)

	return merge(left,right)

sort_items = [55,15,33,18,21,41,25,53]
print sort(sort_items)