username = []
if username:
    for u in username:
        if u == 'Admin':
            print(f"Hello {u}, would you like to see our status report")
        else:
            print(f"Hello {u}, thank you for logging in")
else:
    print("We need to get some users first")
