import random
from random import randint

from dotenv import load_dotenv
from os import getenv
load_dotenv()
email=getenv('EMAIL')
password=getenv('PASSWORD')
import pandas as pd
import datetime as dt
import smtplib
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
data=pd.read_csv('birthdays.csv').to_dict('records')
print(data)

# 2. Check if today matches a birthday in the birthdays.csv
today=dt.datetime.now()
today_month=today.month
today_day=today.day

for value in data:
    if value['month']==today_month and value['day']==today_day:
        random_letter=randint(1,3)
        with open(f'./letter_templates/letter_{random_letter}.txt','r') as f:
            mail_message=f.read().replace('[NAME]', value['name'])
        with smtplib.SMTP('smtp.gmail.com',587)as s:
            s.starttls()
            s.login(email,password)
            s.sendmail(email,value['email'],f'Subject:Happy Birthday!\n\n{mail_message}')
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




