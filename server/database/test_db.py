from service import select_all

data = select_all('./database/users.db', 'USERS')

for row in data:
    print(row)