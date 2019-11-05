from tkinter import *
import numpy as np

def bomb(A,x):
	mine=0
	if A[x]==1:
		mine=-1
	else:
		if x+6<35:
			if A[x+6]==1:
				mine=mine+1
		if x-6>0:
			if A[x-6]==1:
				mine=mine+1
		if (x+1)%6!=0:
			if A[x+1]==1:
				mine=mine+1
		if (x-1)%6!=5:
			if A[x-1]==1:
				mine=mine+1
	return mine
def func00(A):
	b00['state']=DISABLED
	mines=bomb(A,0)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')
	else:
		b00.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func01(A):
	b01['state']=DISABLED
	mines=bomb(A,1)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b01.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')						
def func02(A):
	b02['state']=DISABLED
	mines=bomb(A,2)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b02.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')			
def func03(A):
	b03['state']=DISABLED
	mines=bomb(A,3)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b03.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func04(A):
	b04['state']=DISABLED
	mines=bomb(A,4)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b04.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func05(A):
	b05['state']=DISABLED
	mines=bomb(A,5)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')	
	else:
		b05.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func10(A):
	b10['state']=DISABLED
	mines=bomb(A,6)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b10.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func11(A):
	b11['state']=DISABLED
	mines=bomb(A,7)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b11.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func12(A):
	b12['state']=DISABLED
	mines=bomb(A,8)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b12.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func13(A):
	b13['state']=DISABLED
	mines=bomb(A,9)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b13.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func14(A):
	b14['state']=DISABLED
	mines=bomb(A,10)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b14.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func15(A):
	b15['state']=DISABLED
	mines=bomb(A,11)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b15.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func20(A):
	b20['state']=DISABLED
	mines=bomb(A,12)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b20.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func21(A):
	b21['state']=DISABLED
	mines=bomb(A,13)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b21.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func22(A):
	b22['state']=DISABLED
	mines=bomb(A,14)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b22.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func23(A):
	b23['state']=DISABLED
	mines=bomb(A,15)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b23.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func24(A):
	b24['state']=DISABLED
	mines=bomb(A,16)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b24.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func25(A):
	b25['state']=DISABLED
	mines=bomb(A,17)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b25.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func30(A):
	b30['state']=DISABLED
	mines=bomb(A,18)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b30.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func31(A):
	b31['state']=DISABLED
	mines=bomb(A,19)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b31.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func32(A):
	b32['state']=DISABLED
	mines=bomb(A,20)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b32.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func33(A):
	b33['state']=DISABLED
	mines=bomb(A,21)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b33.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func34(A):
	b34['state']=DISABLED
	mines=bomb(A,22)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b34.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func35(A):
	b35['state']=DISABLED
	mines=bomb(A,23)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b35.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func40(A):
	b40['state']=DISABLED
	mines=bomb(A,24)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b40.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func41(A):
	b41['state']=DISABLED
	mines=bomb(A,25)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b41.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func42(A):
	b42['state']=DISABLED
	mines=bomb(A,26)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b42.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func43(A):
	b43['state']=DISABLED
	mines=bomb(A,27)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b43.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func44(A):
	b44['state']=DISABLED
	mines=bomb(A,28)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b44.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func45(A):
	b45['state']=DISABLED
	mines=bomb(A,29)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b45.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func50(A):
	b50['state']=DISABLED
	mines=bomb(A,30)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b50.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func51(A):
	b51['state']=DISABLED
	mines=bomb(A,31)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b51.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func52(A):
	b52['state']=DISABLED
	mines=bomb(A,32)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b52.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func53(A):
	b53['state']=DISABLED
	mines=bomb(A,33)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b53.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func54(A):
	b54['state']=DISABLED
	mines=bomb(A,34)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b54.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
def func55(A):
	b55['state']=DISABLED
	mines=bomb(A,35)
	global c
	global b
	global l1
	if mines==-1:
		for x in range(36):
			b[x]['state']=DISABLED
		for i in l1:
			b[i].configure(bg='red')		
	else:
		b55.configure(bg='gray',text=str(mines),fg='green')
		c=c-1
#		print(c)
		if c==0:
			for i in l1:
				b[i].configure(bg='green')
if __name__ == "__main__":
	A=[]
	c=0
	list=[]
	l1=[]
	for i in range(10):
		list.append(np.random.randint(0,36))
	for i in range(36):
		if i in list:
			A.append(1)
		else:
			A.append(0)
	for i in range(len(A)):
		if A[i]==0:
			c=c+1
		else:
			l1.append(i)
