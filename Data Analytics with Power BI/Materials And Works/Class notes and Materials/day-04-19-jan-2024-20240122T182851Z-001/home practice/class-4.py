'''import sys

vowel_list = ['a', 'e', 'i', 'o', 'u']


def find_vowel_count(user_text) :
        vowel_count = 0
        
        if user_text.isalpha :
                    for t in vowel_list :
                        vowel_count = vowel_count + user_text.count(t)

        else :
            sys.exit("Invalid Input")


        print ("total vowel  count = ", vowel_count)
    

    

if __name__=='__main__' :
        user_input_1 = input('Enter Text: ')
        my_vowel_count = find_vowel_count(user_input_1)

        print("Total Vowel Count = ", my_vowel_count)

        user_input_2 = input('Enter Text: ')
        my_vowel_count_2 = find_vowel_count(user_input_2)

        print("Total Vowel Count = ", my_vowel_count)




in_file = 'input text.txt'

f_obj = open(in_file, 'r')

for l in f_obj :
    l =l.strip()
    list_str = l.split(',')
    print(list_str)
    print('name =', list_str[0], 'number = ',list_str[1], 'email =', list_str[2] )


f_obj.close()




f_obj =open(in_file, 'r')
my_str = f_obj.read()
print(my_str)
'''
from fibonacci_sum.fibonacci_sum import fibosum
print(fibosum(5))
