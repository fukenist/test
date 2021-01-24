def computePay(hours,rate):
	print("In compute", hours, rate)
	if(hours > 40):
		reg = hours * rate
		over = (hours - 40) * (rate / 2)
		pay = reg + over

	else:
		pay = fr * ft
	print("Верни", pay)
	return pay
	
sr = input("Часы")
st = input("Рейтинг")

try:
	fr = float(sr)
	ft = float(st)
except:
	print("Только цифры")
	quit()
	
xp = computePay(fr,ft)	



	
print("Плата:", xp)