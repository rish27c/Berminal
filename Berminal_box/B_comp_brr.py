from os import path

def data_comp()->list:
    with open(path.join(path.dirname(__file__), 'b_conf.brr'), 'r') as file:
        data=file.read()
        data_list=data.split('\n')
        return data_list

def data_process()->list:
    data_list:list=list()
    data_list_main:list=list()
    if data_comp()!=None:
        data=data_comp()
        for my_data in data:
            data_str:str=''
            for your_data in range(len(my_data)):
                if my_data[your_data]=='/':
                    if my_data[your_data+1]=='/':
                        break
                    else:
                        data_str+=my_data[your_data]
                else:
                    data_str+=my_data[your_data]
            data_list.append(data_str)
        for my_data in data_list:
            if my_data!='':
                data_list_main.append(my_data)
        return data_list_main

def data_main():
    data_list=data_process()
    if data_list!=None:
        main_data=data_not_main(data_list)
        if main_data!=None:
            return main_data
        else:
            print('Falling back to safe.brr[safe-mode]\n')

def data_not_main(data_list)->list:
    brr=True
    for data in data_list:
        data_para=data.split(); data_rejoin=''.join(data_para)
        if data_rejoin[0]=='%' and data_rejoin[1]!='%':
            data_split=data_rejoin.split('=')
            if data_split[0][-1]!='%' or len(data_split)!=2:
                print('Error! "b_conf.brr" threw an unexpected error from poorly defined variable.')
                brr=False
                break

            if data_split[0][1:-1]=='user' and data_split[1][0] in ["'", '"'] and data_split[1][0]==data_split[1][-1]:
                user=data_split[1][1:-1]
            elif data_split[0][1:-1]=='pu_default' and data_split[1] in ['False', 'True']:
                pu_default=data_split[1]
            elif data_split[0][1:-1]=='pu_toggle' and data_split[1] in ['False', 'True']:
                pu_toggle=data_split[1]
            else:
                print('Error! "b_conf.brr" threw an unexpected error due to unknown variable.')
                brr=False
                break
        elif data_rejoin[0:2]=='%%':
            data_split=data_rejoin.split(':')
            if len(data_split)!=2:
                print('Error! "b_conf.brr" threw an unexpected error due to poorly defined key.')
                brr=False
                break
            
            if data_split[0][2:]=='pass_key' and data_split[1][0] in ["'", '"'] and data_split[1][0]==data_split[1][-1]:
                pass_key=data_split[1][1:-1]
            else:
                print('Error! "b_conf.brr" has a poorly defined key which does not follow "@.brr" format.')
                brr=False
                break
        elif data_rejoin[0]=='_':
            data_split=data_rejoin.split(':')
            if len(data_split)!=2:
                print('Error! "b_conf.brr" threw an invalid call.')
                brr=False
                break

            if data_split[0][1:]=='start_line' and data_split[1][0]=='(' and data_split[1][-1]==')' and data_split[1][1] in ["'", '"'] and data_split[1][1]==data_split[1][-2]:
                start_line=data_split[1][2:-2]
            elif data_split[0][1:]=='end_line' and data_split[1][0]=='(' and data_split[1][-1]==')' and data_split[1][1] in ["'", '"'] and data_split[1][1]==data_split[1][-2]:
                end_line=data_split[1][2:-2]
            else:
                print('Error! "b_conf.brr" threw a poor call.')
                brr=False
                break
        else:
            print('Error! "b_conf.brr" threw an invalid value syntax.')
            brr=False
            break
    if brr:
        return [user, pu_default, pu_toggle, pass_key, start_line, end_line]