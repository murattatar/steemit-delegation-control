''' ################################### '''
''' ## steemit delegation control v1 	'''
''' ## by Murat Tatar # Subat 2018 		'''
''' ################################### '''


import re
import time
import requests



#username = raw_input('UserName?: ')
username = 'username'



def Between(bgn,end,sentence):
	b1 = sentence.split(bgn)
	b2 = b1[1].split(end)
	ar = b2[0]
	return ar 



def GetContent(url):
	r = requests.get(url)
	incontent = r.text
	return incontent


url = 'https://steemd.com/@'+username
cnt = GetContent(url)


#betw= Between('<li><a href="/@','aria-label="Next">',cnt)
#print betw

rows = re.findall('\?page=(.*?)">', cnt)



pagenumber = len(rows)+1



i=1
dlgS=[]; 
while i<pagenumber+1:
	adr = 'https://steemd.com/@'+username+'?page='+str(i)
	print adr
	inc = GetContent(url)

	dlgS.append(inc)
	
	i = i+1


print '\n-------', dlgS
