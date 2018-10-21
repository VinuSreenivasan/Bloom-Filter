from count_bloom_filter import countBloomFilter
from re import search
import uuid

def getRandomString():
	return str(uuid.uuid4())

def maincode():	
	print "\nIMPLEMENTATION OF COUNTING BLOOM FILTERS"
	print "------------------------------------------\n"
	id_print=[]
	line_list=[]
	ids=[]
	paragraph_list={}
	count=1
	paragraph=" "
	idcount=0
	cbf = countBloomFilter(100,2)

	with open("testset1-input.txt") as f1:
		for line in f1:
			id_search=search(r'(?:D|T)(?:E|S)(?:V|T)[0-9]*\-MUC[0-9]\-[0-9]{4}',line)
			line=line.rstrip()
			line_list.append(line)
			if(id_search):
				id_print.append(id_search.group())
				ids.append(line)
	for i in line_list:
		temp=i.strip()
		if temp not in ids:
			if count<3:
				paragraph=paragraph + "".join(temp) + " "
		else:
			count=count+1

		if(count==3):
			cbf.addition(paragraph)
			paragraph_list[id_print[idcount]] = paragraph
			idcount=idcount+1
			count=2
			paragraph=" "

	cbf.addition(paragraph)

	print "Statistics Before Deletion:"
	print "---------------------------"
	cbf.generatefinal_statistics()
	print "\n"

	cbf.delete(paragraph_list[id_print[5]])
	cbf.delete(paragraph_list[id_print[57]])
	cbf.delete(paragraph_list[id_print[79]])
	cbf.delete(paragraph_list[id_print[92]])
	cbf.delete(paragraph_list[id_print[97]])

	for k,v in paragraph_list.items():
        	if cbf.exist(v):
           		print('{} exists in bloom filter'.format(k))
        	else:
           		print("%s article does not exist in the bloom filter" % k)

	print "\n"
	print "Results After Deletion:"
	print "-----------------------"
	cbf.generatefinal_statistics()
	cbf.clear_filter()

if __name__ == '__main__':
	maincode()
