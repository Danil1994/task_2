class NotStringSymbolError(TypeError):
    pass


def anagram(text: str) -> str:
    if not isinstance(text, str):
        raise NotStringSymbolError('You must use only string symbol')

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
