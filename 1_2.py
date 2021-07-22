coubes_list = []
add_coubes_list = []
all_sum = 0

for i in range(1, 1000, 2):
    coubes_list.append(i ** 3)

for ind, val in enumerate(coubes_list):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += coubes_list[ind]
    if sum_digits % 7 == 0:
        all_sum += coubes_list[ind]

print(all_sum)





