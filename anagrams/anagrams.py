def anagram(text: str) -> str:
    if type(text) != str:
        raise TypeError('Выражение должно содержать только строковые символы')

    words_list = text.split(' ')
    new_list = []

    # made new word without symbol, only letters
    for word in words_list:
        clean_word = [letter for letter in word if letter.isalpha()]

        # add symbol at the same place
        word_with_symbol = []
        for letter in word:
            if letter.isalpha():
                word_with_symbol.append(clean_word.pop())
            else:
                word_with_symbol.append(letter)
        # save reverse word with symbol to the list like str
        new_list.append(''.join(word_with_symbol))

    return ' '.join(new_list)

print(anagram('a1b                        2b'))

if __name__ == '__main__':
    cases = [
        ('a1bcd efg!h', 'd1cba hgf!e'),
    ]

    for text, reversed_text in cases:
        assert anagram(text) == reversed_text