#	print(c)		
	master=Tk()
	master.title("Minesweeper")
	b00=Button(master,bg='blue',command=lambda:func00(A),height=1,width=1)
	b00.grid(row=0,column=0)
	b01=Button(master,bg='blue',command=lambda:func01(A),height=1,width=1)
	b01.grid(row=0,column=1)
	b02=Button(master,bg='blue',command=lambda:func02(A),height=1,width=1)
	b02.grid(row=0,column=2)
	b03=Button(master,bg='blue',command=lambda:func03(A),height=1,width=1)
	b03.grid(row=0,column=3)
	b04=Button(master,bg='blue',command=lambda:func04(A),height=1,width=1)
	b04.grid(row=0,column=4)
	b05=Button(master,bg='blue',command=lambda:func05(A),height=1,width=1)
	b05.grid(row=0,column=5)
	b10=Button(master,bg='blue',command=lambda:func10(A),height=1,width=1)
	b10.grid(row=1,column=0)
	b11=Button(master,bg='blue',command=lambda:func11(A),height=1,width=1)
	b11.grid(row=1,column=1)
	b12=Button(master,bg='blue',command=lambda:func12(A),height=1,width=1)
	b12.grid(row=1,column=2)
	b13=Button(master,bg='blue',command=lambda:func13(A),height=1,width=1)
	b13.grid(row=1,column=3)
	b14=Button(master,bg='blue',command=lambda:func14(A),height=1,width=1)
	b14.grid(row=1,column=4)
	b15=Button(master,bg='blue',command=lambda:func15(A),height=1,width=1)
	b15.grid(row=1,column=5)
	b20=Button(master,bg='blue',command=lambda:func20(A),height=1,width=1)
	b20.grid(row=2,column=0)
	b21=Button(master,bg='blue',command=lambda:func21(A),height=1,width=1)
	b21.grid(row=2,column=1)
	b22=Button(master,bg='blue',command=lambda:func22(A),height=1,width=1)
	b22.grid(row=2,column=2)
	b23=Button(master,bg='blue',command=lambda:func23(A),height=1,width=1)
	b23.grid(row=2,column=3)
	b24=Button(master,bg='blue',command=lambda:func24(A),height=1,width=1)
	b24.grid(row=2,column=4)
	b25=Button(master,bg='blue',command=lambda:func25(A),height=1,width=1)
	b25.grid(row=2,column=5)
	b30=Button(master,bg='blue',command=lambda:func30(A),height=1,width=1)
	b30.grid(row=3,column=0)
	b31=Button(master,bg='blue',command=lambda:func31(A),height=1,width=1)
	b31.grid(row=3,column=1)
	b32=Button(master,bg='blue',command=lambda:func32(A),height=1,width=1)
	b32.grid(row=3,column=2)
	b33=Button(master,bg='blue',command=lambda:func33(A),height=1,width=1)
	b33.grid(row=3,column=3)
	b34=Button(master,bg='blue',command=lambda:func34(A),height=1,width=1)
	b34.grid(row=3,column=4)
	b35=Button(master,bg='blue',command=lambda:func35(A),height=1,width=1)
	b35.grid(row=3,column=5)
	b40=Button(master,bg='blue',command=lambda:func40(A),height=1,width=1)
	b40.grid(row=4,column=0)
	b41=Button(master,bg='blue',command=lambda:func41(A),height=1,width=1)
	b41.grid(row=4,column=1)
	b42=Button(master,bg='blue',command=lambda:func42(A),height=1,width=1)
	b42.grid(row=4,column=2)
	b43=Button(master,bg='blue',command=lambda:func43(A),height=1,width=1)
	b43.grid(row=4,column=3)
	b44=Button(master,bg='blue',command=lambda:func44(A),height=1,width=1)
	b44.grid(row=4,column=4)
	b45=Button(master,bg='blue',command=lambda:func45(A),height=1,width=1)
	b45.grid(row=4,column=5)
	b50=Button(master,bg='blue',command=lambda:func50(A),height=1,width=1)
	b50.grid(row=5,column=0)
	b51=Button(master,bg='blue',command=lambda:func51(A),height=1,width=1)
	b51.grid(row=5,column=1)
	b52=Button(master,bg='blue',command=lambda:func52(A),height=1,width=1)
	b52.grid(row=5,column=2)
	b53=Button(master,bg='blue',command=lambda:func53(A),height=1,width=1)
	b53.grid(row=5,column=3)
	b54=Button(master,bg='blue',command=lambda:func54(A),height=1,width=1)
	b54.grid(row=5,column=4)
	b55=Button(master,bg='blue',command=lambda:func55(A),height=1,width=1)
	b55.grid(row=5,column=5)
	b=(b00,b01,b02,b03,b04,b05,b10,b11,b12,b13,b14,b15,b20,b21,b22,b23,b24,b25,b30,b31,b32,b33,b34,b35,b40,b41,b42,b43,b44,b45,b50,b51,b52,b53,b54,b55)
	mainloop()