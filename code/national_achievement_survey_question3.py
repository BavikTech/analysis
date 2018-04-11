import matplotlib.pyplot as plt
import pandas
import numpy
#Reading data to dataframe
data = pandas.read_csv("nas-pupil-marks.csv", delimiter=",").fillna(0)																																																																					
#Reading data from datframe to list
math= data['Maths %'].tolist()
science= data['Science %'].tolist()
state= data['State'].tolist()
sex= data['Gender'].tolist()
#defining variables to be used 
mathnew=[]
sciencenew=[]
names=list(data.columns.values)
#contains names of all the states
stated=[]

sumx=0
sums=0
summ=0
x=0
total1=[]
total2=[]
dividen=1
#quratile for math
q1=0
q2=1
q3=0
q4=0
#quartile for science
Q1=1
Q2=0
Q3=0
Q4=0
quartile=[1,2,3,4]
n_groups=4
index = numpy.arange(n_groups)
#quartile list
quar=[]
Quar=[]
width=0.2
#Calculating average score of math and science and converting blank spaces to avergae score with respect to that subject
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
#Finding score of math and science for each state
for i in range(0,185348):

	if (i==0):
		sumx+=mathnew[i]
		sums+=sciencenew[i]
	elif (state[i]==state[i-1]):
		sumx+=mathnew[i]
		sums+=sciencenew[i]
		dividen+=1
	elif (state[i]!=state[i-1]):
		stated.append(state[i-1])
		total1.append((sumx/dividen))
		total2.append((sums/dividen))
		sumx=0
		sums=0
		dividen=1
		sumx+=mathnew[i]
		sums+=sciencenew[i]
	if (i==185347):
		sumx+=mathnew[i]
		sums+=sciencenew[i]
		dividen+=1
		stated.append(state[i-1])
		total1.append((sumx/dividen))
		total2.append((sums/dividen))
	else:
		pass
#normalizing the score
normed1 = [(i-min(total1))/(max(total1)-min(total1)) for i in total1]
normed2 = [(i-min(total2))/(max(total2)-min(total2)) for i in total2]
#finding quartile for south states in math and science where q1 contains states scoring lowest 25% and q4 with the highest 25% score
for i in range(0,33):
	if (normed1[i]<=0.25 and  stated[i] in ('AN','AP','KN','KL','PY','TN')):
		q1+=1
	if (normed1[i]> 0.25 and normed1[i]<=0.5 and  stated[i] in ('AN','AP','KN','KL','PY','TN')):
		q2+=1
	if (normed1[i]>0.5 and normed1[i]<=0.75 and  stated[i] in ('AN','AP','KN','KL','PY','TN')):
		q3+=1
	if (normed1[i]>0.75 and normed1[i]<=1.0 and stated[i] in ('AN','AP','KN','KL','PY','TN')):
		q4+=1
for i in range(0,33):
	if (normed2[i]<=0.25 and  stated[i] in ('AN','AP','KN','KL','PY','TN')):
		Q1+=1
	if (normed2[i]> 0.25 and normed1[i]<=0.5 and  stated[i] in ('AN','AP','KN','KL','PY','TN')):
		Q2+=1
	if (normed2[i]>0.5 and normed1[i]<=0.75 and  stated[i] in ('AN','AP','KN','KL','PY','TN')):
		Q3+=1
	if (normed2[i]>0.75 and normed1[i]<=1 and stated[i] in ('AN','AP','KN','KL','PY','TN')):
		Q4+=1
quar.append(q1)
quar.append(q2)
quar.append(q3)
quar.append(q4)
Quar.append(Q1)
Quar.append(Q2)
Quar.append(Q3)
Quar.append(Q4)
#print(Quar)
# Plotting the quartile
plt.bar(index, quar,width,
         color = ['red'])
plt.bar(index+width, Quar,width,
       color = ['green'])
plt.legend()
 
plt.tight_layout()
plt.xticks(index + width, ('1', '2', '3', '4'))
plt.ylabel('Number of south states that falls under respective quartile')
plt.title('quartile is as follow(q1<q2<q3<q4) and q1 neing lowest 25 percent and q4 being the highest scoring 25 percent')
plt.xlabel('quartile name')
plt.legend(('Math', 'Science'))
plt.show()
#Plotiing state wise score of math and science
left = [1,2,3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	25,	26,	27,	28,	29,	30,	31,	32,33]

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 8}

plt.rc('font', **font)
plt.bar(left, normed1, tick_label = stated,
        width = 0.2, color = ['red'])
plt.axhline(y=0.5, color='green', linestyle='-')
plt.axhline(y=0.25, color='green', linestyle='-')
plt.axhline(y=0.75, color='green', linestyle='-')
plt.axhline(y=1.0, color='green', linestyle='-')
plt.ylabel('Normalized percentage score of SOUTH STAES')
plt.title('All the SOUTH STATES performace in maths subject')
plt.xlabel('State name')
plt.show()
plt.bar(left, normed2, tick_label = stated,
        width = 0.2, color = ['red'])
plt.axhline(y=0.5, color='green', linestyle='-')
plt.axhline(y=0.25, color='green', linestyle='-')
plt.axhline(y=0.75, color='green', linestyle='-')
plt.axhline(y=1.0, color='green', linestyle='-')
plt.ylabel('Normalized percentage score')
plt.title('All the SOUTH states performace in Science subject')
plt.xlabel('State name')
plt.show()