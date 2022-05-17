import re
#http_code_list = re.findall('(?:304|200|404)', log)
txt = "I am aa log and and i have two http code like 400 and there is another code as well like 505. Can you find these 2 codes in this text please?"

#http_codes = re.findall('(\d{3})', txt)
#x = re.search("^The.*Spain$", txt)
y = re.findall('(?:\d{3})', txt)
#print(http_codes)
print(y)
#print(type(x))