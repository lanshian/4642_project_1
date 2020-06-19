import numpy as np

import copy
import math
from numpy import random
import matplotlib.pyplot as plt

# initialize

IAT_rate = float(input("lamda: "))   #lamda pks/us
ST_rate = 1    #pks/us
num_processes = int(input("num_processes: "))
pkt_size = 0
ans = 0
mean_size_pkt = 1 #pks
IAT = []
SST = []
AT = []
ST = []
DT = []
qu = []
j = 0
T = []
queue_size = 0
wait_time = []
n = 0

# find inter arrival_time
for i in range(num_processes):
    temp = random.exponential(1/IAT_rate)
    if i == 0:
        IAT.append(0)
        AT.append(0)
        ST.append(0)
        SST.append(0)
        DT.append(0)
    else:
        IAT.append(temp)
        AT.append(AT[i - 1] + IAT[i])
        pkt_size = np.random.exponential(mean_size_pkt)
        ST.append(pkt_size / ST_rate)
        SST.append(max(AT[i], DT[i - 1]))
        DT.append(SST[i] + ST[i])



temp = DT[0]  # pkt1.append(pkt(AT[i],SST[i],ST[i]))
server_busy = False
# generate the queue number array

for i in range(1,num_processes):

    if temp > AT[i]:
        queue_size += 1
    # print("\n", AT[i], ": pkt", i, "arrives and find", queue_size, "packets in the queue")
    else:
        while i-j > 0 and temp <=  AT[i] :
            j += 1
            temp = DT[j]
            queue_size = queue_size - 1
        
        # print("\n", DT[j], ": pkt", j, " departs having spent", ST[j], "us in the system")
    if queue_size < 0:
        queue_size = 0
     

    qu.append(queue_size)
#print(qu)

p = []

for i in range(1, num_processes):
    T.append((DT[i] - AT[i]))

#    print('packet', i, 'arrives and find', qu[i], 'packets in the queue. packet spend',ST[i], 'us in the system. The packet arrival at ',AT[i],"us and depart at",DT[i],"us")

print("\n Summary:")
print("\n N, the average number of customers in the system: %.10f " % np.mean(qu))
print("\n T, the average time spent by customer in the system: %.10f us" % np.mean(T))
print("probability P(n) that an arriving packet finds n packets already in the system: ")

for n in range(11):
    i = (math.exp(-IAT_rate) * IAT_rate ** n) / math.factorial(n)
    p.append(i)
    print(" %1.f :" % n, " %.2f" % i)


#plot
height = []
bars = []
for n in range(11):
    height.append(p[n])
    bars.append(n)
y_pos = np.arange(len(bars))

plt.bar(y_pos, height, color=['black', 'red', 'green', 'blue', 'cyan', 'black', 'red', 'green', 'blue', 'cyan', 'black'])

# Create names on the x-axis
plt.xticks(y_pos, bars)

# Show graphic
plt.show()