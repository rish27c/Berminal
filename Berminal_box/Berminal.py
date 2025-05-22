def main():
    #Main terminal
    import bcrypt
    from . import bcom
    from getpass import getpass
    from . import B_plug_main as main_plug
    from os import remove as rm
    from os import path
    import sys
    from time import sleep as wait
    global main_plug
    global sys
    quote='Config failure: Falling to back-up mode.' #Message while rolling back in backup mode
    data=main_plug.default(quote)
    err=0
    for err in range(3):
        if data==None:
            print('Still has an issue. Retrying...')
            data=main_plug.default(quote)
            err+=1
        elif data!=None and err>0:
            print('Success')
            break
        else:
            break
    
    if err==3:
        print('berminal(default)||Conf:: "It seems that the berminal was unable to compile conf file.\nConf::"b_conf.brr" threw an unexpected error.')
        print('Forcefully closing berminal...', end='')
        wait(2)
        print('3...', end='')
        wait(1)
        print('2...1...')
        wait(1)
        sys.exit()
    
    user=data[0]
    if data[1]=='True':
        bl=1
    else:
        bl=0
    if data[2]=='True':
        bl2=1
    else:
        bl2=0
    pu_default=bool(bl)
    pu_toggle=bool(bl2)
    pass_key_b=data[3]
    global start_line
    start_line=data[4]
    end_line=data[5]
    print()
    if start_line!='':
        print(start_line)
    if pu_default:
        pu_default=False
        pass_key=getpass('Enter key:')
        if bcrypt.checkpw(pass_key.encode(), pass_key_b):
            pu_default=True
    toggle=False
    global default
    default=False
    while True:
        if pu_toggle:
            if pu_default:
                pu_act='pu-active'
                toggle=True
            else:
                pu_act='pu-deactive'
                toggle=False
        else:
            pu_act=''
        while True:
            try:
                cmd=input(f'Berminal||@{user}[{pu_act}]#>>')
                if cmd!='':
                    break
            except:
                None
        s_cmd=cmd.split()
        if 'pu' not in s_cmd and len(s_cmd)>1 and pu_act=='pu_active':
            s_cmd.insert(0,'pu')
        if s_cmd[0]=='pu':
            if pu_default==False:
                pass_key=getpass('Enter key:')
                if pass_key_b!='':
                    if bcrypt.checkpw(pass_key.encode(), pass_key_b):
                        pu_default=True
                    if s_cmd[1]=='-toggle' and len(s_cmd)==2 and pu_toggle:
                        toggle=True
                    elif s_cmd[1]=='r->rm-->' and len(s_cmd)==3 and s_cmd[2]=='conf':
                        rm(path.join(path.dirname(__file__), 'b_conf.brr'))
                        default=True
                        break
                    elif s_cmd[1]=='true' and len(s_cmd)==2 and pu_toggle:
                        None
                    else:
                        bcom.perr(s_cmd, data)
                else:
                    if s_cmd[1]=='-toggle' and len(s_cmd)==2 and pu_toggle:
                        toggle=True
                    elif s_cmd[1]=='r->rm-->' and len(s_cmd)==3 and s_cmd[2]=='conf':
                        rm(path.join(path.dirname(__file__), 'b_conf.brr'))
                        default=True
                        break
                    elif s_cmd[1]=='true' and len(s_cmd)==2:
                        pu_default=True
                    else:
                        bcom.perr(s_cmd, data)
            elif toggle and pu_default:
                if s_cmd[1]=='-toggle' and len(s_cmd)==2 and pu_toggle:
                    toggle=False
                elif s_cmd[1]=='r->rm-->' and len(s_cmd)==3 and s_cmd[2]=='conf':
                    rm(path.join(path.dirname(__file__), 'b_conf.brr'))
                    break
                else:
                    bcom.perr(s_cmd, data)
        elif (s_cmd[0]=='restart.brr' or s_cmd[0]=='reboot->.brr') and len(s_cmd)==1:
                        print('Exiting...')
                        print('Starting...')
                        default=True
                        break
        elif (s_cmd[0]=='stop.brr' or s_cmd[0]=='stop->.brr') and len(s_cmd)==1:
            if end_line=='':
                print('Exiting...')
            else:
                print(end_line)
            wait(1)
            sys.exit()
        elif s_cmd[0]=='exit.brr' and len(s_cmd)==1:
            print(f'@{user}->Value(\'exit.brr\') to Berminal.')
            print(f'Invalid entry to Berminal<-"Value not recieved from \'Error_Handler\' but from \'@{user}\'(%user%)"')
        elif (s_cmd[0]=='help.brr' or s_cmd[0]=='basic_arg->.brr') and len(s_cmd)==1:
            try:
                with open(path.join(path.dirname(__file__), 'basic_arg.txt'), 'r') as file:
                    help_data=file.read()
                print(help_data)
            except:
                if help_data!=None:
                    with open(path.join(path.dirname(__file__), 'basic_arg.txt'), 'w') as file:
                        file.write(help_data)
                else:
                    print('Error:: "basic_arg.txt" is missing.')
        else:
            bcom.berr(s_cmd)
err=0
while True:
    try:
        main()
    except:
        start_line=''
        if err<=3:
            err+=1
            if IndexError:
                #err-=1
                print('Berminal: Incomplete command->"Got an unexpected error of command missing arguement."')
        elif err<=6:
            print('Error_Handler||Berminal::Their was an unexpected error', end='')
            wait(1)
            print('\tSending errorVALUE to \'Error_Handler(Default)\'')
            err+=1
        elif err>8:
            wait(1)
            print('Error_Handler(Default):: return "Error_Handler||Berminal->Value(\'exit.brr\')"')
            wait(2)
            print('Berminal::Exiting...')
            wait(1)
            err_handle=str.lower(input('Call safe-mode?[y/n]'))
            if err_handle=='y':
                print('Connecting Error_Handler to safe-mode...')
                wait(3)
                print('Use "return 0;" or "return success=True;" to exit.')
                wait(1)
                while True:
                    instruction=input('Error_Handler(!!)')
                    if instruction=='return 0;' or instruction=='return success=True;':
                        ecmd=str.lower(input('Restart Berminal?[y/n]'))
                        if ecmd=='y':
                            print('Error_Handler(Default):: return "Error_Handler||Berminal->Value(\'return 0;\')->restart.brr"')
                            err=0
                            wait(2)
                            break
                        else:
                            print('Cancelling...')
                            wait(2)
                            print('Exiting "error_handle.brr"...')
                            wait(1)
                            sys.exit()
                    else:
                        si=instruction.split()
                        main_plug.default_berminal(si)
            break
        else:
            wait(2)
            print('Error_Handler(Default): return "Error was triggered without reason from \'Error_Handler||Berminal\'."')
            wait(1)
            print('Re-opening Berminal...')
            wait(1)
if default:
    start_line=backup_start_line
    default=False
    main()