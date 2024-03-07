def permutation(word, char_list):
    if len(char_list) == 0:
        print(word)
        return
    for idx in range(len(char_list)):
        permutation(word + char_list[idx], char_list[:idx]+char_list[idx+1:])


string = "abcd"
char_list = list(string)
permutation('', char_list)