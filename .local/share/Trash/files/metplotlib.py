import matplotlib.pyplot as plt
%matplotlib inline
x=[1,2,3,4,5,6,7]
y=[50,51,52,48,47,49,46]
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Weather')
plt.plot(x,y,color='green',linewidth=5, linestyle='dotted')
[<matplotlib.lines.Line2D at 0x16ff68db8d0>]



import matplotlib.pyplot as plt
%matplotlib inline
x=[1,2,3,4,5,6,7]
y=[50,51,52,48,47,49,46]
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Weather')

plt.plot(x,y,'b+--')
[<matplotlib.lines.Line2D at 0x1c806e436d8>]

# Same effect as 'b+' format string
plt.plot(x,y,color='blue',marker='+',linestyle='')
[<matplotlib.lines.Line2D at 0x1c806da3898>]

markersize
plt.plot(x,y,color='blue',marker='+',linestyle='',markersize=20)
[<matplotlib.lines.Line2D at 0x1c8059f7160>]

alpha property to control transparency of line chart
plt.plot(x,y,'g<',alpha=0.5) # alpha can be specified on a scale 0 to 1
[<matplotlib.lines.Line2D at 0x1c805b212b0>]




import matplotlib.pyplot as plt
%matplotlib inline
days=[1,2,3,4,5,6,7]
max_t=[50,51,52,48,47,49,46]
min_t=[43,42,40,44,33,35,37]
avg_t=[45,48,48,46,40,42,41]
plt.plot(days, max_t, label="max")
plt.plot(days, min_t, label="min")
plt.plot(days, avg_t, label="average")
[<matplotlib.lines.Line2D at 0x1f851056eb8>]

Axes labels and chart title
# set axes labels and chart title
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Weather')


plt.plot(days, max_t, label="max")
plt.plot(days, min_t, label="min")
plt.plot(days, avg_t, label="average")
[<matplotlib.lines.Line2D at 0x1f8510c2eb8>]

Legend
# Show legend
plt.plot(days, max_t, label="max")
plt.plot(days, min_t, label="min")
plt.plot(days, avg_t, label="average")

plt.legend(loc='best')
<matplotlib.legend.Legend at 0x1f85224ed30>

# Legend at different location with shadow enabled and fontsize set to large
plt.plot(days, max_t, label="max")
plt.plot(days, min_t, label="min")
plt.plot(days, avg_t, label="average")

plt.legend(loc='upper right',shadow=True,fontsize='large')
<matplotlib.legend.Legend at 0x1f8527de7f0>

Grid
plt.plot(days, max_t, label="max")
plt.plot(days, min_t, label="min")
plt.plot(days, avg_t, label="average")

plt.legend(loc='upper right', fontsize="large",shadow=True)
<matplotlib.legend.Legend at 0x1f852666630>



import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

Simple bar chart showing revenues of major US tech companies
company=['GOOGL','AMZN','MSFT','FB']
revenue=[90,136,89,27]
xpos = np.arange(len(company))
xpos
array([0, 1, 2, 3])
plt.bar(xpos,revenue, label="Revenue")

plt.xticks(xpos,company)
plt.ylabel("Revenue(Bln)")
plt.title('US Technology Stocks')
plt.legend()
<matplotlib.legend.Legend at 0x1fdce45b240>

Multiple Bars showing revenue and profit of major US tech companies
profit=[40,2,34,12]
plt.bar(xpos-0.2,revenue, width=0.4, label="Revenue")
plt.bar(xpos+0.2,profit, width=0.4,label="Profit")

plt.xticks(xpos,company)
plt.ylabel("Revenue(Bln)")
plt.title('US Technology Stocks')
plt.legend()
<matplotlib.legend.Legend at 0x1fdce4ba668>

Horizontal bar chart using barh function
plt.barh(xpos,revenue, label="Revenue")

plt.yticks(xpos,company)
plt.ylabel("Revenue(Bln)")
plt.title('US Technolog Stocks')
plt.legend()
<matplotlib.legend.Legend at 0x1fdcd2ad588>


#In histograms, x axis contains a variable and y axis will be a frequency of that variable


import matplotlib.pyplot as plt
%matplotlib inline

#We have a sample data of blood sugar level of different patients, we will try to plot number of patients by blood range and try to figure out how many patients are normal, pre-diabetic and diabetic

