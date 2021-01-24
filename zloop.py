num = 0
count = 0.0

while True:
	sval = input("Enter number: ")

	if sval == 'done':
		break
	try:
		fval = float(sval)
	except:
		print("Only mubers allowed")
		continue
	num = num + 1
	count = count + fval

print("Finish")
print(num, count, count / num)
