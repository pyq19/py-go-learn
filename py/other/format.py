_format = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}

class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _format[code]
        return fmt.format(d=self)


d = Date(1999, 5, 3)
print format(d) # 1999-5-3
print format(d, 'mdy') # 5/3/1999
print format(d, 'dmy') # 3/5/1999

# print 'the date is {: ymd}'.format(d) # ERROR
