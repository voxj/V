import sys
import os
import pyautogui
import random
import colorama
Fore = colorama.Fore
Style = colorama.Style
red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
reset = Style.RESET_ALL
AppID = str(random.randint(0, 999999999999999999999))
args = sys.argv
imported_modules = []
allMod = ['V.Graphics', 'colors', 'vcord', 'browser']
allModHackON = False
class V:
    def interpret(self, file):
        if allModHackON:
            imported_modules = allMod
        if file.endswith('.v') != True:
            file += '.v'
        if file == "stdin.v":
            cf = "<stdin>"
        else:
            cf = file
        if 1:
            errtype = 1
            with open(f'{AppID}.py', 'w') as tv:
                tv.write(f'import time\nimport discord\nimport webbrowser\nfrom discord.ext import commands\nimport colorama\nimport pyautogui\nimport sys\nimport os\ntrue = "true"\nfalse = "false"\nimport platform\nosver = platform.release()\naosn = platform.system()\nosn = os.name\nFore = colorama.Fore\nStyle = colorama.Style\nred = Fore.RED\nblue = Fore.BLUE\ngreen = Fore.GREEN\nreset = Style.RESET_ALL\nAppID = {AppID}\n')
                a = open(file, 'r').read()
                line_count = 0
                for line in a.splitlines():
                    line_count += 1
                    f = line.split(' ')
                    if line.endswith(';') != True:
                        if errtype == 0 or errtype == None:
                            pyautogui.alert(title='V - Error', text=f'SyntaxError in {cf} on line {line_count}: missing semicolon')
                        else:
                            print(f'{red}SyntaxError in {cf} on line {line_count}: missing semicolon{reset}')
                    line = line[0:-1]
                    if line.startswith('errtype '):
                        errtype = line[7:]
                    elif line.startswith('run '):
                        l = line[4:].split(';')
                        tv.write('\n'.join(l))
                    elif line.startswith('exec '):
                        af = line[5:]
                        tv.write(f'exec({af})\n')
                    elif line.startswith('exit'):
                        if line == 'exit' or line == 'exit ':
                            tv.write('sys.exit()\n')
                        else:
                            tv.write(f'print("{red}AppClosed: App closed with status {line[5:]}.{reset}")\nsys.exit()\n')
                    elif line.startswith('browser.open '):
                        tv.write(f'webbrowser.open({line[13:]})')
                    elif line.startswith('eval '):
                        af = line[5:]
                        tv.write(f'eval({af})\n')
                    elif line.startswith('count'):
                        tv.write(f"for i in range({int(line[6:])+1}):\n\tprint(i)\n\ti += 1\n")
                    elif line.startswith('vcord.Bot.add_command '):
                        lenin = eval(line[22:])
                        name = lenin['name']
                        reply = lenin['reply']
                        tv.write(f"""\n@client.command()\nasync def {name}(ctx):\n\tawait ctx.send("{reply}")\n""")
                    elif line.startswith('vcord.Bot.AddErrorMessage '):
                        if 'vcord' in imported_modules:
                            print(f'{red}DeprecatedFunctionWarning: AddErrorMessage doesn\'t have any use in vCord.Bot.{reset}')
                            lenin = line[26:]
                            tv.write(f'@client.event\nasync def on_message_error(ctx, error):\n\tawait ctx.send({lenin})\n')
                        else:
                            print(f'{red}NameError in {cf} on line {line_count}: name/function {line} not defined.{reset}')
                    elif line.startswith('vcord.Bot.run --token: '):
                        if 'vcord' in imported_modules:
                            token=line[23:]
                        else:
                            print(f'{red}NameError in {cf} on line {line_count}: name/function {line} not defined.{reset}')
                    elif line.startswith('vcord.Bot.client '):
                        if 'vcord' in imported_modules:
                            lenin = eval(line[17:])
                            tv.write(f'client = commands.Bot(command_prefix="{lenin['prefix']}", intents=discord.Intents.all())\n')
                        else:
                            print(f'{red}NameError in {cf} on line {line_count}: name/function {line} not defined.{reset}')
                    elif line == 'vcord.Bot.run --start':
                        if 'vcord' in imported_modules:
                            tv.write(f'\nclient.run({token})')
                        else:
                            print(f'{red}NameError in {cf} on line {line_count}: name/function {line} not defined.{reset}')
                    elif line == ('colors'):
                        if 'colors' in imported_modules:
                            print('Colors! Yay!')
                        else:
                            print(f'{red}NameError in {cf} on line {line_count}: name/function {line} not defined.{reset}')
                    elif line.startswith('import '):
                        impMode = line[7:]
                        if impMode in allMod:
                            imported_modules.append(impMode)
                        else:
                            print(f'{red}ModuleNotFoundError in {cf} on line {line_count}: module {impMode} not found.{reset}')
                    elif line.startswith('printl') or line.startswith('   printl'):
                        try:
                            if line.startswith('   printl'):
                                tv.write(f'print({line.replace("    printl ", "")})\n')
                            else:
                                tv.write(f'print({line.replace("printl ", "")})\n')
                        except Exception as e:
                            print(f'An error occured while compiling: {e}')
                    elif line.startswith('V.Graphics.alert') or line.startswith('V.Graphics.error'):
                        if 'V.Graphics' in imported_modules:
                            title = line.index('.title(')
                            text = line.index('.text(')
                            text_start = text + len('.text(')
                            text_end = line.index(')', text_start)
                            title_start = title + len('.title(')
                            title_end = line.index(')', title_start)
                            text_value = line[text_start:text_end]
                            title_value = line[title_start:title_end]
                            text_value = text_value.replace('(', '').replace(')', '')
                            title_value = title_value.replace('(', '').replace(')', '')
                            tv.write(f'pyautogui.alert(title={title_value}, text={text_value})\n')
                        else:
                            print(f'{red}NameError in {cf} on line {line_count}: name/function {line} not defined.{reset}')
                    elif line.startswith('os'):
                        if line == 'os' or line == "os ":
                            tv.write('print(os.name)\n')
                        else:
                            if line.startswith('os --run-command'):
                                if line != 'os --run-command':
                                    tv.write(f'os.system({line.replace("os --run-command ", "")})\n')
                    elif line.startswith('requesttext'):
                        if line == "requesttext":
                            tv.write('input()\n')
                        else:
                            tv.write(f"input({line[12:]})\n")
                    elif line.startswith('if'):
                        th = line.split(' ')
                        try:
                            char = line.index('"')
                        except Exception:
                            char = line.index("'")
                        cond = th[1]
                        tht = th[3].replace('"', '').replace('"', '').replace("'", "").replace("'", "")
                        replacedLine = line.replace('isnt', '!=').replace('is', '==').replace(' then', ':\n').replace('{', '').replace('}', '').replace('printl ', f'print("{line[char:].replace('"', '')}") # ')
                        replacedLine = replacedLine.replace(f'{tht} then printl ', '')
                        tv.write(f'{replacedLine}\n')
                    elif line.startswith('animate '):
                        tv.write(f'for x in {line[7:]}:\n    print(x, end=\'\')\n    sys.stdout.flush()\n    time.sleep(animspeed)\nprint()\n')
                    elif line.startswith('animation_speed '):
                        tv.write(f'animspeed = {line[16:]}\n')
                    elif line.startswith('wait'):
                        if line == "wait":
                            tv.write('print()\n')
                        else:       
                            tv.write(f'time.sleep({float(line[5:])})\n')
                    elif line.lower() == 'true':
                        tv.write('print("true")\n')
                    elif line.lower() == 'false':
                        tv.write('print("false")\n')
                    elif any(line.startswith(str(i)) for i in range(10)):
                        line = line.lstrip('0')
                        tv.write(f'\nprint({line})\n')
                    elif line.startswith('let') or line.startswith('var'):
                        if 'requesttext' in line:
                            vart = line.replace('let ', '').replace('var ', '').replace('requesttext ', f'input(') + ')\n'
                            tv.write(vart)
                        else:
                            tv.write(f'{line.replace('let ', '').replace('var ', '')}\n')
                    else:   
                        if errtype == 0:
                            pyautogui.alert(title='V - Error', text=f'NameError in {cf} on line {line_count}: name/function {line} not defined.') 
                        else:
                            print(f'{red}NameError in {cf} on line {line_count}: name/function {line} not defined.{reset}')
def run(file):
    V.interpret(self=V, file=file)
    try:
        os.system(f'py {AppID}.py') 
        os.remove(f'{AppID}.py')
    except Exception as e:
        print(f"{Fore.RED}CompilerError: {e}")
        os.remove(f'{AppID}.py')
if len(args) == 2:
    run(file=args[1])
else:
    pass
