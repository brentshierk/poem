import random
#open file


def get_file_lines(filename):
    filename = open('poem.txt', 'r')
    line_list = filename.readlines()
    
    return line_list

   
        
line_list = get_file_lines('poem.txt')


def lines_printed_backwards(line_list):
    
    
    list_num = list(range(len(line_list)))

    for i in list(reversed(list_num)):
        print(f'{i + 1} {line_list[i]}')

lines_printed_backwards(line_list)

def lines_printed_random(line_list):
   
    i = 0
    while i < len(line_list):
        random_line = random.randrange(100)
        print(line_list[random_line])
        i += 1 
    
lines_printed_random(line_list)

def lines_printed_custom(lines_list):
    
    for line in lines_list:
        string = ''
        num_list = range(len(line))
        num_list = list(num_list)
        for i in num_list:
            if line[i] != ' ' and i % 2 == 0:
                string += line[i].upper()
            else:
                string += line[i]
        print(string)
        
lines_printed_custom(line_list)
    
