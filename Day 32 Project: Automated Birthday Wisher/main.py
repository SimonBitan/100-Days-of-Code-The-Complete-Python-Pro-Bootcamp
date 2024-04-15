import pandas as pd
import datetime as dt
import random
import smtplib

# your email
MY_EMAIL = "example@email.com"

# the app password for your email (configure online)
PASSWORD = "abcd1234()"

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
update_birthday = input("Would you like to add or update the birthday data? Type 'yes' or 'no': ").lower()
if update_birthday == "yes":
    # Get the birthday info.
    name = input("What is their name?: ")
    email = input("What is their email address?: ")
    year = int(input("In what year were they born?: "))
    month = int(input("In what month were they born? (month number): "))
    day = int(input("On what day were they born?: "))

    # Make a list of lists of the inputs, then turn it into a dataframe to append to the csv.
    data = [[name, email, year, month, day]]
    df = pd.DataFrame(data)

    # Update the birthday data with the above dataframe.
    df.to_csv("birthdays.csv", mode="a", index=False, header=False)
elif update_birthday != "no":
    print("Please type 'yes' or 'no' and try again.")

# 2. Check if today matches a birthday in the birthdays.csv
# Obtain today's month, and day in integer values.
month = dt.datetime.now().month
day = dt.datetime.now().day

# Match these values to values in the csv, if they exist.
birthday_data = pd.read_csv("birthdays.csv")

matching_entry = birthday_data[
    (birthday_data['month'].astype(int) == month) &
    (birthday_data['day'].astype(int) == day)
]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
letter_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

if len(matching_entry) != 0:
    birthday_name = matching_entry['name'].values[0]
    random_letter = random.choice(letter_list)
    with open(random_letter, "r") as file:
        letter = file.read()
        letter = letter.replace('[NAME]', birthday_name)
        # letter = letter.replace("\n", "")

# 4. Send the letter generated in step 3 to that person's email address.
    birthday_email = matching_entry['email'].values[0]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_email,
                            msg=f"Subject: Happy birthday {birthday_name}\n\n{letter}"
                            )
    print(f"Birthday email sent to {birthday_name} from {MY_EMAIL} to {birthday_email}.")
else:
    print("There are no birthdays today.")
