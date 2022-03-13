import re
#txt = input()
txt = "youArePrettiestGirlIHaveEverSeen"
x = re.sub(r"([A-Z]|[a-z][a-z]*)([A-Z][a-z]*)", r"\1 \2 ", txt).strip()
x = re.sub(" ", "_", x).lower()
print(x)

'''
import re
#txt = input()
txt = "youArePrettiestGirlIHaveEverSeen"
x = re.findall("^[a-z]+", txt) + re.findall("[A-Z][a-z]*", txt)
#re.findall("^[a-z]+", txt) чтобы получить первое слово начинающийся с маленькой буквы это "you"
#re.findall("[A-Z][a-z]*", txt) все остальные слова начинающиеся с большой буквой
snake_case = ""
for i in x:
    if i[0].isupper():
        snake_case += '_'
    snake_case += i.lower()
print(snake_case) 
'''
