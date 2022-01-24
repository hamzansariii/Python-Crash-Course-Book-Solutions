from album import make_album  # album is 8-7

while True:
    print("Enter 'q' anytime to quit\n")
    artist = input("Enter Your fav artist name : ")
    song = input("Enter your fav song of her/his : ")
    num = int(input("Do you know how many albums you fav artist have : "))
    if num == 'no':
        make_album(artist, song)
    else:
        make_album(artist, song, num)
    break
