def is_leap_year(year):
	# checks if input is int
	if isinstance(year, int):
		# checking for years divisible by 4, 400
		if year % 4 == 0 and year % 400 == 0:
			return True
		# checking for years divisible by 4 and not 100 
		elif year % 4 == 0 and year % 100 != 0:
			return True

	else:
		raise ValueError("year should be numeric")
		
	return False

