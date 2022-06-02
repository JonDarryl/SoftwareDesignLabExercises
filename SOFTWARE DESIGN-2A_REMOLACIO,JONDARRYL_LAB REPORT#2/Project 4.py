userPIN = input("Please make a digit pin:")
def verify_pin(pin):
    if pin == userPIN:
        return True
    else:
        return False

def log_in():
    tries = 0
    while tries < 3:
        pin = input('Please Enter Your Digit Pin: ')
        if verify_pin(pin):
            print("==================================")
            print("Pin accepted!")
            return True
        else:
            print("Invalid pin")
            tries += 1
    print("======================================================================")
    print("Too many incorrect tries. Calling the police. Disabling login button")
    return False

def start_menu():
    print("==================================")
    print("Welcome to the atm!")
    if log_in():
        print("Login Successful!")
start_menu()