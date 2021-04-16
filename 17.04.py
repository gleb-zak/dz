cont = True
while cont:
    try:
        nums = [int(i) for i in input().split()]
    except ValueError:
        print('no')
        break
    oper_lst = ['+', '-', '*', '/']
    oper = input('+-*/').strip()
    while oper not in oper_lst:
        oper = input('+-*/').strip()
    if oper == '*':
        try:
            print(nums[0] * nums[1])
        except IndexError:
            print('not enough nums')
    if oper == '+':
        try:
            print(nums[0] + nums[1])
        except IndexError:
            print('not enough nums')
    if oper == '+':
        try:
            print(nums[0] - nums[1])
        except IndexError:
            print('not enough nums')
    if oper == '/':
        try:
            print(nums[0] / nums[1])
        except (ZeroDivisionError, IndexError):
            print('error')
    cont = True if input('continue ("yes/no")').lower() == 'yes' else False
