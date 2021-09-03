import random

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
user_answer_before = ""
user_answer_current = ""
user_answer_after = ""
score = 0

while user_answer_before != "-1":
    print("=========================")
    random_month_number = random.randrange(len(months))
    random_month = months[random_month_number]
    month_before = months[random_month_number - 1]

    print(f"The current month is {random_month}.")
    user_answer_before = input("What comes before?: ")

    if user_answer_before == month_before:
        score += 1
        print(f"Well Done, your score is {score}")
    else:
        score -= 1
        print(f"Try again, your score is {score}")