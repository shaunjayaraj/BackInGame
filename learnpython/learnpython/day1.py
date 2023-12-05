import re


def process_string(inp_str):
    num = re.findall(r'\d', inp_str)
    first_number = 0
    second_number = 0 

    if(len(num) == 1):
        str_num = str(num[0])
        #print("The number: " + str_num)
        first_number = str_num[0]
        #print("First number: " + first_number)
        second_number = str_num[len(str_num)-1]

        #print("Second number: " + second_number)
    else:
        first_number = int(str(num[0])[0])
        second_number = int(str(num[len(num)-1])[0])
    
    result = str(first_number) + str(second_number)
    return int(result)

def sum_results(list_lines):
    sum_res = 0
    for line in list_lines:
        print("\nLine: " + line)
        print("Number: " + str(process_string(line)))
        sum_res = sum_res + process_string(line)
    return sum_res

def read_file_and_process_input(): 
    # Using readlines()
    file1 = open('day1_file.txt', 'r')
    Lines = file1.readlines()

    lst_lines = []
    for line in Lines:
        lst_lines.append(line)

    res = str(sum_results(lst_lines))
    print(res)
    return res

read_file_and_process_input()
#process_string("treb7uchet")