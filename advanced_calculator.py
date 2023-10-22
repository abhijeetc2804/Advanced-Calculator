from stack import Stack
from simple_calculator import SimpleCalculator

class AdvancedCalculator(SimpleCalculator):
	def init(self):
		SimpleCalculator.init(self)
		self.s=""
		self.ls=[]
		self.history=[]
		
	def check_brackets(self, list_tokens):
		self.ls=list_tokens
		s1=Stack()
		s2=Stack()
		s3=Stack()
		balanced=True
		i=0
		l2=["(",")","{","}"]
		ls1=[]
		for x in self.ls:
			if x in l2:
				ls1.append(x)
			
		while(i<len(ls1) and balanced):
			if (ls1)[i]=="(":
				s1.push("(")
				s3.push("(")
			elif (not(s1.is_empty())) and ls1[i]=="{":
				balanced=False
			elif (ls1)[i]=="{":
				s2.push("{")
				s3.push("{")
			else:
				if s3.is_empty() :
					balanced=False
				elif (ls1)[i]==")":
					s1.pop()
					s3.pop()
				elif (ls1)[i]=="}":
					s2.pop()
					s3.pop()
			i+=1
		if balanced and s1.is_empty() and s2.is_empty() and s3.is_empty():
			return True 
		else:
			return False

	def evaluate_list_tokens(self, list_tokens):
		s=""
		for x in list_tokens:	
			s+=str(x)
		input_expression=s
		lst=self.infix_to_postfix(input_expression)
		c=0
		c1=0
		for x in lst:
			if type(x)==float:
				c+=1
			elif x in ["+","-","*","/"]:
				c1+=1
		if c-c1!=1:
			return "Error"
		else:
			if self.check_brackets(input_expression)==True:	
				self.s=input_expression
				try:
					l1=self.infix_to_postfix(self.s)
					ans=self.calc_postfix(l1)
					return ans
				except:
					self.s=input_expression
					
					return "Error"
			else:
				self.s=input_expression
				return "Error"

	def get_history(self):
		return self.history[::-1]


		pass
	def isdigit(self,s):
		if 48<=ord(s)<=57 or ord(s)==46:
			return True
		return False
	def tokenize(self,input_expression):
		tokens=[]
		s=input_expression
		s_new=""
		for x in s:
			if x!=" ":
				s_new+=str(x)
		s=s_new
		n=len(s)
		s1=""
		i=0
		while(i<n):
			s1=""
			if self.isdigit(s[i])==False:
				tokens.append(str(s[i]))
				s1=""
				i+=1
			else:
				if i==n-1:
					s1+=s[i]
					tokens.append(float(s1))
				else:
					s1+=str(s[i])
					j=1
					while(i+j<n and self.isdigit(s[i+j])):
						s1+=s[i+j]
						j+=1
					if s1!="":
						tokens.append(float(s1))
				i=i+j
		return tokens

	
	def infix_to_postfix(self,input_expression):
		p=input_expression
		tokens=[]
		s=input_expression
		s_new=""
		for x in s:
			if x!=" ":
				if x=="{":
					x="("
				elif x=="}":
					x=")"	
				s_new+=str(x)
		s=s_new
		n=len(s)
		s1=""
		i=0
		while(i<n):
			s1=""
			if self.isdigit(s[i])==False:
				tokens.append(str(s[i]))
				s1=""
				i+=1
			else:
				if i==n-1:
					s1+=s[i]
					tokens.append(float(s1))
				else:
					s1+=str(s[i])
					j=1
					while(i+j<n and self.isdigit(s[i+j])):
						s1+=s[i+j]
						j+=1
					if s1!="":
						tokens.append(float(s1))
				i=i+j
				
		for x in tokens:
			if x=="{":
				x="("
			elif x=="}":
				x=")"
		result_ls=[]
		operator_stack=Stack()
		operators={"/": 2, "*":2,"+":1,"-":1}
		n=len(tokens)
		for i in range(n):
			if tokens[i]=="(":
				operator_stack.push(tokens[i])
			elif tokens[i]==")":
				while((not operator_stack.is_empty()) and operator_stack.peek()!="("):
					last = operator_stack.peek()
					operator_stack.pop()
					result_ls.append(last)
				if not operator_stack.is_empty() and operator_stack.peek()=="(":
					operator_stack.pop()
			elif tokens[i] in operators:
				while not operator_stack.is_empty() and operator_stack.peek() !="(" and operators[operator_stack.peek()]>=operators[tokens[i]]:
					last=operator_stack.peek()
					operator_stack.pop()
					result_ls.append(last)
				operator_stack.push(tokens[i])
			else:
				result_ls.append(tokens[i])
		
		while operator_stack.is_empty()==False:
			y=operator_stack.peek()
			operator_stack.pop()
			result_ls.append(y)

		return result_ls

	def calc_postfix(self,l1):
		s=Stack()
		check=True
		for x in l1:
			if type(x)==float:
				s.push(x)
			else:
				a=s.peek()
				s.pop()
				b=s.peek()
				s.pop()
				if x=="+":
					ans= a+b
				elif x=="-":
					ans= b-a
				elif x=="*":
					ans= a*b
				elif x=="/":
					if a==0.0:
						check=False
					else:
						ans =b/a
				s.push(ans)
		if check==False:
			return "Error"
		return s.peek()

	def evaluate_expression(self, input_expression):
		lst=self.infix_to_postfix(input_expression)
		c=0
		c1=0
		for x in lst:
			if type(x)==float:
				c+=1
			elif x in ["+","-","*","/"]:
				c1+=1
		if c-c1!=1:
			return "Error"
		else:
			if self.check_brackets(input_expression)==True:	
				self.s=input_expression
				try:
					l1=self.infix_to_postfix(self.s)
					ans=self.calc_postfix(l1)
					self.history.append((self.s,ans))
					return ans
				except:
					self.s=input_expression
					self.history.append((self.s,"Error"))
					return "Error"
			else:
				self.s=input_expression
				self.history.append((self.s,"Error"))
				return "Error"
