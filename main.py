import random
import sys

months_raw = open("Months.txt",encoding="utf-8").readlines()
months_polish_raw = open("MonthsPolish.txt",encoding="utf-8").readlines()
months = []
months_polish = []

for element in months_raw:
    months.append(element.strip())

for element in months_polish_raw:
    months_polish.append(element.strip())

option = input("""
Choose an option:
1 - What month comes before
2 - English to Polish months

quit - To exit
> """)

if option == "1":
    user_answer_before = ""
    user_answer_current = ""
    user_answer_after = ""
    optionOneScore = 0

    while True:

        random_month_number = random.randrange(len(months))
        random_month = months[random_month_number]
        month_before = months[random_month_number - 1]

        # The next 2 lines are there to print out a line of "=" that is the length of the question.
        to_print = f"The current month is {random_month}. What comes before?: "
        print("=" * len(to_print))
        user_answer_before = input(to_print)

        if user_answer_before == month_before:
            optionOneScore += 1
            print(f"Well Done, your score is {optionOneScore}")
        elif user_answer_before == "-1":
            break
        else:
            optionOneScore -= 1
            print(f"Try again, it was {month_before}, your score is {optionOneScore}")

elif option == "2":
    optionTwoScore = 0
    user_answer_polish = ""

    while True:
        random_month_number = random.randrange(len(months))
        englishMonth = months[random_month_number]
        polishMonth = months_polish[random_month_number]

        user_answer_polish = input(f"The current month is {englishMonth}, what is this month in Polish?: ")

        if user_answer_polish == polishMonth:
            optionTwoScore += 1
            print(f"Well done, your score is {optionTwoScore}")
        else:
            optionTwoScore -= 1
            print(f"Try again, your score is {optionTwoScore}")

elif option == "quit":
    sys.exit()
else:
    print("Not a valid option.")