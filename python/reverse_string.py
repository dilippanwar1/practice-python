str = 'revereseme'

def reverse_str (s):
    str = ""
    for i in s:
        print ("I IS " +i)
        str = i + str
        #str =  str + i
        print(str)

    return str




new_str = reverse_str(str)
print(new_str)