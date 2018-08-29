import multiprocessing as mp
import numpy as np
import pickle
import sys
import inflect
reload(sys)
sys.setdefaultencoding('utf8')
inflect = inflect.engine()
f = open('all_head.txt','r')
all_head = f.readlines()
f.close()

f = open('all.txt','r')
all = f.readlines()
f.close()

f = open('cat_head.txt','r')
cat_head = f.readlines()
f.close()

f = open('cat.txt','r')
cat = f.readlines()
f.close()

only_head = open('only_head.txt','w')
only = open('only.txt','w')

def process_line(i):
	a_h = all_head[i]
	a_h = a_h.strip().split('\t')
	ans_h = a_h[0] + '\t'
	ans = a_h[0] + '\t'
	if len(a_h)>1:
		return ans_h, ans
	a = all[i]
	a = a.strip().split('\t')
	c_h = cat_head[i]
	c_h = c_h.strip().split('\t')
	c  = cat[i]
	c = c.strip().split('\t')
	s_head = []
	p_head = []
	s = []
	p = []
	for j in range(1, len(c)):
		if inflect.singular_noun(c_h[j]) == False:
			s_head.append(c_h[j])	
			s.append(c[j])
		else:
			p_head.append(c_h[j])	
			p.append(c[j])
	if len(p) == 1:
		ans_h += p_head[0]+'\t'
		ans += p[0]+'\t'
	elif len(p) == 0:
		if len(s) == 1:
			ans_h += s_head[0] + '\t'
			ans += s[0] + '\t'
	return ans_h, ans

if __name__ == "__main__":
	p = mp.Pool(mp.cpu_count())
	res = [p.apply_async(process_line, (i,)) for i in range(len(all))]	
	for i in res:
		i = i.get()	
		only_head.write(i[0]+'\n')
		only.write(i[1]+'\n')
	p.close()
	p.join()
	only_head.close()
	only.close()		
