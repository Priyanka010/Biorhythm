from datetime import date
from pylab import plot, show, title, legend, xlabel, ylabel,grid
from numpy import array,sin,pi

Year = int(input("Give your birth year: "))
Month = int(input("Give your birth month: "))
Day = int(input("Give your birth day: "))
MyDob1 = date(Year,Month,Day)
t0 = MyDob1.toordinal()
Year2 = int(input("Give your target year: "))
Month2 = int(input("Give your target month: "))
Day2 = int(input("Give your target day: "))
MyDob2 = date(Year2,Month2,Day2)
t1 = MyDob2.toordinal()
MyDob = MyDob2 - MyDob1
t = array(range((t1-10),(t1+10))) # range of 20 days
print('The number of days since birth is',MyDob)

y = 100*[sin(2*pi*(t-t0)/23),  # Physical
         sin(2*pi*(t-t0)/28),  # Emotional
         sin(2*pi*(t-t0)/33)]; # Intellectual
# converting ordinals to date
label = []
for p in t:
 label.append(date.fromordinal(p))

fig = plot.figure()
ax = fig.gca()
plot(label,y[0],label,y[1],label,y[2])
grid() # adding grid to chart
legend(['Physical', 'Emotional', 'Intellectual']) # adding a legend
# formatting the dates on the x axis
ax.set_xticklabels(label, rotation=45, ha='right') #writing dates vertically
title('Biorythms charts')
xlabel('Date')
ylabel('Percentage (%) ' ) 
show()
