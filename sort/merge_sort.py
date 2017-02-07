

'''
test_list = [1,2,3,4,5,5,6,6,8]

'''

test_list = [5,1,2,6,3,8,4,5,6]


def merge_sort(test_list):
	A = []
	B = []
	T = test_list
	print("S ",test_list)
	if len(test_list) > 1:
		mid = len(test_list)//2
		A = test_list[:mid]
		B = test_list[mid:]
		
		merge_sort(A)
		merge_sort(B)
		
		i = 0
		j = 0
		k = 0
		print("time", A, B)
		while i<len(A) and j<len(B):

			if A[i] < B[j]:
				#print(counter_a)
				#T.append(A[i])
				T[k] = A[i]

				i = i + 1
			else:
				#T.append(B[j])
				T[k] = B[j]
				j = j +1
			k = k+1


		while i<len(A):
			T[k] = A[i]
			k = k+1
			#T.append(A[i])
			i = i +1
		while j<len(B):

			#T.append(B[j])
			T[k] = B[j]
			k = k+1
			j = j+1
		#merge
	print("Merging ",T)


		


if __name__ == '__main__':
	print(merge_sort(test_list))


