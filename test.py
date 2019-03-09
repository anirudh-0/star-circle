from math import sqrt
r=25
x,y=r,r
def dist(i,j):
	d=(i-x)**2+(j-y)**2
	d=sqrt(d)
	return d
for i in range(2*r+1):
	for j in range(2*r+1):
		if i==x and j==y:
			print("O ",end="")
		elif dist(i,j)<=r:
			print("* ",end="")
		else:
			print("  ",end="")
	print("")