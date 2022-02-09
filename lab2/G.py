number_of_demons = int(input())
weakness_of_each_demon = []
d = set()
for i in range(number_of_demons):
    s = input().split()
    weakness_of_each_demon.append(s[1])
    d.add(s[1])
amount_of_hunters = int(input())
hunters = []
hunters_ability = set()
for i in range(amount_of_hunters):
    s = input().split()
    hunters.append(s)
    hunters_ability.add(s[1])
h_dict = {}
d_dict = {}
for i in hunters_ability:
    sum = 0
    for j in range(len(hunters)):
        if i == hunters[j][1]:
            sum += int(hunters[j][2])
            h_dict[i] = sum
for i in d: 
    d_dict[i] = weakness_of_each_demon.count(i)
number_of_remaining_demons = number_of_demons
for i in h_dict.keys():
    for j in d_dict.keys():
        if i == j:
            if h_dict[i] >= d_dict[j]:
                number_of_remaining_demons -= d_dict[j]
            else:
                number_of_remaining_demons -= h_dict[i]
print("Demons left:", number_of_remaining_demons)

