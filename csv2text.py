import os
import re

files = os.listdir('./csv')
if not os.path.exists('./csvText'):
	os.system('mkdir csvText')

for file in files:
	txt = open(os.path.join('./csv',file),'r').read()
	# print(txt, type(txt))
	txt = re.sub('[^a-z0-9A-Z. ]', ' ' , txt)
	if len(txt)!=0:
		with open(os.path.join('./csvText',str(file.split('.')[0]+'.txt')), 'w') as f:
			f.write(txt)
		print(file, 'Done!')
	else:
		print(file, 'Empty!')