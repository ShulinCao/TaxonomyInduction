import inflect
import multiprocessing as mp
import sys

reload(sys)
sys.setdefaultencoding('utf8')
inflect=inflect.engine()
f=open('dif.txt','r')
contents=f.readlines()
f.close()
f_head=open('dif_head.txt','r')
heads=f_head.readlines()
f_head.close()
plu=open('plural.txt','w')
plu_head=open('plural_head.txt','w')
sin=open('singular.txt','w')
sin_head=open('singular_head.txt','w')
def process_line(i):
	content=contents[i]
	head=heads[i]
	content=content.strip().split('\t')
	head=head.strip().split('\t')
	res_p=content[0]+'\t'
	res_p_head=head[0]+'\t'
	res_s=content[0]+'\t'
	res_s_head=head[0]+'\t'
	for i in range(1,len(head)):	
		if inflect.singular_noun(head[i])==False:
			res_s+=content[i]+'\t'
			res_s_head+=head[i]+'\t'
		else:
			res_p+=content[i]+'\t'
			res_p_head+=head[i]+'\t'
	return res_p,res_p_head,res_s,res_s_head

if __name__=="__main__":
	ps=mp.cpu_count()
	p=mp.Pool(ps)
	res=[p.apply_async(process_line,(i,)) for i in range(len(contents))]
	for i in res:
		i=i.get()
		plu.write(str(i[0])+'\n')
		plu_head.write(str(i[1])+'\n')
		sin.write(str(i[2])+'\n')
		sin_head.write(str(i[3])+'\n')
	plu.close()
	plu_head.close()
	sin.close()
	sin_head.close()
		
