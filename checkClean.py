import re
def main():
	out = open('./wrongTxt.txt','a',encoding = 'utf-8')
	out.write('test\n')
	out.close()
	for i in range(1,91):
		rpath = "./cleantest/"+str(i) + ".txt"
		doc = open(rpath,'r',encoding = 'utf-8')
		txt = doc.read()
		pattern = re.compile(f'[^\u4e00-\u9fa5]')
		ch = pattern.sub("",txt)
		
		if not ch:
			out = open('./wrongTxt.txt','a',encoding = 'utf-8')
			out.write(str(i)+'\n')
			out.close()

	out = open('./wrongTxt.txt','a',encoding = 'utf-8')
	out.write('train\n')
	out.close()
	for i in range(1,179):
		rpath = "./traintxt/"+str(i) + ".txt"
		doc = open(rpath,'r',encoding = 'utf-8')
		txt = doc.read()
		pattern = re.compile(f'[^\u4e00-\u9fa5]')
		ch = pattern.sub("",txt)
		
		if not ch:
			out = open('./wrongTxt.txt','a',encoding = 'utf-8')
			out.write(str(i)+'\n')
			out.close()

if __name__ == '__main__':
	main()