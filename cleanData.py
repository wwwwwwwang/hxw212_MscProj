import re
def cleanb(txt):
	cle = txt.replace(b' ', b'')
	cle = cle.replace(b'\n',b'')
	cle = cle.replace(b'\r\n',b'')
	return cle

def clean(txt):
	cle = txt.replace(' ', '')
	cle = cle.replace('\n','')
	cle = cle.replace('\r\n','')
	return cle

def delweird(txt,settxt):
	txt = cleanb(txt)
	txt = txt.replace(bytes('８',encoding = 'utf-8'),b'8')
	txt = txt.replace(bytes('㈨',encoding = 'utf-8'),b'9')
	txt = txt.replace(bytes('㈤',encoding = 'utf-8'),b'5')
	txt = txt.replace(bytes('６',encoding = 'utf-8'),b'6')
	txt = txt.replace(bytes('９',encoding = 'utf-8'),b'9')
	txt = txt.replace(bytes('２',encoding = 'utf-8'),b'2')
	txt = txt.replace(bytes('５',encoding = 'utf-8'),b'5')
	txt = txt.replace(bytes('㈥',encoding = 'utf-8'),b'6')
	txt = txt.replace(bytes('３',encoding = 'utf-8'),b'3')
	txt = txt.replace(bytes('㈧',encoding = 'utf-8'),b'8')
	txt = txt.replace(bytes('㈣',encoding = 'utf-8'),b'4')
	txt = txt.replace(bytes('％',encoding = 'utf-8'),b'%')
	txt = txt.replace(bytes('［',encoding = 'utf-8'),b'[')
	txt = txt.replace(bytes('＝',encoding = 'utf-8'),b'=')
	txt = txt.replace(bytes('０',encoding = 'utf-8'),b'0')
	txt = txt.replace(bytes('¾',encoding = 'utf-8'),b'')
	txt = txt.replace(bytes('²',encoding = 'utf-8'),b'^2')
	txt = txt.replace(bytes('³',encoding = 'utf-8'),b'^3')
	txt = txt.replace(bytes('＜',encoding = 'utf-8'),b'<')
	txt = txt.replace(bytes('½',encoding = 'utf-8'),b'1/2')
	txt = txt.replace(bytes('７',encoding = 'utf-8'),b'7')
	txt = txt.replace(bytes('＊',encoding = 'utf-8'),b'*')
	txt = txt.replace(bytes('４',encoding = 'utf-8'),b'4')
	txt = txt.replace(bytes('ｖ',encoding = 'utf-8'),b'v')
	txt = txt.replace(bytes('ａ',encoding = 'utf-8'),b'a')


	for s in settxt:
		txt = txt.replace(bytes(s,encoding = 'utf-8'),b'')
	
	return txt

def main():
	# for clean self
	file = open('./nonChEn.txt','rb')
	txt = file.read()
	settxt = set(list(str(txt,encoding = 'utf-8')))
	newtxt = bytes(''.join(settxt),encoding = 'utf-8')
	out = open("./wierdWord.txt",'ab')
	out.write(newtxt)
	out.close()
	for i in range(1,179):
		rpath = "./traintxt/"+str(i) + ".txt"
		wpath = "./cleantrain/"+str(i) + ".txt"
		file = open(rpath,'rb')
		txtData = file.read()
		tranTxt = delweird(txtData,settxt)
		out = open(wpath,'wb')
		out.write(tranTxt)
		out.close()
		doc = open(wpath,'r',encoding = 'utf-8')
		txt = doc.read()
		txt = clean(txt)
		en = re.findall(r'[a-zA-Z0-9\.\,\:\+\*\-]{10,1000}',txt)
		for e in en:
			 txt = txt.replace(e,"")
		out = open(wpath,'w',encoding = 'utf-8')#,encoding = 'utf-8')
		out.write(txt)
		out.close()


	# for clean txt
	# file = open('./nonChEn.txt','rb')
	# txt = file.read()
	# settxt = set(list(str(txt,encoding = 'utf-8')))
	for i in range(1,91):
		rpath = "./testtxt/"+str(i) + ".txt"
		wpath = './cleantest/'+str(i) + ".txt"
		doc = open(rpath,'rb')#,encoding = 'utf-8')
		txt = doc.read()
		txt = delweird(txt,settxt)
		out = open(wpath,'wb')#,encoding = 'utf-8')
		out.write(txt)
		out.close()
		doc = open(wpath,'r',encoding = 'utf-8')
		txt = doc.read()
		txt = clean(txt)
		en = re.findall(r'[a-zA-Z0-9\.\,\:\+\*\-]{10,1000}',txt)
		for e in en:
			 txt = txt.replace(e,"")
		out = open(wpath,'w',encoding = 'utf-8')#,encoding = 'utf-8')
		out.write(txt)
		out.close()


		

if __name__ == '__main__':
	main()