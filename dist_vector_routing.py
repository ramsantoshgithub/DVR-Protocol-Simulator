import queue
import numpy as np
import time
import sys
from _thread import *
import threading

def readfile():                 
    file_name=sys.argv[1]      
    file1 = open(file_name,"r+")
    input=file1.read()          
    return input

def appendweights(a):           #function to append the weights to the list
    i=2
    while a[i]!='EOF':
        arr.append(a[i].split(' '))
        weights.append(a[i].split(' '))
        i=i+1

    
    for i in range(0,len(weights)):     #converting the weights to integers
        for j in range(0,len(weights[i])):
            if(weights[i][j]>= 'A' and weights[i][j]<='Z'):
                weights[i][j] = ord(weights[i][j])-65
            else:
                weights[i][j] = int(weights[i][j])
    return weights
    
class thread(threading.Thread):                     #thread class
    def __init__(self, thread_name): 
        threading.Thread.__init__(self) 
        self.thread_name = int(thread_name)
        
    def run(self):                                  #the main function run by each thread
        c=0
        while(c<5):
            lock.acquire()                          
            if c==0:                                #printing initial distance vector at iteration zero
                print('------------------')
                print('node name:'+chr(self.thread_name + 65)+'\t'+'iteration:'+str(c))
                for k in range(0,len(routing_table[int(self.thread_name)])):
                    # print(chr(k+65))
                    print('D('+chr(k+65)+')'+' - '+str(routing_table[int(self.thread_name),k]))
                print('------------------')


            #data sent to queues in 2 messages. 1 is its name. 2 is its distant vector    
            for i in range(0,len(weights)):         #each and every node sending their distant vectors to their neighbours queues.   
                if weights[i][0]==int(self.thread_name):                
                    array_queues[weights[i][1]].put(weights[i][0])
                    array_queues[weights[i][1]].put(routing_table[weights[i][0]])
                elif weights[i][1]==int(self.thread_name):
                    array_queues[weights[i][0]].put(weights[i][1])
                    array_queues[weights[i][0]].put(routing_table[weights[i][1]])
            #print(str(self.thread_name)+': ended')
            lock.release()

            time.sleep(2)


            cnt=0
            neighbours=[]           #neighbours name
            rt=[]      #neighnours routing table
            while(not(array_queues[self.thread_name].empty() ) ):
                if cnt%2==0:
                    neighbours.append(array_queues[self.thread_name].get())
                else:
                    rt.append(array_queues[self.thread_name].get())
                cnt=cnt+1


            #bellman fords formula
            for i in range(0,count):
                
                if i!=self.thread_name:
                    minimum=float('inf')
                    for j in range(0,len(rt)):
                        if minimum > (edge_costs[self.thread_name][neighbours[j]] + rt[j][i]):
                            minimum = (edge_costs[self.thread_name][neighbours[j]] + rt[j][i])
                    routing_table_new[self.thread_name,i]=minimum
            
            lock.acquire()
            print('------------------')
            print('node name:'+chr(self.thread_name + 65)+'\t'+'iteration:'+str(c+1))
            for k in range(0,len(routing_table[int(self.thread_name)])):
                if routing_table_new[int(self.thread_name),k]==routing_table[int(self.thread_name),k]:
                    print('D('+chr(k+65)+')'+' - '+str(routing_table_new[int(self.thread_name),k]))
                else :
                    print('D('+chr(k+65)+')'+' - '+str(routing_table_new[int(self.thread_name),k])+'*')
            print('------------------')
            for i in range(0,count):
                routing_table[self.thread_name,i]=routing_table_new[self.thread_name,i]
            lock.release()
            time.sleep(2)
            c=c+1


input=readfile()
a=input.split('\n')             #splitting it based on new line
count=int(a[0])                 #storing number of nodes
arr=[]
weights=[]                      # this list stores connection between nodes and their weights


weights=appendweights(a)
print(arr)

edge_costs=np.zeros((count,count))  # array of size nodes*nodes. it stores values of edges costs
routing_table=np.zeros((count,count))  #initial distance vector values which are equal to edge costs

routing_table_new=np.zeros((count,count))  #empty new distance vector to store new ones after updation


lock = threading.Lock()


for i in range(0, len(weights)):                         #storing edge costs to routing vector in the form of matrix in both directions
    routing_table[weights[i][0],weights[i][1]]=weights[i][2]        
    routing_table[weights[i][1],weights[i][0]]=weights[i][2]



for i in range(0, count):
    for j in range(0,count):
        if i==j:                                    #the distnace vector for a node itself is o.
            routing_table[i,j]=0
        elif routing_table[i,j]==0:
            routing_table[i,j]=float('inf')         #the distnace vector for  nodes which dont have connection  is 'inf'
    
print(routing_table)

edge_costs=np.copy(routing_table)

array_queues={}                 #shared buffer
for i in range(0,count):
    array_queues[i]= queue.Queue()

th=[]

for i in range(0,count):
    thr= thread(i) 
    th.append(thr)
    th[i].start()


