import re
def main():
	for i in range(1,179):
		rpath = "./traintxt/"+str(i) + ".txt"
		file = open(rpath,'r', encoding="utf-8")
		txt = file.read()
		txt = txt.replace('万方数据','')
		pattern = re.compile(r'[0-9a-zA-Z\u4e00-\u9fa5\s\·\~\！\@\#\￥\%\……\&\*\（\）\——\-\+\=\【\】\{\}\、\|\；\‘\’\：\“\”\《\》\？\，\。\、\`\~\!\#\$\%\^\&\*\(\)\_\[\]{\}\\\|\;\'\'\:\"\"\,\.\/\<\>\?\/\±\=\<\>\#\μ\℃\%\×\κ\α\[\]\-\β\÷\‰\Ω\∶\≤\∑]')
		unChEn = pattern.sub("",txt)
		# pattern = re.compile(f'[^\u4e00-\u9fa5]')
		# ch = pattern.sub("",txt)
		# if ch == "":
		# 	print(i)
		out = open("./nonChEn.txt",'a',encoding = 'utf-8')
		out.write(unChEn)
		out.close()
 
 
 
if __name__ == "__main__":
    main()