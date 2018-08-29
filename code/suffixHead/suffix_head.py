import numpy as np
import pickle
import sys
import multiprocessing as mp
reload(sys)
sys.setdefaultencoding('utf8')

f = open('unby_head.txt','r')
lines = f.readlines()
f.close()

f = open('unby.txt','r')
contents = f.readlines()
f.close()

f_h = open('suffix_head.txt','w')
f = open('suffix.txt','w')
fu_h = open('unsuffix_head.txt','w')
fu = open('unsuffix.txt','w')

def process_line(i):
	line = lines[i]
	content = contents[i]
	line = line.strip().split('\t')
	content = content.strip().split('\t')
	s_h = line[0] + '\t'
	s = content[0] + '\t'
	us_h = line[0] + '\t'
	us = content[0] + '\t'
	for j in range(1, len(line)):
		if line[0].endswith(line[j]):
			s_h += line[j] + '\t'
			s += content[j] + '\t'
		else:
			us_h += line[j] + '\t'
			us += content[j] + '\t'
	return s_h, s, us_h ,us		
	
if __name__ == "__main__":
	p = mp.Pool(mp.cpu_count())
	res = [p.apply_async(process_line, (i,)) for i in range(len(lines))]
	for i in res:
		i = i.get()
		f_h.write(i[0]+'\n')
		f.write(i[1]+'\n')
		fu_h.write(i[2]+'\n')
		fu.write(i[3]+'\n')
	f_h.close()
	f.close()
	fu_h.close()
	fu.close()	


