# avg temperature in TLV is between -5 and 40 degrees
i = 0
while i < 10:
    temperature = int(input('input your temperature: '))
    if temperature > 40 or temperature < -5:
        print ('Your data is invalid')
        break
    i = i + 1

if i == 10:
    print('Your data is valid')