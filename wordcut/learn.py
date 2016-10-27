class a(object):
	"""docstring for a"""
	def __init__(self, *arg):
		super(a, self).__init__()
		if len(arg)==1:
			print(arg[0])
		if len(arg)==2:
			print(arg[0],arg[1])
		else:
			print("other")
test=a(1,2)