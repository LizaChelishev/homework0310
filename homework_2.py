sum_of_numbers_bigger_than_77 = 0
count_of_numbers_bigger_than_77 = 0
while True:
    number = int(input('Enter a number'))
    if number == 0:
        break
    if number > 77:
        sum_of_numbers_bigger_than_77 += number
        count_of_numbers_bigger_than_77 += 1
print('Count of numbers bigger than 77: ' + str(count_of_numbers_bigger_than_77))
print('Sun of numbers bigger than 77: ' + str(sum_of_numbers_bigger_than_77))
