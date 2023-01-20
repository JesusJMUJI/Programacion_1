class Date:
    monthDays = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31]
    def __init__(self, _day, _month, _year):
        self.day = _day
        self.month = _month
        self.year = _year

    def __str__(self):
        return '{0}//{1}//{2}'.format(self.day, self.month, self.year)

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year

    def isAnnualEvent(self, annualEventDate):
        return self.day == annualEventDate.day and self.month == annualEventDate.month

    def AddDays(self, daysToAdd):
        self.day += daysToAdd

        currentMonthDay = self.monthDays[self.month - 1]
        if  self.day >= currentMonthDay:
            self.day = self.day % currentMonthDay
            self.month += 1

            if  self.month > 12:
                self.month = 1
                self.year += 1

    def isLeapYear(self):
        leapYear = False

        if self.year % 4 == 0:
            leapYear = True

            if self.year % 100 == 0:
                leapYear = False

                if self.year % 400 == 0:
                    leapYear = True

        return leapYear


me_birthday = Date(27, 10, 2001)

keira_birthday = Date(29, 4, 2004)

today = Date(29, 4, 2000)


print(today.isLeapYear())
