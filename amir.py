import os
import time
os.system('git pull')
print('\033[92mInstalling Missing Moules...')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('clear')
time.sleep(3)
import bbtox
bbtox.xd()
