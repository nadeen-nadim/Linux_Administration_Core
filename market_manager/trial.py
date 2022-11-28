from datetime import datetime

date_time = datetime.now()

date_time = date_time.strftime("Date: %d/%m/%Y\nTime: %H:%M:%S")
print(date_time) 