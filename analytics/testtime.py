from datetime import datetime, timedelta
print(datetime.strftime(datetime.now() + timedelta(minutes=30), '%H:%M'))