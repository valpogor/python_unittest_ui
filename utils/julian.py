import datetime
import string
import secrets
import pytz


def getUID(size=12, char=string.ascii_uppercase + '234567'): #BASE32 characters
    return''.join(secrets.choice(char) for _ in range(size))

def getJulian():
    #make sure we use paccific time when creating the tuid
    utc_now=datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
    pacific_now=utc_now.astimezone(pytz.timezone("US/Pacific"))
    dt = pacific_now
    year = dt.strftime("%y")
    date = dt.strftime('%Y.%m.%d')
    today = datetime.datetime.strptime(date,'%Y.%m.%d')
    tt = today.timetuple()
    julian = '{0}{1}'.format(year,str(tt.tm_yday).zfill(3))
    return julian

def getTedsTUID():
    julian=getJulian()
    tiud=julian+getUID(6)+'-'+getUID(6)
    return tiud
print(getTedsTUID())