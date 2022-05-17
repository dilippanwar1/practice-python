my_list = ['djk', 'sdgds', 'sfw3', 1]
my_str = 'iamstraight'
rev_str = ''
for counter, value in enumerate(my_list, -1):
    rev_str = str(value) + rev_str

print('reverse str is ' +rev_str)
