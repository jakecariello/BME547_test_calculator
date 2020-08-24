def interface():
    print('My Program')
    while True:
        print('Options for you:')
        print('1 - HDL')
        print('2 - LDL')
        print('9 - Quit')
        choice = input('Enter your choice: ')
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()
        elif choice == '2':
            LDL_driver()

def HDL_driver():
    # get input
    hdl = get_input('HDL')
    # check if HDL is normal
    response = check('HDL', hdl)
    # output
    output('HDL', hdl, response)

def LDL_driver():
    ldl = get_input('LDL')
    response = check('LDL', ldl)
    output('LDL', ldl, response)

def get_input(input_type: str) -> int:
    return int(input('Enter {} test result: '.format(input_type)))

def check(check_type: str, value: int) -> str:
    assert check_type in ['LDL', 'HDL'], 'Invalid check_type option!'
    if check_type == 'HDL':
        if value >= 60:
            return 'Normal'
        elif 40 <= value < 60:
            return 'Borderline Low'
        else:
            return 'Low'
    elif check_type == 'LDL':
        if value >= 190:
            return 'Very High'
        elif value in range(160, 190):
            return 'High'
        elif value in range(130, 160):
            return 'Borderline High'
        else:
            return 'Normal'

def output(output_type: str, value: int, response: str):
    print('{} value of {} is classified as \'{}\''.format(output_type, value, response))

interface()

