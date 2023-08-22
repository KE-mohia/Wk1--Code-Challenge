def convert_to_24_hour(hour, minute, period):
    if period == "am":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
    
    return f"{hour:02d}{minute:02d}"
    
# Test cases
print(convert_to_24_hour(8, 30, "am"))  # Output: "0830"
print(convert_to_24_hour(8, 30, "pm"))  # Output: "2030"
print(convert_to_24_hour(12, 15, "am")) # Output: "0015"
