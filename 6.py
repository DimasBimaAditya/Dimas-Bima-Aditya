answer1 = input('masukkan kata pertama ')
answer2 = input('masukkan kata kedua ')

print(answer1)
print(answer2)

if answer1 == answer2:
     print(f'{answer1} & {answer2} adalah anagram')
else:
     print(f'{answer1} & {answer2} bukan anagram')