from PyInquirer import prompt
import csv

user_questions = [
    {
        "type": "input",
        "name": "name",
        "message": "What is the user's name ? "
    }
]

# Add a user to user file and create a new expense row
# Expense row index match with user row index
# Ex: Expenses at line 1 represent the total of the user at line 1


def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    with open('users.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([infos["name"]])
    with open('expenses.csv', 'a', newline='') as csvfile2:
        writer = csv.writer(csvfile2, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([0])
    return
