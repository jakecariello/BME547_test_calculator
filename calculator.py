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
    response = check_hdl(hdl)
    # output
    output_hdl(hdl, response)

def LDL_driver():
    ldl = get_input('LDL')

def get_input(input_type: str) -> int:
    return int(input('Enter {} test result: '.format(input_type)))

def check_hdl(value: int) -> str:
    if value >= 60:
        return 'Normal'
    elif 40 <= value < 60:
        return 'Borderline Low'
    else:
        return 'Low'

def output_hdl(value: int, response: str):
    print('HDL value of {} is classified as \'{}\''.format(value, response))

interface()

