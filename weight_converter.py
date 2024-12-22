#Python Weight converter (Kg to Lbs)
Weight = float(input('Enter your weight: '))
Unit = input('Enter unit (Kg or Lbs): ')

if Unit == 'Lbs':
    weight = Weight / 2.505
    print(f'your weight is {weight} Kgs',)
elif Unit == 'Kg':
    weight = Weight * 2.505
    print(f'your weight is {weight} Lbs')
else:
    print('your entered information is not valid, please enter the right information')
