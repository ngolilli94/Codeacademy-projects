from datetime import datetime

now = datetime.now()
print now

# Fetching only current yy, dd, or mm
#print now.year
#print now.month
#print now.day

# Formatting date
# mm/dd/yyyy
#print '%02d/%02d/%04d' % (now.month, now.day, now.year)

# yyyy/mm/dd
#print '%04d/%02d/%02d' % (now.year, now.month, now.day)

# Date & Time
print 'The current date and time is %02d/%02d/%04d %02d:%02d:%02d.' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

# Stringifying datetime
print now.strftime('%B') #Month name
print now.strftime('%a') #Abbreviated weekday
print now.strftime('%I') #Current hour in 12-hour format
print now.strftime('%p') #AM or PM