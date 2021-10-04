current_modulu = 2
previous_number = -1
while current_modulu < 10:
    number = int(input('Enter a number that divides by ' + str(current_modulu) + ': '))
    if number < 0:
        continue
    if number % current_modulu == 0:
        current_modulu += 1
    if previous_number == number:
        print ('You entered the same number twice in a row.')
        break
    previous_number = number


