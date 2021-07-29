all_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, v in enumerate(all_list):
    if v.isdigit():
        all_list[i] = f'"{ int( v):02}"'
    elif v[1:].isdigit():
        all_list[i] = f'"{v[0]}{int(v[1:]):02}"'

print(all_list)
print("".join(all_list))