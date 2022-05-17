a = "4*5+5"
print(eval(a))
#b = list[a]
b = []
for v in a:
    b.append(v)
output = ''
print(b)
for idx, val in enumerate(a):
    if val == "*": 
        output = int(b[idx-1]) * int(b[idx+1])
    elif(val == "+"):
        output = b[idx-1] + b[idx+1]
    
    print(output)
    
    
