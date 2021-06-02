def reverseword(s):
    w=s.split(sep=" ")
    print(w)
    w[0],w[1]=w[1],w[0]
    print(w)
    new_string=''.join(w)
    print(new_string)
    return new_string

s=input("Enter the String")
print(reverseword(s))

