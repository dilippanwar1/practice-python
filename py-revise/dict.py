mydict  = {
    "k1": "v1",
    "k2": "v2",
    "k3": "v3",
    "k4": "v4",
    "k5": "v5",
    "k6": "v6",
    "k7": "v7"
    
}
print("dic keys are:" +str(mydict.keys()))
for k, v in mydict.items():
    print("Key is:" +k+ " value is:" +v)
#dic_keys = mydict.keys
#print("dic keys are:" +str(dic_keys()))

if 'k61' in mydict:
    print("it exists")
else:
    print("it doesn't")

if mydict.get('k1') is 'v11':
    print("Yo")