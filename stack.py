class Stack:

    def __init__(self):

        self.ls=[]

        self.a=""

        self.count=0

    def push(self, item):

        self.ls = [item] + self.ls

        self.count+=1


    def peek(self):

        if self.ls==[]:

            return "Error"

        return self.ls[0]


    def pop(self):

        n=len(self.ls)

        self.count+=-1

        if n==0:

            return "Error"

        self.ls = self.ls[1:]


    def is_empty(self):

        return self.ls==[]


    def __str__(self):
        s1=""
        for x in self.ls:
            s1=s1+str(x)+str(" ")
        s2=s1[0:len(s1)-1]
        return s2
        
    def __len__(self):

        return self.count
  



