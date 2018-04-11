import matplotlib.pyplot as plt
import pandas
import numpy
data = pandas.read_csv("nas-pupil-marks.csv", delimiter=",").fillna(0)																																																																					
math= data['Maths %'].tolist()
reading= data['Reading %'].tolist()
science= data['Science %'].tolist()
social= data['Social %'].tolist()
names=list(data.columns.values)
state= data['State'].tolist()
sex= data['Gender'].tolist()
a='MATH'
b='SCIENCE'
c='SOCIAL'
d='READING'
summ=0
x=0
mathnew=[]
sciencenew=[]
socialnew=[]
readingnew=[]
#Calculating average score of all and converting blank spaces to avergae score with respect to that subject
for i in math:
	if i!=0 :
		summ+= i
		x+=1
	else :
		pass
avg=(summ/x)
for i in math:
	if i==0 :
		mathnew.append(avg)
	else:
		mathnew.append(i)
summ=0
x=0
for i in science:
	if i!=0 :
		summ+= i
		x+=1
	else :
		pass
avg=(summ/x)
for i in science:
	if i==0 :
		sciencenew.append(avg)
	else:
		sciencenew.append(i)
summ=0
x=0
for i in social:
	if i!=0 :
		summ+= i
		x+=1
	else :
		pass
avg=(summ/x)
for i in social:
	if i==0 :
		socialnew.append(avg)
	else:
		socialnew.append(i)
summ=0
x=0
for i in reading:
	if i!=0 :
		summ+= i
		x+=1
	else :
		pass
avg=(summ/x)
for i in reading:
	if i==0 :
		readingnew.append(avg)
	else:
		readingnew.append(i)

#finding performance of all the boys  in each subject for each state
def male(lst,sub):
	stated=[]
	sumx=0
	sums=0
	total1=[]
	total2=[]
	dividen=1

	for i in range(0,185348):

		if (i==0 and sex[i]==1 ):
			sumx+=lst[i]
		elif (state[i]==state[i-1] and sex[i]==1):
			sumx+=lst[i]
			dividen+=1
		elif (state[i]!=state[i-1] and sex[i]==1):
			stated.append(state[i-1])
			total1.append((sumx/dividen))
			sumx=0
			dividen=1
			sumx+=lst[i]
		elif (state[i]!=state[i-1] and sex[i]==2):
			stated.append(state[i-1])
			total1.append((sumx/dividen))
			sumx=0
			dividen=1
		elif (i==185347 and sex[i]==2 ):
			stated.append(state[i-1])
			total1.append((sumx/dividen))
		else:
			pass
	normed1 = [(i-min(total1))/(max(total1)-min(total1)) for i in total1]
	#normed2 = [i/max(total2) for i in total2]
	print(normed1)
	print(stated)
	#graph of all the boys in all subjects in each state
	left = [1,2,3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	25,	26,	27,	28,	29,	30,	31,	32,33]

	font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 9}

	plt.rc('font', **font)
	plt.bar(left, normed1, tick_label = stated,
        width = 0.2, color = ['red'])
	plt.ylabel('Normalized'+str(sub)+' performance score')
	plt.title('NOTE :How do boys perform across states?')
	plt.xlabel('State name')
	plt.axhline(y=0.5, color='green', linestyle='-')
	plt.axhline(y=0.25, color='green', linestyle='-')
	plt.axhline(y=0.75, color='green', linestyle='-')
	plt.axhline(y=1.0, color='green', linestyle='-')
	plt.show()
def female(lst,sub):
	#finding performance of all the girls  in each subject in each state
	stated=[]
	sumx=0
	sums=0
	total1=[]
	total2=[]
	dividen=1
	for i in range(1,185348):

		#if (i==0 and sex[i]==1 ):
		#	pass
		if (i==1 and sex[i]==2 ):
			sumx+=lst[i]
		elif (state[i]==state[i-1] and sex[i]==2):
			sumx+=lst[i]
			dividen+=1
		elif (state[i]!=state[i-1] and sex[i]==2):
			stated.append(state[i-1])
			total1.append((sumx/dividen))
			sumx=0
			dividen=1
			sumx+=lst[i]
		elif (state[i]!=state[i-1] and sex[i]==1):
			stated.append(state[i-1])
			total1.append((sumx/dividen))
			sumx=0
			dividen=1
		if (i==185347 and sex[i]==2 ):
			sumx+=lst[i]
			dividen+=1
			stated.append(state[i-1])
			total1.append((sumx/dividen))
			
		else:
			pass
	
	normed1 = [(i-min(total1))/(max(total1)-min(total1)) for i in total1]
	#print(normed1)
	#graph of female in all subjects for each state
	left = [1,2,3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	25,	26,	27,	28,	29,	30,	31,	32,33]

	font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 9}

	plt.rc('font', **font)
	plt.bar(left, normed1, tick_label = stated,
        width = 0.2, color = ['red'])
	plt.ylabel('Normalized'+str(sub)+' performance score')
	plt.title('NOTE :How do girls perform across states?')
	plt.xlabel('State name')
	plt.axhline(y=0.5, color='green', linestyle='-')
	plt.axhline(y=0.25, color='green', linestyle='-')
	plt.axhline(y=0.75, color='green', linestyle='-')
	plt.axhline(y=1.0, color='green', linestyle='-')
	plt.show()
male(mathnew,a)
male(sciencenew,b)
male(socialnew,c)
male(readingnew,d)
female(mathnew,a)
female(sciencenew,b)
female(socialnew,c)
female(readingnew,d)
