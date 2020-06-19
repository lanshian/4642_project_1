import numpy as np
import math
from numpy import random
import matplotlib.pyplot as plt
import sys

# initialize
trace = str(sys.argv[1])  # trace
f = open(trace, "r")
contents = f.readlines()

ST_rate = 10 * (10 ** 3)  #bits/us

pkt_size = 0
ans = 0
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
pkt_size = []
n = 0

IAT.append(0)
pkt_size.append(0)
for i in range(len(contents)):
    IAT.append(float(contents[i].split('\t')[0]))
    pkt_size.append(int(contents[i].split('\t')[1]))

lamda = 1 / (np.mean(IAT))

#mean_pkt_size = (np.mean(pkt_size)) * 8  # bits
#mu = ST_rate / mean_pkt_size
# around 1.43 pkts per us

# find inter arrival_time
for i in range(len(contents)):
    if i == 0:
        AT.append(0)
        ST.append(0)
        SST.append(0)
        DT.append(0)
    else:
        AT.append(AT[i - 1] + IAT[i])
        ST.append(pkt_size[i] * 8/ST_rate)
        SST.append(max(AT[i], DT[i - 1]))
        DT.append(SST[i] + ST[i])
#   find service start time and departure time


temp = DT[1]  # pkt1.append(pkt(AT[i],SST[i],ST[i]))
server_busy = False
# generate the queue number array

for i in range(1, len(contents)):
    if temp > AT[i]:
        queue_size += 1
    # print("\n", AT[i], ": pkt", i, "arrives and find", queue_size, "packets in the queue")
    else:
        while i - j > 0 and temp <= AT[i]:
            j += 1
            temp = DT[j]
            queue_size = queue_size - 1

        # print("\n", DT[j], ": pkt", j, " departs having spent", ST[j], "us in the system")
    if queue_size < 0:
        queue_size = 0

    qu.append(queue_size)
qu.append(queue_size)



for i in range(1, len(contents)):
    T.append((DT[i] - AT[i]))

#    print('packet', i, 'arrives and find', qu[i], 'packets in the queue. packet spend',ST[i], 'us in the system. The packet arrival at ',AT[i],"us and depart at",DT[i],"us")
print("\n Summary:")
print("\n N, the average number of customers in the system: %.10f " % np.mean(qu))
print("\n T, the average time spent by customer in the system: %.10f us" % np.mean(T))
print("probability P(n) that an arriving packet finds n packets already in the system: ")

#for n in range(11):
#    i = (math.exp(-lamda) * lamda ** n) / math.factorial(n)
#    p.append(i)
#    print(" %1.f :" % n, " %.2f" % i)

p = []
m = [0] * 11
for i in range(len(contents)):
    for n in range(11):
        if qu[i] == n:
            m[n]+= 1


print(3686993/4501993)

for n in range(11):

    i = m[n]/len(contents)
    p.append(i)
    print(" %1.f :" % n, " %.2f" % i)

# plot
height = []
bars = []
for n in range(11):
    height.append(p[n])
    bars.append(n)
y_pos = np.arange(len(bars))

plt.bar(y_pos, height,
        color=['black', 'red', 'green', 'blue', 'cyan', 'black', 'red', 'green', 'blue', 'cyan', 'black'])

# Create names on the x-axis
plt.xticks(y_pos, bars)

# Show graphic
plt.show()