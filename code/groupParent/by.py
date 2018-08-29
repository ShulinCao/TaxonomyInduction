import numpy
import pickle
import sys
import re
import multiprocessing as mp
reload(sys)
sys.setdefaultencoding('utf8')

f = open('unonly_head.txt','r')
lines = f.readlines()
f.close()

f = open('unonly.txt','r')
contents = f.readlines()
f.close()

f_h = open('by_head.txt','w')
f = open('by.txt','w')
fu_h = open('unby_head.txt','w')
fu = open('unby.txt','w')
def match(s):
	g = re.match(r'(.*) by (.*)',s)
	if g:
		return True
	else:
		return False
def process_line(i):
	line = lines[i]	
	line = line.strip().split('\t')
	content = contents[i]
	content = content.strip().split('\t')
	by_head = line[0] + '\t'
	by = line[0] + '\t'
	unby_head = line[0] + '\t'
	unby = line[0] + '\t'
	for j in range(1, len(line)):
		if match(content[j]):
			by_head += line[j] + '\t'
			by += content[j] + '\t'
		else:
			unby_head += line[j] + '\t'
			unby += content[j] + '\t'
	return by_head, by, unby_head, unby
if __name__ == "__main__":
	p = mp.Pool(mp.cpu_count())
	res = [p.apply_async(process_line, (i,)) for i in range(len(lines))]
	for i in res:
		i = i.get()
		f_h.write(i[0]+'\n')
		f.write(i[1]+'\n')
		fu_h.write(i[2]+'\n')
		fu.write(i[3]+'\n')
	p.close()
	p.join()
	f_h.close()
	f.close()
	fu.close()
	fu_h.close()
