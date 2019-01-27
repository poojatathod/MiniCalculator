import sys

class calculator:
    def __init__(self):
        self.l=[]
        self.prev=0
    
    def Input(self):
        ip=raw_input().replace(" ","")
        if not ip:
            print("Invalid Input: empty strings are not allowed.")
            self.cal()
        if ip.lower()=="exit":
            sys.exit() 
        self.TakeInput(ip)
    
    def TakeInput(self,string):
        str1=""
        c=0
        li=[]
        for s in string:
            if s.isdigit() or s==".":
                if c>0:
                    li.append(str1)
                    c=0
                    str1=""
                str1+=s
            else:
                if c==0:
                    if str1 != "":
                        li.append(str1)
                        str1=""
                if s in ["+","-","*","/","%"]:
                    str1+=s
                    c+=1
        li.append(str1)
        self.l = li

    def cal(self):
            self.Input()
            if self.l[0] not in ["+","-","*","/","%"]:
                res=""
            else:
                res=str(self.prev)
            for i in self.l:
                res+=i
            x=eval(res)
            self.prev=x
            print x
            self.cal()
                
if __name__=="__main__":
        t=calculator()
        t.cal()
