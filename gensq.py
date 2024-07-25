from utils.cmd_gensq import cmd_inp, cmd_outv
from utils.cmd_info import info_cli

print(f'{info_cli['name']} [version: {info_cli['version']}]')
print(f'by {info_cli['creator']}')
print()
print('Use "gensq help" to show all commands')

ask_command = ''

while not ask_command == 'gensq quit':
    ask_command = cmd_inp()
    cmd_outv(ask_command)