def add_songs(*args):
    songs = {}

    for arg in args:
        song = arg[0]
        lyric = arg[1]
        if song not in songs:
            songs[song] = lyric
        else:
            songs[song].extend(lyric)

    result = []

    for song, lyrics in songs.items():
        result.append(f"- {song}")
        for lyric in lyrics:
            result.append(lyric)

    return "\n".join(result)


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))