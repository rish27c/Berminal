from os import remove as rm
from os import path
from os import listdir
from getpass import getpass

def perr(cmd, data):
    if cmd[0]=='pu':
        cmd=cmd[1::]
    pu_berr(cmd, data)

def pu_berr(cmd, data):
    if cmd[0]=='rebuild':
        if len(cmd)==1:
            print('WARNING! You are about to rebuild data. This may cause data structure instablity.')
            yn=str.lower(input('Are you sure?[y/n]: '))
            if yn=='y':
                user='"' + data[0] + '"'
                pu_default=data[1]
                pu_toggle=data[2]
                pass_key_b=data[3]
                start_line='"' + data[4] + '"'
                end_line='"' + data[5] + '"'
                rm(path.join(path.dirname(__file__), 'b_conf.brr'))
                with open(path.join(path.dirname(__file__), 'b_conf.brr'), 'w') as file:
                    file.write(f'//Berminal-config\n\n%user%={user}\n%pu_default%={pu_default}\n%pu_toggle%={pu_toggle}\n%%pass_key: "{pass_key}"\n\n//Configurations\n_start_line: ("{start_line}")\n_end_line: ("{end_line}")')
                print('rebuild: Success')
            else:
                print('Cancelling...')
        elif len(cmd)==2 and cmd[1]=='-anew':
            print('Warning! You are about to erase stored data.')
            yn=str.lower(input('Are you sure?[y/n]: '))
            if yn=='y':
                rm(path.join(path.dirname(__file__), 'b_conf.brr'))
                with open(path.join(path.dirname(__file__), 'b_conf.brr'), 'w') as file:
                    file.write('//Berminal-config\n\n%user%="user"\n%pu_default%=False\n%pu_toggle%=False\n%%pass_key: ""\n\n//Configurations\n_start_line: ("")\n_end_line: ("")')
                print('rebuild: Success| Status: New')
        else:
            print('rebuild: invalid function')
    elif cmd[0]=='update' and cmd[1]=='conf':
        user='"' + data[0] + '"'
        pu_default=data[1]
        pu_toggle=data[2]
        pass_key_b=data[3]
        start_line='"' + data[4] + '"'
        end_line='"' + data[5] + '"'
        if len(cmd)==3 and cmd[2]=='all':
            user=input('%User%==')
            pu_default=input('%pu_default%==')
            pu_toggle=input('%pu_toggle%==')
            start_line=input('_start_line:()::')
            end_line=input('_end_line:()::')
            pass_key=getpass('Enter (old) key:')
            if pass_key_b!='':
                if bcrypt.checkpw(pass_key.encode(), pass_key_b):
                    pass_key_p=getpass('Enter (new) key:')
                    pass_key_n=getpass('Retype^^ Enter (new) key:')
                    if pass_key_n==pass_key_p and pass_key_n!='':
                        pass_key=bcrypt.hashpw(pass_key_n.encode(), bcrypt.gensalt())
                    else:
                        print('Key mismatch')
                else:
                    print('Incorrect password')
            else:
                pass_key_p=getpass('Enter (new) key:')
                pass_key_n=getpass('Retype^^ Enter (new) key:')
                if pass_key_n==pass_key_p and pass_key_n!='':
                    pass_key=bcrypt.hashpw(pass_key_n.encode(), bcrypt.gensalt())
                elif pass_key_n=='':
                    pass_key=''
                else:
                    print('Key mismatch')
            with open(path.join(path.dirname(__file__), 'b_conf.brr'), 'w') as file:
                file.write(f'//Berminal-config\n\n%user%={user}\n%pu_default%={pu_default}\n%pu_toggle%={pu_toggle}\n%%pass_key: "{pass_key}"\n\n//Configurations\n_start_line: ({start_line})\n_end_line: ({end_line})')
        elif len(cmd)>2:
            if 'key' in cmd:
                cmd.remove('key')
                cmd.append('key')
            for pack in cmd[2::]:
                if pack=='user':
                    user=input('%User%==')
                elif pack=='pu':
                    pu_default=input('%pu_default%==')
                elif pack=='toggle':
                    pu_toggle=input('%pu_toggle%==')
                elif pack=='sl':
                    start_line=input('_start_line:()::')
                elif pack=='el':
                    end_line=input('_end_line:()::')
                elif pack=='key':
                    pass_key=getpass('Enter (old) key:')
                    if bcrypt.checkpw(pass_key.encode(), pass_key_b):
                        pass_key_p=getpass('Enter (new) key:')
                        pass_key_n=getpass('Retype^^ Enter (new) key:')
                        if pass_key_n==pass_key_p or pass_key_n=='':
                            pass_key=pass_key_p
                        else:
                            print('Key mismatch')
                    else:
                        print('Incorrect password')
                else:
                    print(f'Invalid var: "{pack}" in conf')
            with open(path.join(path.dirname(__file__), 'b_conf.brr'), 'w') as file:
                file.write(f'//Berminal-config\n\n%user%={user}\n%pu_default%={pu_default}\n%pu_toggle%={pu_toggle}\n%%pass_key: "{pass_key_b}"\n\n//Configurations\n_start_line: ({start_line})\n_end_line: ({end_line})')
        else:
            print('Update: Conf: Invalid Command')
    elif cmd[0]=='call':
        if cmd[1]=='dir' and len(cmd)>3 and cmd[-1][-1]==';':
            pl=[]
            pth=' '.join(cmd[2:])[0:-1]
            if pth[0] in ["'", '"']:
                q=pth[0]
                pthp=pth[1:]
                q=pthp.find(q)
                pthp=pth[1:q+1]
                pth=pth[q+4:-1]
            if '"' in pth or "'" in pth or '"' in pthp or "'" in pthp:
                print('Error! Incorrect path format')
            else:
                if pthp=='list':
                    try:
                        print(listdir(pth))
                    except:
                        print('Error! Unable to access the directed folder')
                elif pthp=='r->rm->':
                    try:
                        qe=str.lower(input('Are you sure?[y/n]'))
                        if qe=='y':
                                rm(pth)
                    except:
                        print('Error! Unable to access the directed item')
    else:
        berr(cmd)

