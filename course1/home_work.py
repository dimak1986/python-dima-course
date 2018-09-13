
q = input('what is the lang of Isael: ')
if q != 'Hebrew':
    print('Not at all!')
else:
    print("you're right")

print('you need to give paraments to matter a square')

y = int(input('give a number for y: '))

x = int(input('give a number for x: '))

answer = int(x * y)

print(answer)


while True:
    q2 = input('How much will be 5 + 5:')
    if float(q2) == 10:
        print('good = %s' % q2)
        break
    else:
        print('%s you are wrong' % q2)
        continue
