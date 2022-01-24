# these people already taken the poll
favorite_languages = {
    'phil': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'jen': 'python',
}

# these people should take the poll
name = ['jen', 'phil', 'hamza', 'zaid']
for i in name:
    if i in favorite_languages.keys():
        print("Thank you for responding, ", i)
    else:
        print("Please Respond, ", i)
