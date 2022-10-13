#function to convert hours to seconds
def convert_to_seconds(hours):
    
    seconds = hours*60*60
    
    return seconds

# Driver program
hours = int(input("\nEnter number of hours: "))

seconds=convert_to_seconds(hours)

print(hours, "hour/s = ", seconds, "seconds")
