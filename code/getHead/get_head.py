#coding=utf-8
from stanfordcorenlp import StanfordCoreNLP
from nltk import word_tokenize
import multiprocessing as mp
import sys
reload(sys)
sys.setdefaultencoding('utf8')
nlp = StanfordCoreNLP('http://127.0.0.1', port=9003)
fin=open('cat.txt','r')
fout=open('cat_head.txt','w')
def get_head_word(line):
    dep_parse = nlp.dependency_parse(line)
    text = nlp.word_tokenize(line)
    head = ''
    if len(dep_parse) == 0:
        return head
    elif (len(dep_parse[0]) > 2) and (dep_parse[0][0] == u'ROOT') and len(text) > 0:
        head = text[dep_parse[0][2] - 1]
    return head

def process_line(line):
	content=line.strip().split('\t')
	result = ''
	for i in content:
		i=i.lower()
		i=get_head_word(i)
		result+=i+'\t'
	return result
if __name__=="__main__":
	fin=open('cat.txt','r')
	fout=open('cat_head.txt','w')
	lines=fin.readlines()
	ps=mp.cpu_count()
	p=mp.Pool(ps)
	res=[p.apply_async(process_line, (line,)) for line in lines]
	for i in res:
		fout.write(str(i.get())+'\n')
	fin.close()
	fout.close()

