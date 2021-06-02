def reverseword(s):
    w=s.split(" ")
    print(w)
    w.reverse()
    new_string=''.join(w)
    print(new_string)
    return new_string
s=input("Enter the string")
print(reverseword(s))