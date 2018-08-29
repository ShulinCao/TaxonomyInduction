import multiprocessing as mp
from multiprocessing import Pool
from collections import defaultdict
import sys
import json
import pickle
reload(sys)
sys.setdefaultencoding('utf8')
fin=open('plural.txt','r')
fin_head=open('plural_head.txt','r')
contents=fin.readlines()
fin.close()
heads=fin_head.readlines()
fin_head.close()
f1=open('sup.txt','w')
f2=open('sup_head.txt','w')
f3=open('unsup.txt','w')
f4=open('unsup_head.txt','w')
def mycallback(x):
        f1.write(str(x[0])+'\n')
#	f1.flush()
        f2.write(str(x[1])+'\n')
#	f2.flush()
        f3.write(str(x[2])+'\n')
#	f3.flush()
        f4.write(str(x[3])+'\n')
#	f4.flush()
def find(x,y):
	cnt=0
	for head in heads:
		head=head.strip().split('\t')
		if head[0]!=x:
			continue
		for i in range(1,len(head)):
			if head[i]==y:
				cnt+=1
	return cnt

def process_line(d,i):
	content=contents[i]
	head=heads[i]
	content=content.strip().split('\t')
	head=head.strip().split('\t')
	sup=content[0]+'\t'
	sup_head=head[0]+'\t'
	unsup=content[0]+'\t'
	unsup_head=head[0]+'\t'	
	
	cnt=[]
	cnt.append(-1)
	for i in range(1,len(content)):
		tmp=head[0]+'\t'+head[i]
		if not tmp in d:	
			d[tmp]=find(head[0],head[i])
		cnt.append(d[tmp])
	mx=-1
	for i in range(1,len(content)):
		if cnt[i]>mx:
			mx=cnt[i]
	for i in range(1,len(content)):	
    		if mx>=5 and cnt[i]==mx:
			sup+=content[i]+'\t'
			sup_head+=head[i]+'\t'
		else:
			unsup+=content[i]+'\t'
			unsup_head+=head[i]+'\t'
	return sup,sup_head,unsup,unsup_head


if __name__ == '__main__':
    pool = Pool(mp.cpu_count())
    d=mp.Manager().dict()
    res=[pool.apply_async(process_line,(d,i)) for i in range(len(contents))]
    for i in res:
	x=i.get()
	mycallback(x)
    pool.close()
    pool.join()
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    a=open('support.pkl','wb')
    pickle.dump(dict(d),a)
    a.close()
