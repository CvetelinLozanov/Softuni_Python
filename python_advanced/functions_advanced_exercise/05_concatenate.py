def concatenate(*args, **kwargs):
    txt = ''

    for word in args:
        txt += word

    for k, v in kwargs.items():
        if k in txt:
            txt = txt.replace(k, v)

    return txt

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print()
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))