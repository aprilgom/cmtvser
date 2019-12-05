
from konlpy.tag import Komoran

def hyeongtae(filename):
	tokenizer = Komoran()
	tok_comments = []
	f = open(filename+".txt",'r+',-1,"utf-8")

	comments = f.read().splitlines()
	f.close()
	g = open("tok"+filename+".txt",'w',-1,"utf-8")
	for com in comments:
		tok_com_l = tokenizer.morphs(com)
		i = 0
		for tok in tok_com_l:
			g.write(tok)
			i+=1
			if i != len(tok_com_l):
				g.write(" ")
		g.write("\n")
