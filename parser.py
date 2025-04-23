'''Testing the time parser for various formats and edge cases.'''
import re
from datetime import datetime, timedelta, timezone
from dateutil.relativedelta import relativedelta

def parse(time_string: str) -> datetime:
    """
    Parses a time string like 'now()+10d+12h' and returns a datetime object in UTC.
    """
    # Validate and extract base modifier
    if not time_string.startswith("now()"):
        raise ValueError("Only 'now()' is supported as the base time.")

    # Start with current UTC time
    result_time = datetime.now(timezone.utc)

    # Extract the operations, e.g., +10d, +5h
    modifiers = re.findall(r'\+(\d+)(s|m|h|d|mon|y)', time_string)

    for value_str, unit in modifiers:
        value = int(value_str)
        if unit == 's':
            result_time += timedelta(seconds=value)
        elif unit == 'm':
            result_time += timedelta(minutes=value)
        elif unit == 'h':
            result_time += timedelta(hours=value)
        elif unit == 'd':
            result_time += timedelta(days=value)
        elif unit == 'mon':
            result_time += relativedelta(months=value)
        elif unit == 'y':
            result_time += relativedelta(years=value)
        else:
            raise ValueError(f"Unsupported time unit: {unit}")

    return result_time


print(parse("now()+1d+3h")) 
print(parse("now()+2mon+5d"))
print(parse("now()+1y+2mon+3d+4h+5m+6s"))

