import re
txt =  "my_name, perfect_number, snake_case, ali, upper_case, bin_to_dec, aliZak, you_are_prettiest_girl_i_have_ever_seen"  #snake case
x = re.sub('_', ' ', txt).split(',')
for i in x:
    y = i.split()
    string = y[0]
    for j in range(1, len(y)):
        string += y[j].capitalize()
    print(string, end = " ")                            