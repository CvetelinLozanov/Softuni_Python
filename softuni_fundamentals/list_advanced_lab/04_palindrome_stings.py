def palindrome_strings():
    palindromes = [word for word in input().split() if word == word[::-1]]
    searched_word = input()
    word_count = palindromes.count(searched_word)

    print(palindromes)
    print(f'Found palindrome {word_count} times')


palindrome_strings()
