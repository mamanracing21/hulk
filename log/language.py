from xyz import *
from romz.banner import Banner

class bahasa:
	
	def __init__(self):
		self.indo = [] 
		self.english = []
		Banner().logo2()
		
		tulis(Panel(f"""{Te} {U}•{K} 01 {O}Bahasa/Language Indonesian
 {U}•{K} 02 {O}Language/Bahasa English
 {U}•{M} 00 {O}Keluar/Logout""",
		title = f'{Te}{M}[ {H}Language/Bahasa {M}]',style='#FF0022'))
		rom = input('%s╰─ %sSelect/Pilih %s> %s'%(p,o,m,k))
		if rom in['']:
			exit()
		elif rom in['1','01']:
			kentod = [
				"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
				"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
				"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
				"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
				"√"
			]
			for ci in kentod:
				sys.stdout.write(f'\r{p}╰─{o} mohon tunggu sebentar ... {h}{ci}');sys.stdout.flush();jeda(0.06)
			os.system("rm -rf data/indo.txt && rm -rf data/english.txt")
			self.indo = ("bahasa_indonesia")
			open("data/indo.txt","w").write(self.indo)
			open("data/english.txt","w").write(self.indo)
			self.jalan (f'\n{p}╰─{o} menggunakan bahasa Indonesia');jeda(2)
			tulis(Panel(f'{Te} {U}•{O} jalankan ulang perintah nya ketik{M}:\n{P} - {H}python bff-2.py',
			style='#FF0022'));exit()
		elif rom in['2','02']:
			kentod = [
				"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
				"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
				"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
				"🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚",
				"√"
			]
			for ci in kentod:
				sys.stdout.write(f'\r{p}╰─{o} please wait ... {h}{ci}');sys.stdout.flush();jeda(0.06)
			os.system("rm -rf data/indo.txt && rm -rf data/english.txt")
			self.english = ("bahasa_inggris")
			open("data/english.txt","w").write(self.english)
			open("data/indo.txt","w").write(self.english)
			self.jalan (f'\n{p}╰─{o} use language English');jeda(2)
			tulis(Panel(f'{Te} {U}•{O} rerun the command type{M}:\n{P} - {H}python bff-2.py',
			style='#FF0022'));exit()
		elif rom in['0','00']:
			exit()
		else:
			exit()
			
	#--- JALAN
	def jalan(self,keliling):
		for mau in keliling + '\n':
			sys.stdout.write(mau)
			sys.stdout.flush();jeda(0.03)