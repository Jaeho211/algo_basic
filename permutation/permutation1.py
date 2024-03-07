def permutation(word, char_set):
    str_set_copy = char_set.copy()
    for c in word:
        str_set_copy.discard(c)
    if len(str_set_copy) == 0:
        print(word)
        return
    for c in str_set_copy:
        permutation(word+c, str_set_copy)


string = "abcd"
char_set = set(string)
permutation('', char_set)