duration = int(input('Enter duration in (sec): '))
sec = duration % 60
min = duration // 60 % 60
hour = duration // 3600

print('Time:', hour, 'hr', min, 'min', sec, 'sec')