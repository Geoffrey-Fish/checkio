class Date:
    def __init__(self, y, m, d):
        self.d = d
        self.m = m
        self.y = y
  
monthDays = [31, 28, 31, 30, 31, 30,
			31, 31, 30, 31, 30, 31]

def countLeapYears(d):
    
	years = d.y

	if (d.m <= 2):
		years -= 1

	return int(years / 4) - int(years / 100) + int(years / 400)

def getDifference(dt1, dt2):
    
	n1 = dt1.y * 365 + dt1.d

	for i in range(0, dt1.m - 1):
		n1 += monthDays[i]

	n1 += countLeapYears(dt1)

	n2 = dt2.y * 365 + dt2.d
	for i in range(0, dt2.m - 1):
		n2 += monthDays[i]
	n2 += countLeapYears(dt2)

	return (n2 - n1)

def days_diff(a,b):
    ay = a[0]
    am = a[1]
    ad = a[2]
    by = b[0]
    bm = b[1]
    bd = b[2]
    dt1 = Date(ay,am,ad)
    dt2 = Date(by,bm,bd)
    return abs(getDifference(dt1,dt2))

if __name__ == "__main__":
    print("Example:")
    print(days_diff((2014, 8, 27), (2014, 1, 1)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")