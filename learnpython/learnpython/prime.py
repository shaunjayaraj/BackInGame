def add_to_list_if_number_is_prime(max_candidate):
    prime_numbers = []
    
    for candidate_number in range(1, max_candidate + 1, 1):
        is_prime_flag = True
        for prime_number in prime_numbers:
            if(prime_number > 1 and candidate_number > 1):
                if((candidate_number % prime_number) == 0):
                    is_prime_flag = False
        if (is_prime_flag == True):
            prime_numbers.append(candidate_number)
    
    return prime_numbers


