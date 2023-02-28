
class Banner(object):
    def LoadDarkdumpBanner(self):
        try:
            from termcolor import cprint, colored
            banner = '''
     ____          _     _               
    |    \ ___ ___| |_ _| |_ _ _____ ___ 
    |  |  | .'|  _| '_| . | | |     | . |
    |____/|__,|_| |_,_|___|___|_|_|_|  _|
                                    |_|  
        Developed By: D3VIL
        https://github.com/YAHYA950/darkdump.git
              Version: 2.0
              '''

            cprint(banner, 'magenta', attrs=['bold'])

        except ImportError as ie:
            print(banner)
