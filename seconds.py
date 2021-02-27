import sys
import re

value_i = sys.stdin.readline()
value_s = value_i.strip()

# check if the input is an integer
result = re.match("[-+]?\d+$", value_s)

# check if the conditions are met
if (result is not None) and (0 < int(value_s)) <= 864000:

    value = int(value_s)
    days = value//86400
    if days < 10:
        days = '0' + str(days)

    value %= 86400
    hrs = value//3600
    if hrs < 10:
        hrs = '0'+str(hrs)

    value %= 3600
    mins = value//60
    if mins < 10:
        mins = '0' + str(mins)

    value %= 60
    secs = value
    if secs < 10:
        secs = '0'+str(secs)

    print(f"{days}d{hrs}h{mins}m{secs}s")

else:
    # invalid input
    print("ERRO")
