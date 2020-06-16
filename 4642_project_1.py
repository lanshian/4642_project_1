import numpy as np
import queue
import copy
import random

# initialize
IAT_rate = 9*(10**6)
ST_rate  = 10*(10**9)
num_processes = 10000
pkt_size = 0
ans = 0
import numpy as np
import queue
import copy
import random

IAT_rate = 10**6
ST_rate  = 10*(10**9)
num_processes = 10000
pkt_size = 0
ans = 0
mean_size_pkt=10000
IAT = []
SST = []
AT = []
ST = []
DT = []
qu = []
j = 0
T = []
queue_size = 0
wait_time= []



# find inter arrival_time
for i in range(num_processes):
    temp = random.expovariate(IAT_rate)
    if i==0:
        IAT.append(0)
        AT.append(0) 
        ST.append(0)
        SST.append(0)
        DT.append(0)
    else:
        IAT.append(temp)
        AT.append(AT[i-1] + IAT[i])
        pkt_size= np.random.exponential(mean_size_pkt)
        ST.append(pkt_size/ST_rate)
        SST.append(max(AT[i],DT[i-1]))
        DT.append(SST[i]+ST[i])
#   find service start time and depature time


 
temp=DT[1]  #  pkt1.append(pkt(AT[i],SST[i],ST[i]))

# generate the queue number array
for i in range(num_processes):
    if i==0:
        qu.append(0)
    elif temp > AT[i]:
        queue_size+=1
       
    else:
        j+=1
        temp = DT[j]
        queue_size=queue_size-1
    
    if queue_size < 0:
        queue_size= 0
        
    qu.append(queue_size)

for i in range(num_processes):
    T.append((DT[i]-AT[i])*(10**6))
    
    
print("\n Summary:")
print("\n N, the average number of customers in the system: %.10f "  %np.mean(qu))
print ("\n T, the average time spent by customer in the system: %.10f us" %np.mean(T))