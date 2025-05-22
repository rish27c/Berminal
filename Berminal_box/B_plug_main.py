from os import path
from os import remove as rm
import B_comp_brr as blug
from getpass import getpass
import bcrypt

def default_berminal(instruction)->None:
    if instruction[0]=='build':
        if len(instruction)==1:
            try:
                with open(path.join(path.dirname(__file__), 'b_conf.brr'), 'r') as file:
                    print('Error: "b_conf.brr" file already exist.')
            except:
                with open(path.join(path.dirname(__file__), 'b_conf.brr'), 'w') as file:
                    data=file.write('//Berminal-config\n\n%user%="user"\n%pu_default%=False\n%pu_toggle%=False\n%%pass_key: ""\n\n//Configurations\n_start_line: ("")\n_end_line: ("")')
                    return True
        elif len(instruction)>1 and instruction[1]=='->redo':
            if len(instruction)==2:
                try:
                    with open(path.join(path.dirname(__file__), 'b_conf.brr'), 'r') as file:
                        None
                    rm(path.join(path.dirname(__file__), 'b_conf.brr'))
                    with open(path.join(path.dirname(__file__), 'b_conf.brr'), 'w') as file:
                        data=file.write('//Berminal-config\n\n%user%="user"\n%pu_default%=False\n%pu_toggle%=False\n%%pass_key: ""\n\n//Configurations\n_start_line: ("")\n_end_line: ("")')
                        return True
                except:
                    print('Error!: redo-> Could not find vonf file for rebuild.')
            elif len(instruction)==3 and instruction[2]=='-force':
                try:
                    with open(path.join(path.dirname(__file__), 'b_conf.brr'), 'r') as file:
                        None
                    rm(path.join(path.dirname(__file__), 'b_conf.brr'))
                    with open(path.join(path.dirname(__file__), 'b_conf.brr'), 'w') as file:
                        data=file.write('//Berminal-config\n\n%user%="user"\n%pu_default%=False\n%pu_toggle%=False\n%%pass_key: ""\n\n//Configurations\n_start_line: ("")\n_end_line: ("")')
                        return True
                except:
                    print('Error!: redo-> Could not find vonf file for rebuild.\nForcing rebuild...')
                    with open(path.join(path.dirname(__file__), 'b_conf.brr'), 'w') as file:
                        data=file.write('//Berminal-config\n\n%user%="user"\n%pu_default%=False\n%pu_toggle%=False\n%%pass_key: ""\n\n//Configurations\n_start_line: ("")\n_end_line: ("")')
                        return True
            else:
                print('redo::Command->Not found->_return:4;')
        else:
            print('Command not found.')
    elif instruction[0]=='easy-manual':
        if len(instruction)==2 and instruction[1]=='build':
            try:
                with open(path.join(path.dirname(__file__), 'b_conf.brr'), 'r') as file:
                    print('build<-->easy-manual::Error! Conf file already exist.')
            except:
                pass_key=''
                user=input('%User%==')
                pu_default=input('%pu_default%==')
                pu_toggle=input('%pu_toggle%==')
                pass_key_p=getpass('%%passkey::')
                pass_key_n=getpass('Retype||%%passkey::')
                if pass_key_n==pass_key_p and pass_key_n!='':
                    pass_key=bcrypt.hashpw(pass_key_n.encode(), bcrypt.gensalt())
                    with open(path.join(path.dirname(__file__), 'b_conf.brr'), 'w') as file:
                        data=file.write(f'//Berminal-config\n\n%user%={user}\n%pu_default%={pu_default}\n%pu_toggle%={pu_toggle}\n%%pass_key: "{pass_key}"\n\n//Configurations\n_start_line: ("")\n_end_line: ("")')
                else:
                    print('Key mismatch!')
        else:
            print('easy-manual<-->build::incorrect arguement.')
    else:
        print('berminal(backup): No value is returned by berminal')

def default(quote)->None: #For basic berminal interference
    err=True
    try:
        if err:
            data=blug.data_main()
        if data!=None:
            return data
        else:
            err=False
            while err!=True:
                if quote!=None:
                    print(quote)
                    quote=None
                default_berminal_instruction=input('B-default||&user%[]#>>')
                command_para=default_berminal_instruction.split()
                err=default_berminal(command_para)
    except:
        err=False
        while err!=True:
            if quote!=None:
                print(quote)
                quote=None
            default_berminal_instruction=input('B-default||&user%[]#>>')
            command_para=default_berminal_instruction.split()
            err=default_berminal(command_para)