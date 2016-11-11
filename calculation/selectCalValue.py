import calculation.calValue as cal
def poly(equation,value,cost):
	
	b=cal.calValue(['u'],value[:],cost[:]);
	a=cal.calValue(['(', '(', '1', '/', '2', ')', '*', 'a', ')'],value[:],cost[:])
	c=cal.calValue(['-1','*','s'],value[:],cost[:])

	root=cal.calValue(['(', 'b', '^', '2', ')', '-', 
		'(', '4', '*', '(', 'a', '*', 'c', ')', ')'],['a','b','c'],[a,b,c])
	print(a,":",b,":",c,"\n",root)

	if(root<0):
		return []
	elif(root==0):
		return [cal.calValue(['(', '(', '-', '1', ')', '*', 'b', 
			')', '/', '(', '2', '*', 'a', ')'],['a','b','c'],[a,b,c])]
	else :
		t=[]
		t+=[cal.calValue(['(', '(', '(', '-', '1', ')', '*', 'b', ')',
		 '-', '(', 'root', '^', '(', '1', '/', '2', ')', ')', ')', 
		 '/', '(', '2', '*', 'a', ')'],['a','b','c','root'],[a,b,c,root])]
		t+=[cal.calValue(['(', '(', '(', '-', '1', ')', '*', 'b', ')',
		 '+', '(', 'root', '^', '(', '1', '/', '2', ')', ')', ')', 
		 '/', '(', '2', '*', 'a', ')'],['a','b','c','root'],[a,b,c,root])]
		return t
def select(equation,value,cost):
	left=[]
	right=[]
	for i in equation:
		if(i=='='):
			right=equation[equation.index('=')+1:]
			break
		left+=[i]
	if(right[0][0]=='0'):
		return poly(equation[:],value[:],cost[:])
	else:
		return cal.calValue(equation[equation.index('=')+1:],value[:],cost[:])
'''
equation=['(', '(', 'u', '*', 't', ')', '+', '(', '(',
 '(', '1', '/', '2', ')', '*', 'a', ')', '*', '(',
  't', '^', '2', ')', ')', ')', '+', 's', '=', '0']
value=['u','a','s']
cost=[4,4,2]
print(select(equation[:],value[:],cost[:]))
'''
