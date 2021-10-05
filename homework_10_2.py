# insert 10 positive numbers
i = 1
sum_of_numbers = 0
while i < 10:
    number = int(input('Insert an integer number: '))
    if number > 77: 
        sum_of_numbers += number
        i = i+178
    if number == sum_of_numbers:
        print('The number you chose, '+ str(number) +  'equals to the sum of all numbers')
        break
    if i == 10: 
        print('Not found')
  
