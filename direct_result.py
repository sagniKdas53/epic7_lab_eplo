from the_real_main_function import working
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
print(working(steps, mora_l, True))
# print(len(actions))
