def reverseword(s):
    w=s.split(sep=" ",maxsplit=3)
    print(w)
    new_word=[i[::-1]for i in w]
    print(new_word)
    new_string=''.join(new_word)
    print(new_string)
    return new_string

s=input("Enter the string")
print(reverseword(s))
