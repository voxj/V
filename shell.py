import compiler
import sys
import colorama
red = colorama.Fore.RED
reset = colorama.Style.RESET_ALL
while True:
    with open('stdin.v', 'w') as t:
        a = input('> ')
        if a.startswith('exit'):
            if a == 'exit;' or a == 'exit':
                exit()
            else:
                if a.endswith(';'):
                    print(f"{red}AppClosed: App closed with status {a[5:].replace(';', '')}.{reset}")
                    sys.exit()
                else:
                    print(f'{red}SyntaxError in <stdin> on line 1: missing semicolon{reset}')
        else:
            t.write(f'{a}')
    compiler.run('stdin.v')
