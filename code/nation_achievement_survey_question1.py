import matplotlib.pyplot as plt
import pandas
import numpy
#read data to datframe
data = pandas.read_csv("nas-pupil-marks.csv", delimiter=",",usecols=(2,3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	25,	26,	27,	28,	29,	30,	31,	32,	33,	34,	35,	36,	37,	38,	39,	40,	41,	42,	43,	44,	45,	46,	47,	48,	49,	50,	51,	52,	53,	54,	55,	56,	57,	58,	59,	60,	61,	62,	63)).fillna(0)																																																																						
usecomputers= data['Use computer'].tolist()
Subjects= data['Subjects'].tolist()
usecomputer=[]
l=[]
m=[]
o=[]
s=[]
zero=[]
math= data['Maths %'].tolist()
reading= data['Reading %'].tolist()
science= data['Science %'].tolist()
social= data['Social %'].tolist()
#defining variables to be used 
mathnew=[]
sciencenew=[]
socialnew=[]
readingnew=[]
#Calculating average score of all and converting blank spaces to avergae score with respect to that subject
for i in range(0,185348):
	if (usecomputers[i]== 'Yes'):
		usecomputer.append(1)
	else :
		usecomputer.append(0)
data.insert(loc=62, column='usecomputer', value=usecomputer)
for i in range(0,185348):
	if (Subjects[i]== 'L'):
		l.append(1)
	else :
		l.append(0)
data.insert(loc=63, column='l', value=l)
for i in range(0,185348):
	if (Subjects[i]== 'O'):
		o.append(1)
	else :
		o.append(0)
data.insert(loc=64, column='o', value=o)
for i in range(0,185348):
	if (Subjects[i]== 'M'):
		m.append(1)
	else :
		m.append(0)
data.insert(loc=65, column='m', value=m)
for i in range(0,185348):
	if (Subjects[i]== 0):
		zero.append(1)
	else :
		zero.append(0)
data.insert(loc=66, column='zero', value=zero)
for i in range(0,185348):
	if (Subjects[i]== 'S'):
		s.append(1)
	else :
		s.append(0)
data.insert(loc=67, column='s', value=s)
summ=0
x=0
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
data.insert(loc=68, column='math', value=mathnew)
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
data.insert(loc=69, column='science', value=sciencenew)
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
data.insert(loc=70, column='social', value=socialnew)
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
data.insert(loc=71, column='reading', value=readingnew)
averg=[]
#finding average of all subjects for each student
for i in range(0,185348):
	averg.append(mathnew[i]+readingnew[i]+sciencenew[i]+socialnew[i])
data.insert(loc=72, column='aveg', value=averg)
del data['Maths %']
del data['Reading %']
del data['Social %']
del data['Science %']
del data['Use computer']
del data['Subjects']
print(data.head)
names=list(data.columns.values)
#finding r values 
correlations = data.corr()
# plot correlation matrix
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0,67,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
plt.ylabel('Each Factor')
plt.title('NOTE :correlation cofficient ("r") value compared of each factor(magnify for the particular factor inn the result after running the respected python code to see exact values )')
plt.show()