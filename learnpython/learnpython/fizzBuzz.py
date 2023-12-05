def fizzBuzz(input_list):
    for number in range(0,len(input_list)):
        
        if input_list[number] % 5 ==0 and input_list[number] % 3 == 0:
            input_list[number]= 'fizzbuzz'

        elif input_list[number] % 3 == 0:
            input_list[number]= 'fizz'

        elif input_list[number] % 5 ==0:
            input_list[number]= 'buzz'

        

    return input_list
