def interface():
    print('My Program')
    while True:
        print('Options for you:')
        print('1 - HDL')
        print('9 - Quit')
        choice = input('Enter your choice: ')
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()

def HDL_driver():
    # get input
    hdl = get_input()
    # check if HDL is normal
    response = check_hdl(hdl)
    # output
    output(response)

interface()

