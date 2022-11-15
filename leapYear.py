def days_in_month(year, month):
    leap=year%4
    if year<1959 and month==2:
        return 28
    elif year>1960:
        if leap==0 and month==2:
            return 29
        elif leap!=0 and month==2:
            return 28
        elif month in [9,4,6,11]:
            return 30
        elif month in [1,2,3,5,7,8,10,12]:
            return 31
    

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
