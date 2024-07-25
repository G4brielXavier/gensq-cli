from utils.cmd_class import seq
from utils.cmd_info import *
from random import randint

s = seq()

def cmd_inp():
    print()
    c =  input('-> ')
    return c
    
# gensq help
def gensq_help():
    for i, v in info_cmd.items():
        print()
        print(f' | < {i} > : {v}')
        print()
    return

# gensq one2one
def gensq_one2one():
    s.__clear__()
    
    try:
        
        print()
        qty = int(input(' - Qty. values: '))
        print()
        for i in range(qty):
            value = int(input(f' | Value {i} : '))
            s.__insert__(value)
        
        print()
        print(f'Generating....')
        print()
        s.__show__()
        print()
        return        
        
    except ValueError:
        print(f'gensq ValueError: the value not can be empty')
        print()
        return
    
# gensq random
def gensq_random():
    s.__clear__()
    
    try:
        
        print()
        qty = int(input(' - Qty: '))
        st_val = int(input(' - (x, y): x = '))
        en_val = int(input(f' - ({st_val}, y): y = '))
        
        print()
        print(f'was Generate a seq:')
        print(f'Elements: {qty}')
        print(f'Random values: ({st_val}, {en_val})')
        print()
        
        for i in range(qty):
            s.__insert__(randint(st_val, en_val))
        
        s.__show__()
        print()
        return
        
    except ValueError:
        
        print(f'gensq ValueError: the value not can be empty')
        print()
        return
           
# gensq range
def gensq_range():
    s.__clear__()
    
    try:
        
        print()
        rg_sq_ini = int(input(' - Begin: '))
        rg_sq_end = int(input(' - End: '))
        
        for i in range(rg_sq_ini, rg_sq_end):
            s.__insert__(i)
        
        print(f'Generating a seq({rg_sq_ini}, {rg_sq_end})')  
        print()
        s.__show__()
        print()
        
        return
        
    except ValueError:
        
        print(f'gensq ValueError: the value not can be empty')
        print()
        
        return

# gensq quit
def gensq_quit():
    return

# gensq v
def gensq_v():
    print(f'{info_cli['name']} {info_cli['version']}')
    return

# gensq creator
def gensq_creator():
    print(f'{info_cli['creator']}')
    return

# gensq date-release
def gensq_date_release():
    print(f'{info_cli['release-date']}')

# gensq help -cmd
def gensq_help_cmd():
    try:
        
        print()
        n_cmd = input(' - Command name: ')
        for i, v in info_cmd.items():
            if i == n_cmd:
                print()
                print(f' - {i} : {v}')
                return
        
        print()
        gensq_error(n_cmd)
        print()
        return
        
    except ValueError:
        
        print(f'gensq ValueError: the value not can be empty')
        print()
        
# ERROR OCORRED
def gensq_error(cmd):
    print()
    print(f'gensq CommandError: the command "{cmd}" not exist.')
    print()
        
def cmd_outv(cmd):
    c = cmd.lower()
    
    match c:
        case 'gensq help':
            gensq_help()
        case 'gensq one2one':
            gensq_one2one()
        case 'gensq range':
            gensq_range()
        case 'gensq quit':
            gensq_quit()
        case 'gensq v':
            gensq_v()
        case 'gensq creator':
            gensq_creator()
        case 'gensq release-date':
            gensq_date_release()
        case 'gensq help -cmd':
            gensq_help_cmd()
        case 'gensq random':
            gensq_random()
        case _:
            gensq_error(c)
            
        