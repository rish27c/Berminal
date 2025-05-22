try:
    from Berminal_box import Berminal
except:
    raise Exception
    print('It seems that the Berminal is unable to enter backup-mode.')
    print('Entering Emergency recovery mode...')
    import os
    import shutil
    try:
        try:
            print('Recovering file...')
            url='https://github.com/rish27c/Berminal.git'
            os.system(f'git clone {url}')
            shutil.move(os.path.join(os.path.join(os.path.dirname(__file__), 'Berminal'), 'Berminal_box'), os.path.join(os.path.dirname(__file__), 'Berminal_recovery'))
            shutil.rmtree(os.path.join(os.path.join(os.path.dirname(__file__), 'Berminal')))
            shutil.move(os.path.join(os.path.dirname(__file__), 'Berminal_recovery'), os.path.join(os.path.dirname(__file__), 'Berminal'))
        except:
            shutil.rmtree(os.path.join(os.path.join(os.path.dirname(__file__), 'Berminal_box')))
            print('Recovering file...')
            url='https://github.com/rish27c/Berminal.git'
            os.system(f'git clone {url}')
            shutil.move(os.path.join(os.path.join(os.path.dirname(__file__), 'Berminal'), 'Berminal_box'), os.path.join(os.path.dirname(__file__), 'Berminal_recovery'))
            shutil.rmtree(os.path.join(os.path.join(os.path.dirname(__file__), 'Berminal')))
            shutil.move(os.path.join(os.path.dirname(__file__), 'Berminal_recovery'), os.path.join(os.path.dirname(__file__), 'Berminal'))
    except:
        print('Berminal(Emergency Recovery)>>Error!! Please install -git manually.')