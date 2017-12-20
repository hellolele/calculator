#!/usr/bin/env python3
import sys 
import os
args=sys.argv[1:]
index1=args.index('-c')
configfile=args[index1+1]
try:
	if os.path.exists(configfile) is False:
		raise ValueError
except:
	print('Parameter Error')
with open(configfile) as file:
	config={}
	for line in file:
		 a=line.strip()
		 a=a.split('=')
		 config[a[0]]=float(a[1])

index2=args.index('-d')
userdatafile=args[index2+1]
try:
	if os.path.exists(userdatafile) is False:
		raise ValueError
except:
	print('Parameter Error')
with open(userdatafile) as file:
	userdata={}
	for line in file:
		a=line.strip()
		a=a.split(',')
		userdata[a[0]]=float(a[1])

index3=args.index('-o')
output=args[index3+1]
try:
	if os.path.exists(output) is False:
		raise ValueError
except:
	print('Parameter Error')

if __name__=='__main__':
	users=userdata.keys()
	def shehuishui(gz):
		if gz<config['JiShuL']:
			return(config['JiShuL']*0.165)
		elif gz>config['JiShuH']:
			return(config['JiShuH']*0.165)
		else:
			return(gz*0.165)
	def Yns(gz):
		sde=gz-shehuishui(gz)-3500
		if gz<=3500 or sde<0:
			return 0
		elif gz>3500 and gz<=5000:
			return(sde*0.03)
		elif gz>5000 and gz<=8000:
			return(sde*0.1-105)
		elif gz>8000 and gz<=12500:
			return(sde*0.2-555)
		elif gz>12500 and gz<=38500:
			return(sde*0.25-1005)
		elif gz>38500 and gz<=58500:
			return(sde*0.3-2755)
		elif gz>58500 and gz<=83500:
			return(sde*0.35-5505)
		else:
			return(sde*0.45-13505)
	for user in users:
		sqgz=userdata.get(user)
		shs=shehuishui(sqgz)
		yns=Yns(sqgz)
		shgz=sqgz-shs-yns
		with open(output,'a') as Op:
			Op.write(str(user))
			Op.write(',')
			Op.write(str(int(sqgz)))
			Op.write(',')
			Op.write(str('%.2f' % shs))
			Op.write(',')
			Op.write(str('%.2f' % yns))
			Op.write(',') 
			Op.write(str('%.2f' % shgz))
			Op.write('\n')


