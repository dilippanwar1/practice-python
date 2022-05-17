mydict = {
"k1" : "v1",
"k2" : "v2",

}

print ("lenth of dict is " +str(len(mydict)))
key_List = mydict.keys()
print(key_List)
print("My dict keys: " +str(key_List))
mydict.update({'k3': 'v3'})

print(mydict.values())
print(mydict.items())
for k,v in mydict.items():
    print("key is " +k+ "Value is " +v)

if 'k1' in mydict:
    print("yes k1 is there")