def working(steps, total_moral, camp_s, steps_n, enc, camp):
    actions = []
    total_moral += camp
    for step in steps:
        if total_moral < -20:
            print('Caution')
        if total_moral < -30:
            actions.append('d')
            break
        actions.append(step)
        if step == 'b':
            total_moral -= 3
        if step == ' ':
            total_moral -= per_tile
        if step == 'c':
            total_moral -= per_encounter
            total_moral -= 1
            camp_s += 1
        if step == 'x':
            total_moral -= 1
            camp_s += 1
        if step == 'n':
            total_moral -= per_encounter
            enc = + 1
        if step == 'e':
            steps_n += 1
            break
        if step == 's':
            pass
        steps_n += 1

    for moves in actions:
        if moves == 's':
            print('Start', end=',')
        if moves == ' ':
            print('Normal tile', end=',')
        if moves == 'c':
            print('Camp tile with encounter', end=',')
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
    return '\nMoral Left:{}\nSteps taken:{}\nEncounters:{}\nCamp done:{}'.format(total_moral, steps_n, enc, flag)


print('Enter The path one tile at a time')
per_encounter = 7
per_tile = 1
exception = 'Moral is consumed at Fights that occur on tiles where camping is unavailable ' \
            '(i.e. not at corners or intersections)\nDo remember to go to beginning to exit'
total_moral = 70
flag = True
steps_n = 0
encounter = 0
camp_s = 0
step = 'd'
print(exception)
print('Journal:\ns to start\n\' \' for normal\nc for camp\nx for camp but no fight\nn for encounter\n'
      'b for return to beginning\ne to exit')
mora_l = input('Camp Moral:')
mora_l = int(mora_l)
steps = input('Enter the steps\n')
print(working(steps, total_moral, camp_s, steps_n, encounter, mora_l))
# print(len(actions))
