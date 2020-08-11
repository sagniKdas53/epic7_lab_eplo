# (steps, totalmoral, campspots, n_steps, encounter, mora_l, flag_camp, False)
def working(stepss, camp, full):
    assert type(stepss) == str, "Path must be entered as a string"
    assert type(camp) == int, "It can either be an integer"
    assert type(full) == bool, "It can either be True or False"
    actions = []
    actions_e = []
    enc = 0
    n_steps = 0
    campspots = 0
    flagcamp = True
    per_encounter = 7
    per_tile = 1
    totalmoral = 70
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
# print(working('s   c n x   n n n  n cnb   x n   n x  n  n  cn', 70, 40, False))
# print(working('s   c n x   n n n  n cnb   x n   n x  n  n  cn', 70, 40, True))
