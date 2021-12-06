# 6 components: Year, Month, Day, Hour, Minute, Second

import time

#print(time.localtime(time.time()))

mytime = time.localtime(time.time())
#time is a reserved keyword and as such will show in green and not be valid as variable name

print(time.asctime(mytime))