import sys
import multiprocessing as mp
import numpy as np
import pickle
reload(sys)
sys.setdefaultencoding('utf8')
f=open('unsup_head.txt','r')
lines = f.readlines()
print len(lines)
f.close()
f=open('unsup.txt','r')
contents = f.readlines()
print len(contents)
f.close()
f=open('id.pkl','r')
id = pickle.load(f)
f.close()
print "start reading tsim"
f=open('tsim.pkl','r')
tsim = pickle.load(f)
f.close()
print "end"
fsim_h = open('sim_head.txt','w')
fsim = open('sim.txt','w')
funsim_h = open('unsim_head.txt','w')
funsim = open('unsim.txt','w')
def get_sim(x,y):
	x = id[x]
	y = id[y]
	tmp = str(x)+'\t'+str(y)
	return tsim[tmp]
def process_line(i):
	T=0.5
	line = lines[i]
	content = contents[i]
	line = line.strip().split('\t')
	content = content.strip().split('\t')
	sim_head = line[0]+'\t'
	sim = content[0]+'\t'
	unsim_head = line[0]+'\t'
	unsim = content[0]+'\t'
	ans = [0.0]
	for i in range(1,len(line)):
		tmp = get_sim(line[0],line[i])
		ans.append(tmp)
	mmax=0.0
	for i in range(1,len(line)):
		if ans[i]>mmax:
			mmax=ans[i]
	for i in range(1,len(line)):
		if ans[i]==mmax and mmax>=T:
			sim_head += line[i]+'\t'
			sim += content[i]+'\t'
		else:
			unsim_head += line[i]+'\t'
			unsim += content[i] + '\t'
	return sim_head, sim, unsim_head, unsim
if __name__=="__main__":
	p = mp.Pool(mp.cpu_count())
	res = [p.apply_async(process_line,(i,)) for i in range(len(lines))]
	for i in res:
		i=i.get()
		fsim_h.write(i[0]+'\n')
		fsim.write(i[1]+'\n')
		funsim_h.write(i[2]+'\n')
		funsim.write(i[3]+'\n')
	fsim_h.close()
	fsim.close()
	funsim.close()
	funsim_h.close()
