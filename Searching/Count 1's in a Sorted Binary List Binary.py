def countOnes(arr, n):
	low = 0
	high = n - 1
	while (low <= high): # get the middle index
		mid = (low + high) // 2

		if (arr[mid] < 1):
			high = mid - 1

		elif(arr[mid] > 1):
			low = mid + 1
		else:

			if (mid == n - 1 or arr[mid + 1] != 1):
				return mid + 1
			else:
				low = mid + 1

	return 0


if __name__ == '__main__':

	arr = [1, 1, 1, 1, 0, 0, 0]
	n = len(arr)

	print("Count of 1's in given array is ", countOnes(arr, n))

