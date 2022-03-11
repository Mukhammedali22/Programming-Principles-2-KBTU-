import re
txt = "abc_der, Ai_Hec au_uc alUm popIt"
x = re.findall("[a-z]+_[a-z]+", txt)
if x: print(x)
else: print("there is no snake_case in the text")