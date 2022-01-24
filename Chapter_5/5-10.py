current_user = ['leo', 'Tobey', 'Tom', 'andrew', 'spidy']
new_user = ['LeO', 'tOm', 'Margot', 'Robbie', 'zendaya']

current_user = [user.lower() for user in current_user]
new_user = [user.lower() for user in new_user]

for current in current_user:
    for user in new_user:
        if user == current:
            print(f"Username_ {user} not available")
        else:
            print("username available")
