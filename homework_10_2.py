# insert 10 positive numbers
i = 0
sum_of_numbers = 0
while i < 10:
    number = int(input('Insert an integer number #' + str(i+1) + ': '))
    if number == sum_of_numbers:
        print('The number you entered ('+ str(number) +') equals to the sum of all previous numbers.')
        break
    sum_of_numbers += number
    i += 1

if i == 10:
    print('Not found')
  
