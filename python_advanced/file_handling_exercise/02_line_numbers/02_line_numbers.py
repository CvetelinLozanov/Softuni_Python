from string import punctuation, ascii_lowercase, ascii_uppercase

input_file = "text.txt"
punctuation_counter = 0
letters_counter = 0

with open(input_file) as f, open("output.txt", "w") as of:
    for row, line in enumerate(f.readlines(), start=1):
        for ch in line:  # iterate through every char from line
            if ch in punctuation:  # check if char is punctuation symbol
                punctuation_counter += 1
            elif ch in ascii_lowercase or ch in ascii_uppercase:  # check if char is letter
                letters_counter += 1

        of.writelines(f"Line {row}: {line.strip()}({letters_counter})({punctuation_counter})\n")
        letters_counter = 0
        punctuation_counter = 0
