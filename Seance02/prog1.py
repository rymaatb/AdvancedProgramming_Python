import logging #logging is a library used for debugging , here we used logging.debug instead of print so it can show us where is the error or bug
hourly_wage = 20.0
hours = 6
day = "Sunday"

daily_wages = hourly_wage * hours
if day == "sunday":
    daily_wages * 2
logging.debug(f"daily wages : {daily_wages} errors")