temp_dct={}

def berr(cmd):
    global temp_dct
    if cmd[0]=='arise':
        if cmd[1]=='echo' and len(cmd)>2:
            if cmd[2][0] in ['"', "'"] and cmd[2][0]==cmd[-1][-2] and cmd[-1][-1]==';':
                fr=' '.join(cmd[2::])
                print(fr[1:-2])
            else:
                print('arise: echo: Invalid berminal msg input.')
        elif cmd[1]=='echo->delay' and len(cmd)>2:
            if cmd[2][0] in ['"', "'"] and cmd[2][0]==cmd[-1][-2] and cmd[-1][-1]==';':
                fr=' '.join(cmd[2::]); fr=fr[1:-2]
                temp_mem=input('Memory-address%%')
                temp_dct.update({temp_mem:fr})
            else:
                print('arise: echo: Invalid berminal msg input.')
        elif cmd[1]=='echo->now' and len(cmd)>2 and cmd[-1][-1]==';':
            cnd=cmd[2:]; cnd=' '.join(cnd)
            for msg in cnd[0:-1]:
                print(temp_dct[msg])
        elif cmd[1]=='echo->num' and len(cmd)>2:
            if cmd[2][0] in ['"', "'"] and cmd[2][0]==cmd[-1][-2] and cmd[-1][-1]==';':
                fr=' '.join(cmd[2::]); fr=fr[1:-2]
                try:
                    int(eval(fr))
                    print(eval(fr))
                except:
                    print(f'Error! Bad input-->"{fr}"')
    else:
        print('Berminal::Command invalid.')