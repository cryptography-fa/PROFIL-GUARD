import requests, json, os, sys, hashlib
n = []
#color
class warna:
    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'

#config
def get_userid(token):
    url = "https://graph.facebook.com/me?access_token=%s" % token
    res = requests.get(url)
    info = json.loads(res.text)
    nick = info['name']
    n.append(info['name'])
    return info["id"]
def turn_shield(token, enable = True):
    uid = get_userid(token)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(uid))
    headers = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % token}
    url = "https://graph.facebook.com/graphql"
    res = requests.post(url, data = data, headers = headers)
    if '"is_shielded":true' in res.text:
        print "\033[92mProfil Guard Is Active"
    elif '"is_shielded":false' in res.text:
        print "\033[91mProfil Guard Is Non-Active"
    else:
        print "Error"
#login
print ("\033[94m[============================================]")
print ("\033[95m[ Tool    : Active/Non-Active Guard Facebook ]")
print ("\033[92m[ Author  : GUNAWAN ID                       ]")
print ("\033[93m[ Github  : https://github.com/GUNAWAN18ID   ]")
print ("\033[92m[ Team    : 407 Authentic eXploit            ]")
print ("\033[91m[ Youtube : https://youtube.com/c/GUNAWANID  ]")
print ("\033[94m[============================================]")
print ("\033[0mPlease Login To Facebook")
usr = raw_input("\033[93mUsername : \033[0m")
pwd = raw_input("\033[93mPassword : \033[0m")
API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';
data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":usr,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+usr+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
x = hashlib.new('md5')
x.update(sig)
data.update({'sig':x.hexdigest()})
req = requests.get('https://api.facebook.com/restserver.php',params=data)
gn = json.loads(req.text)
try:
	USER_TOKEN=""+gn['access_token']+""
except KeyError:
	print ('\033[91m[!] Login Failed')
	print ('\033[91m[!] Check Email or Password Again')
	exit()
#menu
print ("""\033[92m  ______                                       __ 
 /      \                                     /  |
/$$$$$$  | __    __   ______    ______    ____$$ |
$$ | _$$/ /  |  /  | /      \  /      \  /    $$ |
$$ |/    |$$ |  $$ | $$$$$$  |/$$$$$$  |/$$$$$$$ |
$$ |$$$$ |$$ |  $$ | /    $$ |$$ |  $$/ $$ |  $$ |
$$ \__$$ |$$ \__$$ |/$$$$$$$ |$$ |      $$ \__$$ |
$$    $$/ $$    $$/ $$    $$ |$$ |      $$    $$ |
 $$$$$$/   $$$$$$/   $$$$$$$/ $$/        $$$$$$$/ """)
 
print ("\033[0mMenu List")
print ("\033[93m[01] Activate")
print ("\033[93m[02] Non-Active")
act = raw_input("\033[0mSelect Number: ")
if act == ("1") or act == ("01"):
    SHIELD_ENABLE="true"
    turn_shield(USER_TOKEN, SHIELD_ENABLE)
elif act == ("2") or act == ("02"):
    SHIELD_ENABLE="false"
    turn_shield(USER_TOKEN, SHIELD_ENABLE)
else:
	print ("[!] Login Is Failed")