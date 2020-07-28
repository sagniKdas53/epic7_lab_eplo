print('Enter The path one tile at a time')
per_encounter = 7
per_tile = 1
exception = 'Fights that occur on tiles where camping is unavailable (i.e. not at corners or intersections)\n ' \
            'Do remember to go to beginning to exit'
total_moral = 70
flag = False
steps_n = 0
encounter = 0
camp_s = 0
actions = []
step = 'd'
print(exception)
print('Step:\ns to start\nm for normal\nj for camp\nx for camp but no fight\nn for encounter\nb for return to beginning'
      '\ne to exit')
while total_moral > -30:
    steps = input()
    for step in steps:
        #print(step)
        if total_moral < -20:
            print('Caution')
        if total_moral < -30:
            actions.append('d')
            break
        actions.append(step)
        if step == 'b':
            total_moral -= 3
        if step == 'm':
            total_moral -= per_tile
        if step == 'j':
            total_moral -= per_encounter
            total_moral -= 1
            camp_s += 1
            print(total_moral)
            if total_moral < 0 and flag is False:
                camp = input('Camp Moral')
                total_moral += int(camp)
                flag = True
        if step == 'x':
            total_moral -= 1
            camp_s += 1
            print(total_moral)
            if total_moral < 0 and flag is False:
                camp = input('Camp Moral')
                total_moral += int(camp)
                flag = True
        if step == 'n':
            total_moral -= per_encounter
            encounter =+ 1
        if step == 'e':
            steps_n += 1
        if step == 's':
            steps_n += 1
            #print(total_moral,steps_n)
            break
        steps_n += 1
    if step == 'e':
        break

for moves in actions:
    if moves == 's':
        print('Start', end=',')
    if moves == 'm':
        print('Normal tile', end=',')
    if moves == 'j':
        print('Camp tile', end=',')
    if moves == 'j':
        print('Camp tile no encounter', end=',')
    if moves == 'n':
        print('encounter', end=',')
    if moves == 'b':
        print('move to beginning', end=',')
    if moves == 'e':
        print('exit', end='\n')
    if moves == 'd':
        print('ded lol', end='\n')
print('\nMoral Left:{}\nSteps taken:{}\nCamp done:{}'.format(total_moral,steps_n,flag))
#trial : https://gist.github.com/bc29de4f27382a1dba2a19bd8af75a81
