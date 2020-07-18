from datetime import datetime
from pytz import timezone

fmt = "%Y-%m-%d %H:%M:%S %Z%z"

# get the current time in UTC
now_utc = datetime.now(timezone('UTC'))
print('UTC :', now_utc)

# Convert this to EST
now_est = now_utc.astimezone(timezone('US/Eastern'))
print('EST :', now_est)

# Convert this to Berlin
now_berlin = now_utc.astimezone(timezone('Europe/Berlin'))
print('Berlin:', now_berlin)

# Convert this to London
now_london = now_utc.astimezone(timezone('Europe/London'))
print('London:', now_london)

# Convert this to Kolkata
now_Kolkata = now_utc.astimezone(timezone('Asia/Kolkata'))
print('Kolkata:', now_Kolkata)

# Convert this to Shanghai
now_Shanghai = now_utc.astimezone(timezone('Asia/Shanghai'))
print('Shanghai:', now_Shanghai)

# Convert this to Sydney
now_Sydney = now_utc.astimezone(timezone('Australia/Sydney'))
print('Sydney:', now_Sydney)

# Convert this to Johannesburg
now_Johannesburg = now_utc.astimezone(timezone('Africa/Johannesburg'))
print('Johannesburg:', now_Johannesburg)
