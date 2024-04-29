num = 10
a=0
b=1

next_number = b
count = 1

while a <= num:
     if num==a:
          print(f'{num} merupakan bilangan fibonacci')
          a,b = b, a+b
          print(f'{num} bukan fibonacci')
