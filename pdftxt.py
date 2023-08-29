import fitz

def main():
	for i in range(1,91):
		rpath = "./testpdf/"+str(i) + ".pdf"
		wpath = "./testtxt/"+str(i) + ".txt"
		doc = fitz.open(rpath) # open a document
		out = open(wpath, "w",encoding = 'UTF-8') # create a text output
		for page in doc: # iterate the document pages
			txt = page.get_text()#.encoding('UTF-8') # get plain text (is in UTF-8)
			out.write(txt)# write text of pagepython
		out.close()

	for i in range(1,179):
		rpath = "./trainpdf/"+str(i) + ".pdf"
		wpath = "./traintxt/"+str(i) + ".txt"
		doc = fitz.open(rpath) # open a document
		out = open(wpath, "w",encoding = 'UTF-8') # create a text output
		for page in doc: # iterate the document pages
			txt = page.get_text()#.encoding('UTF-8') # get plain text (is in UTF-8)
			out.write(txt)# write text of page
		out.close()
if __name__ == '__main__':
	main()