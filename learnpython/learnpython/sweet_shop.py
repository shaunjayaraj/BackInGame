def is_valid_input(user_input):
    if user_input < 1 or user_input > 3:
        return False
    else:
        return True

def accept_user_input():
    user_input = int(input())
    if (is_valid_input(user_input)):
        return user_input 
    else:
        return 0

def sweet_cost_lookup(sweet_number):
  cost_dictionary = {"1": 1, "2" : 1.35, "3" : 3.45}
  return cost_dictionary[str(sweet_number)]

shopping_cart_total = 0

while(True):

    welcome_msg = '''Welcome to the Haribo sweet store
    1> Hard boiled sweets  - £1
    2> Lollipops - £1.35
    3> Gummi Bear - £3.45
    
    Select a sweet by typing in the serial number'''

    print(welcome_msg)

    validated_input = accept_user_input()

    if(validated_input == 0):
        print("invalid input")
    cost_of_sweet = sweet_cost_lookup(validated_input)
    print(cost_of_sweet)
    shopping_cart_total = shopping_cart_total + cost_of_sweet
    print("Shopping cart Total so far: {}".format(shopping_cart_total))

    print("Do you want to continue y/n? :")
    continue_choice = input()
    if (continue_choice != 'y'):
      break
