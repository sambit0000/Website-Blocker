# Importing the required libraries
import time
from datetime import datetime as dt

# Specifying the file path for host file
hosts_path = r'C:\Windows\System32\Drivers\etc\hosts'
# Local IP address
redirect = '127.0.0.1'
# List of websites to block
website_list = ['www.facebook.com','facebook.com']

# Infinite loop
while True:
    # Conditional, if time is in working hours
    if dt(dt.now().year,dt.now().month,dt.now().day,12) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,20):
        print('Working Hours...')
        # Open the host file
        with open(hosts_path,'r+') as file:
            # Read contents of host file
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    # Write in host file the website to block
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path,'r+') as file:
            # Read as a list
            content = file.readlines()
            # Place the cursor at the start of file
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            # Remove the extra content of file
            file.truncate()
        print('Enjoy time')
    # Execute after every 7 seconds
    time.sleep(7)
