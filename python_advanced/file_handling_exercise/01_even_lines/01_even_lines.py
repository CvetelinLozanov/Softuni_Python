file = 'text.txt'
valid_symbols = ("-", ",", ".", "!", "?")


with open(file) as f, open("output.txt", 'w') as of:
    for row, line in enumerate(f.readlines()):
        for s in valid_symbols:
            line = line.replace(s, '@')
        if row % 2 == 0:
            of.writelines(' '.join(line.split()[::-1]) + '\n')
