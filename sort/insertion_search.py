
'''
test_list = [1,2,3,4,5,5,6,6,8]

'''

test_list = [5,1,2,6,3,8,4,5,6]

def insertion_search(test_list):
	counter = 0
	for i in test_list:
		j = counter
		while j>0 and test_list[j-1] > test_list[j]:
			temp = test_list[j]
			test_list[j] = test_list[j-1]
			test_list[j-1] = temp
			j = j - 1		
		counter = counter + 1
	print(test_list)