def permutation(word, add_char, char_set):
    word += add_char
    char_set_copy = char_set.copy()
    char_set_copy.remove(add_char)
    if len(char_set_copy) == 0:
        print(word)
        return
    for c in char_set_copy:
        permutation(word, c, char_set_copy)


string = "abcd"
str_set = set(string)
permutation('', str_set)