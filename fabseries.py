def fabnocci(n):
	# base case
	if n==0:
		return 0
	elif n==1:
		return 1
	# recursive case
	else:
		return fabnocci(n-1)+fabnocci(n-2)
print(fabnocci(int(input("enter number:"))))