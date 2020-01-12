def SquareDigit(n):
	x = " " 
	for i in str(n):
		x += str(int(i)**2) 
	return int (x)
  
print(SquareDigit(9119))
