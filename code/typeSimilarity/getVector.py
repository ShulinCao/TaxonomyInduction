import pickle
d=dict()
fin=open('plural_head.txt','r')
lines=fin.readlines()
fin.close()
for line in lines:
	content=line.strip().split('\t')
	for i in range(1,len(content)):
		x=content[i]
		for j in range(1,len(content)):
			if j==i:
				continue
			y=content[j]
			tmp=x+'\t'+y
			if tmp in d:
				d[tmp]+=1
			else:
				d[tmp]=1
a=open('coocurence.pkl','w')
pickle.dump(d,a)
a.close()
		
			
			 
