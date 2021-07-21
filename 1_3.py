num = int(input('Enter % (0-20): '))
word = ['процент', 'процента', 'процентов']
if num == 1:
    print(num, word[0])
elif 1 < num <= 4:
    print(num, word[1])
else:
    print(num, word[2])