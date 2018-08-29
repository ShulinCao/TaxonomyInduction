import multiprocessing as mp
import sys
reload(sys)
sys.setdefaultencoding('utf8')
pre_path='debug/'
cat_=open('cat.txt','r')
cat=cat_.readlines()
cat_.close()
cat_head_=open('cat_head.txt','r')
cat_head=cat_head_.readlines()
cat_head_.close()
same=open('same.txt','w')
s_head=open('same_head.txt','w')
dif=open('dif.txt','w')
d_head=open('dif_head.txt','w')
def same_head(i):
	content=cat[i].strip().split('\t')
	heads=cat_head[i].strip().split('\t')
	if len(content)!=len(heads):
		print "error"
	res_s=''
	res_d=''
	head_s=''
	head_d=''
	res_s+=content[0]+'\t'
	res_d+=content[0]+'\t'
	head_s+=heads[0]+'\t'
	head_d+=heads[0]+'\t'
	for i in range(1,len(content)):
		if heads[i]==heads[0]:
			res_s+=content[i]+'\t'
			head_s+=heads[i]+'\t'
		else:
			res_d+=content[i]+'\t'
			head_d+=heads[i]+'\t'
	return res_s,res_d,head_s,head_d
		

	


if __name__=="__main__":
	ps=mp.cpu_count()
        p=mp.Pool(ps)
        res=[p.apply_async(same_head, (i,)) for i in range(len(cat))]
	for i in res:
		i=i.get()
		same.write(str(i[0])+'\n')
		dif.write(str(i[1])+'\n')
		s_head.write(str(i[2])+'\n')
		d_head.write(str(i[3])+'\n')
	same.close()
	dif.close()
	s_head.close()
	d_head.close()
