import calculation as change
import selectCalValue as cal

def printE(List):
	for i in List:
		print(i,end="")
valueFind=['t']
index=4
value=['s','a','u']
cost=[100,-10,60]
equationChange=(change.getEquationChange(index,valueFind))
printE(change.getEquationOrigin(index))
print("")
printE(equationChange)
print("")
print(cal.select(equationChange,value,cost))
