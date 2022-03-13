import re
txt = "you_are_prettiest_girl_i_have_ever_seen"
x = re.sub(r"([a-z]+)_", r"\1 ", txt)
x = re.split(" ", x)
s = ""
for i in x:
    s += "".join(i).capitalize()
print(s)
