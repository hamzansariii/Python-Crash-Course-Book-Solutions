

def make_album(artist_name, album_title, no_songs=None, info={}):

    info['Artist_name'] = artist_name
    info['Album_title'] = album_title

    if no_songs:
        print(f"name:{artist_name} and title={album_title} and no={no_songs}")
        info['No_Songs'] = no_songs
        print(info)

    else:
        print(f"Artist_name:{artist_name} and Album_title={album_title}")
        print(info)


#make_album('charlie puth', 'attention')
#make_album('justin bieber', 'sorry', 8)