blood_sugar = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
plt.hist(blood_sugar, rwidth=0.8) # by default number of bins is set to 10
(array([ 3.,  3.,  1.,  0.,  1.,  1.,  0.,  2.,  0.,  2.]),
 array([  77. ,   84.3,   91.6,   98.9,  106.2,  113.5,  120.8,  128.1,
         135.4,  142.7,  150. ]),
 <a list of 10 Patch objects>)

bins parameter
plt.hist(blood_sugar,rwidth=0.5,bins=4)
(array([ 7.,  1.,  2.,  3.]),
 array([  77.  ,   95.25,  113.5 ,  131.75,  150.  ]),
 <a list of 4 Patch objects>)

Histogram showing normal, pre-diabetic and diabetic patients distribution
80-100: Normal
100-125: Pre-diabetic
80-100: Diabetic
plt.xlabel("Sugar Level")
plt.ylabel("Number Of Patients")
plt.title("Blood Sugar Chart")

plt.hist(blood_sugar, bins=[80,100,125,150], rwidth=0.95, color='g')
(array([ 6.,  2.,  4.]),
 array([ 80, 100, 125, 150]),
 <a list of 3 Patch objects>)

Mutiple data samples in a histogram
plt.xlabel("Sugar Level")
plt.ylabel("Number Of Patients")
plt.title("Blood Sugar Chart")

blood_sugar_men = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

plt.hist([blood_sugar_men,blood_sugar_women], bins=[80,100,125,150], rwidth=0.95, color=['green','orange'],label=['men','women'])
plt.legend()
<matplotlib.legend.Legend at 0x1c741b46be0>

histtype=step
plt.xlabel("Sugar Level")
plt.ylabel("Number Of Patients")
plt.title("Blood Sugar Chart")

plt.hist(blood_sugar,bins=[80,100,125,150],rwidth=0.95,histtype='step')
(array([ 6.,  2.,  4.]),
 array([ 80, 100, 125, 150]),
 <a list of 1 Patch objects>)

horizontal orientation
plt.xlabel("Number Of Patients")
plt.ylabel("Sugar Level")
plt.title("Blood Sugar Chart")

plt.hist(blood_sugar, bins=[80,100,125,150], rwidth=0.95, orientation='horizontal')
(array([ 5.,  2.,  3.]),
 array([ 80, 100, 125, 150]),
 <a list of 3 Patch objects>)
 
 
 
 
#Draw pie chart to track down home expenses
 

import matplotlib.pyplot as plt
%matplotlib inline

exp_vals = [1400,600,300,410,250]
exp_labels = ["Home Rent","Food","Phone/Internet Bill","Car ","Other Utilities"]
plt.pie(exp_vals,labels=exp_labels)
([<matplotlib.patches.Wedge at 0x28e652a1630>,
  <matplotlib.patches.Wedge at 0x28e652a1b00>,
  <matplotlib.patches.Wedge at 0x28e652a1fd0>,
  <matplotlib.patches.Wedge at 0x28e651b4518>,
  <matplotlib.patches.Wedge at 0x28e651b4a58>],
 [Text(0.0932866,1.09604,'Home Rent'),
  Text(-0.982218,-0.495224,'Food'),
  Text(-0.162847,-1.08788,'Phone/Internet Bill'),
  Text(0.62561,-0.904772,'Car '),
  Text(1.0615,-0.288458,'Other Utilities')])

Draw pie chart as perfect circle
plt.pie(exp_vals,labels=exp_labels, shadow=True)
plt.axis("equal")
plt.show()

Show percentages for every pie. Specify radius to increase chart size
plt.axis("equal")
plt.pie(exp_vals,labels=exp_labels, shadow=True, autopct='%1.1f%%',radius=1.5)
plt.show()

Explode
plt.axis("equal")
plt.pie(exp_vals,labels=exp_labels, shadow=True, autopct='%1.1f%%',radius=1.5,explode=[0,0,0,0.1,0.2])
plt.show()

counterclock and angle properties
plt.axis("equal")
plt.pie(exp_vals,labels=exp_labels, shadow=True, autopct='%1.1f%%',radius=1.5,explode=[0,0,0,0.1,0.2],counterclock=True, startangle=45)
plt.show()


