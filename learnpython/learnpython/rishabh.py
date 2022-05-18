num = 75
modulo_of_number = num % 2

if(modulo_of_number == 0):
    print("number is even")
else:
    print("number is odd")

list_of_numbers = [5,2,43,2312,3453,21,4,6,7,342,1,66,2,1,5,4545,75,21,1,11,1]

for number in list_of_numbers:
    modulo_of_number = number % 2
    if(modulo_of_number == 0):
        print('{0} is even'.format(number))
    else:
        print('{0} is odd'.format(number))


print(list_of_numbers[0])

studentdata = ["Kristy", "Home work forgotten", "-2", "FALSE"]

print(studentdata[3])

if (studentdata[3] == "FALSE"):
    print("Letter not sent")

print('caterpiller'[0:2])