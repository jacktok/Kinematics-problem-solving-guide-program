from wordFilter import Filter
a=Filter()
while True:
	x=input(" >> ")
	if x=='exit()':
		break
	if x=='save':
		a.save()
	else :
		a.add()