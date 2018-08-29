import numpy as np
import pickle
import sys
reload(sys)
sys.setdefaultencoding('utf8')

f = open('only.txt','r')
only = f.readlines()
f.close()

f = open('only_head.txt','r')
only_head = f.readlines()
f.close()

f = open('unsim.txt','r')
unsim = f.readlines()
f.close()

f = open('unsim_head.txt','r')
unsim_head = f.readlines()
f.close()

unonly = open('unonly.txt','w')
unonly_head = open('unonly_head.txt','w')

def process_line(i):
	o_h = only_head[i]
	o_h = o_h.strip().split('\t')
	if len(o_h) == 1:
		return unsim_head[i].strip(), unsim[i].strip()
	usim_h = unsim_head[i]
	usim_h = usim_h.strip().split('\t')
	usim = unsim[i]
	usim = usim.strip().split('\t')
	ans_h = o_h[0]+'\t'
	ans = o_h[0] + '\t'
	for j in range(1, len(usim_h)):
		if usim_h[j] != o_h[1]:
			ans_h += usim_h[j]
			ans += usim[j]
	return ans, ans_h
	
if __name__ == "__main__":
	for i in range(len(only)):
		res = process_line(i)
		unonly_head.write(res[0]+'\n')
		unonly.write(res[1]+'\n')
