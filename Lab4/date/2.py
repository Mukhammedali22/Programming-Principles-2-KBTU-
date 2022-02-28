import datetime
today = datetime.datetime.now()
d = datetime.timedelta(days = 1)
yesterday = today - d
tomorrow = today + d
print("yesterday:  ", yesterday.strftime("%c"))
print("today:      ", today.strftime("%c"))
print("tomorrow:   ", tomorrow.strftime("%c"))