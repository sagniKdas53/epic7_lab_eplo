# (steps, totalmoral, campspots, n_steps, encounter, mora_l, flag_camp, False)
def working(stepss, totalmoral, camp, full):
    actions = []
    actions_e = []
    enc = 0
    n_steps = 0
    campspots = 0
    flagcamp = True
    per_encounter = 7
    per_tile = 1
    totalmoral += camp
    for step in stepss:
        if totalmoral < -20:
            print('Caution')
        if totalmoral < -30:
            actions.append('d')
            break
        actions.append(step)
        if step == 'b':
            totalmoral -= 3
        if step == ' ':
            totalmoral -= per_tile
        if step == 'c':
            totalmoral -= per_encounter
            totalmoral -= 1
            campspots += 1
        if step == 'x':
            totalmoral -= 1
            campspots += 1
        if step == 'n':
            totalmoral -= per_encounter
            enc += 1
        if step == 'e':
            n_steps += 1
            break
        if step == 's':
            pass
        n_steps += 1

    for moves in actions:
        if moves == 's':
            actions_e.append('Start,')
        if moves == ' ':
            actions_e.append('Normal Tile,')
        if moves == 'c':
            actions_e.append('Camp tile with encounter,')
        if moves == 'j':
            actions_e.append('Camp tile no encounter,')
        if moves == 'n':
            actions_e.append('encounter,')
        if moves == 'b':
            actions_e.append('move to beginning,')
        if moves == 'e':
            actions_e.append('exit\n')
        if moves == 'd':
            actions_e.append('ded lol\n')

    if full is False:
        return '\nMoral Left:{}\nSteps taken:{}\nEncounters:{}\nCamp done:{}'.format(totalmoral, n_steps, enc, flagcamp)
    else:
        return '\nMoral Left:{}\nSteps taken:{}\nEncounters:{}\nCamp done:{}\nActions;{}'.format(totalmoral, n_steps,
                                                                                                 enc, flagcamp,
                                                                                                 actions_e)



print('Enter The path one tile at a time')
exception = 'Moral is consumed at Fights that occur on tiles where camping is unavailable ' \
            '(i.e. not at corners or intersections)\nDo remember to go to beginning to exit'
total_moral = 70
print(exception)
print('Journal:\ns to start\n\' \' for normal\nc for camp\nx for camp but no fight\nn for encounter\n'
      'b for return to beginning\ne to exit')
mora_l = input('Camp Moral:')
mora_l = int(mora_l)
steps = input('Enter the steps\n')
print(working(steps, total_moral, mora_l, True))
# print(len(actions))