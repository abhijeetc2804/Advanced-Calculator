from stack import Stack
class SimpleCalculator:
	def __init__(self):
		self.string=""
		self.history=[]
	
	def evaluate_expression(self,input_expression):
		self.string=input_expression
		ls=list(self.string)
		for _ in ls:
			if _==" ":
				ls.remove(_)
				
		n=len(ls)
		l1=["/","*","+","-"]
		a=True
		c=0
		for i in range(n):
			if ls[i] in l1:
				c+=1
				if i==0 or i==n-1:
					a=False
				elif ls[i+1] in l1 or ls[i-1] in l1:
					a=False
				elif ls[i]=="/" and ls[i+1]=="0":
					a=False
		if c!=1:
			a=False
		if a==False:
			(self.history).append((self.string,"Error"))
			return("Error")
		else:
			for i in range(n):
				if ls[i] in l1:
					a=""
					for x in ls[:i]:
						a+=str(x)
					b=""
					for x in ls[i+1:]:
						b+=str(x)
					a=float(a)
					b=float(b)
					if ls[i]=="/":
						(self.history).append((self.string,a/b))
						return(a/b)
					elif ls[i]=="*":
						(self.history).append((self.string,float(a*b)))
						return(a*b)
					elif ls[i]=="+":
						(self.history).append((self.string,float(a+b)))
						return(a+b)
					elif ls[i]=="-":
						(self.history).append((self.string,float(a-b)))
						return(a-b)
	def get_history(self):
	    return (self.history)[::-1]
