try:
    import Berminal
    Berminal.Berminal()
except:
    print('It seems that the Berminal is unable to enter backup-mode.')
    print('Entering Emergency recovery mode...')
    from os import system
    try:
        print('Recovering file...')
        system('git clone https://github.com/rish27c/Berminal.git')
    except:
        print('Please install -git manually.')