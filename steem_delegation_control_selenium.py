''' ################################### '''
''' ## steemit delegation control v1 	'''
''' ## by Murat Tatar # Mart 2018 		'''
''' ################################### '''


import re
import os
import time
import requests
import selenium
from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys

''' #windows ''' 
from Tkinter import *

''' # bg image ''' 
from PIL import Image, ImageTk, ImageGrab

#username = raw_input('UserName?: ')
username = 'username'


# select requests or selenium. 
# If html element code not seen in page source (ctrl+u) 
# mean, air elements created via script, we should Selenium
way = 'sel' # or 'req'


# quick exit
def e():
    exit()





# catch the word(s)
def Between(bgn,end,sentence):
	b1 = sentence.split(bgn)
	b2 = b1[1].split(end)
	ar = b2[0]
	return ar 

# get page source code (like as ctrl+u)
def GetContent(url):
	r = requests.get(url)
	incontent = r.text
	return incontent




def DelegationControl(username):

	url = 'https://steemd.com/@'+username
	cnt = GetContent(url)
	rows = re.findall('\?page=(.*?)">', cnt)
	pagenumber = len(rows)+1



	# source code has all elements, way = 'req'
	# it has not all, way = 'sel'

	if way == 'req':

		i=1
		dlgS=[]; 
		while i<pagenumber+1:
			adr = 'https://steemd.com/@'+username+'?page='+str(i)
			print adr
			inc = GetContent(url)

			dlgS.append(inc)

			i = i+1


		print '\n-------', dlgS



	elif way == 'sel':

		'''  # Call the chromedriver ''' 
		driver = web.Chrome("chromedriver.exe")

		'''  # set chromedriver window size and position ''' 
		'''  # if you get an error about the click location, ''' 
		'''  # you should set the pixel location ''' 
		driver.set_window_size(1360, 768)
		driver.set_window_position(0,0)


		i=1; dhtml='<h3>Delegation Control<h3><br>'
		while i<pagenumber+1:

			''' # Bring an Chain control address like as SteemD  '''
			adr = 'https://steemd.com/@'+username+'?page='+str(i)
			print adr
			driver.get(adr)
			driver.implicitly_wait(30)

			''' # Wait for driver done  '''
			time.sleep(3)


			'''  # find element created via javasctipt that there is NOT in Ctrl + U ''' 
			js_code = '''
			b = document.getElementsByTagName('span');
			return b
			'''

			# execute script "in" chrome driver
			spns = driver.execute_script(js_code)


			 

			x=0; sp_ar=[]
			for element in spns:
				element_text = element.text
				#print x, element_text
				sp_ar.append(element_text)
				
				if ' delegate ' in element_text: 
					print adr
					print element_text
					dhtml = dhtml + '<a href="'+adr+'">element_text</a><br>'


				x= x+1


			#print sp_ar


			i = i+1


		''' # create html ''' 
		if dhtml=='<h3>Delegation Control<h3><br>': dhtml = dhtml + 'Not found Delegation record on steemd.com'
		o = open("dhtml.html","w"); o.write(dhtml); o.close()  
    	os.startfile("dhtml.html") # open alert.html





''' ## Window functions ########## '''

def wquit():
    global delegationbox
    print "exited"    
    delegationbox.destroy()
    e()



def SendtoStrBox(sunu):    
    var.set(sunu)



def Startd():
	username = ReadUser()
	print "started"
	DelegationControl(username)



def Stopd():
    wquit()

    


def BoxPlace(event):
       
    if userBox.get() == ' UserName?':
       userBox.delete(0, "end") 
       userBox.insert(0, '  ',)
       
  
def ReadUser():
    buser = userBox.get()
    buser = buser.strip()
    return buser





''' ## Windows Creating ###################  '''

delegationbox = Tk()
delegationbox.iconbitmap(default='ico.ico')
delegationboxTitle = delegationbox.title("Steemit Delegation Control v1.0 -alfa")

en = 530; by = 345
#ekran boyutu ogren
sw = delegationbox.winfo_screenwidth()
sh = delegationbox.winfo_screenheight()
x = (sw-en)/2+7
y = (sh-by)/2-102

go = str(en) + "x" + str(by) + "+" + str(x) + "+" + str(y)

delegationbox.geometry(go) 
delegationbox["bg"] = "#15151A"
delegationbox.resizable(width=FALSE, height=FALSE)


photo = PhotoImage(file="back.gif")
label = Label(image=photo)
label.place(x=0, y=0)


userBox = Entry(delegationbox, font=("Tahoma",12), fg="#70e4b8", bg="#15151A")
userBox.place(x=130,y=60,height=38, width=145)

userBox.insert(0, ' UserName?')
userBox.bind('<FocusIn>', BoxPlace)



symimage1 = ImageTk.PhotoImage(file="start.gif")


startBtn  = Button(image=symimage1,command= Startd); startBtn.place(x=290, y=60)



var = StringVar()
var.set('Enter your UserName and click to Start. (be patient)')
strBox = Label(delegationbox, textvariable = var,
               font=("Tahoma",11), fg="#70e4b8", bg="#15151A")

strBox.place(x=0, y=305,height=37, width=530)



''' ##  bring to front '''
def bringFront():
    delegationbox.lift()
    delegationbox.attributes('-topmost', 1)
    #delegationbox.attributes('-topmost', 0)

bringFront()	


while True:
  delegationbox.mainloop()







