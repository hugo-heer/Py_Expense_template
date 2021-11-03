from PyInquirer import prompt
import csv

# Return a list with all the users


def get_users(answer):
    with open('users.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    flat_list = [item for sublist in data for item in sublist]
    return flat_list


def list_to_object_list(answer):
    l = get_users("e")
    new_l = []
    for i in l:
        new_l.append({"name": i})
    return new_l


expense_questions = [
    {
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
    {
        "type": "list",
        "name": "spender",
        "message": "New Expense - Spender: ",
        "choices": get_users
    },
    {
        "type": "checkbox",
        "qmark": "X",
        "message": "Select participants",
        "name": "participants",
        "choices": list_to_object_list
    }
]

# Return the row of the spender


def get_spender(spender):
    with open('users.csv', 'r') as o:
        myData = csv.reader(o)
        i = 0
        for row in myData:
            i = i + 1
            if row[0] == spender:
                return i

# Modify users' balances


def add_default_expense(num, spenderId):
    i = 1
    with open('expenses.csv', 'r') as o:
        myData = csv.reader(o)
        l = list(myData)
        i = 1
        for elm in l:
            if spenderId == i:
                elm[0] = int(float(elm[0])) + (int(float(num)) / len(l))
            else:
                elm[0] = int(float(elm[0])) - (int(float(num)) / len(l))
            i = i + 1
        with open('expenses.csv', 'w') as file:
            writer = csv.writer(file, delimiter='|',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(l)


def new_expense(*args):
    infos = prompt(expense_questions)
    with open('expense_report.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([infos["spender"]] +
                        [infos["amount"]] + [infos["label"]])

    spender = get_spender(infos["spender"])

    add_default_expense(infos["amount"], spender)
    print("Expense Added !")
    return True
