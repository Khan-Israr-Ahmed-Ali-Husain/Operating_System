'''
Operating System  Project
Name : Khan Israr Ahmed Ali Husain
Description :
It is based on Scheduling Algorithms. We can calculate the Average Waiting Time and Average Burst Time using
1. FCFS (with or without Arrival Time)
2. SJF non-preemptive (with or without Arrival Time)
3. Priority Algorithm (with or without Arrival Time)
'''
def FCFS():
    n=int(input("Enter the Number of Processes : "))
    bt=[]
    at=[]
    flag=int(input("Have all the processes arrived at same time (Press [1] : YES  , Press[0] : NO) : "))
    for i in range(n):
        if(flag==1):
            at.append(0)
        else:    
            at.append(int(input("Enter the Arrival time of Process P{} : ".format(i+1))))
        bt.append(int(input("Enter the Burst time of Process P{} : ".format(i+1))))
    tl=0
    wt=[]
    tat=[]
    i=0
    while i<len(at):
        if tl>=at[i]:
            wt.append(tl-at[i])
            tat.append(wt[i]+bt[i])
            tl +=bt[i]
            i +=1
        else:
            tl +=1
    print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurn Around Time")
    for i in range(len(bt)):
        print("  P{}         {}             {}                 {}                 {}".format(i+1,at[i],bt[i],wt[i],tat[i]))
    print("Average Waiting Time : {} ms".format(sum(wt)/len(bt)))
    print("Average Turn Around Time : {} ms".format(sum(tat)/len(bt)))

def SJF():
    n=int(input("Enter the Number of Processes : "))
    bt=[]
    at=[]
    flag=int(input("Have all the processes arrived at same time (Press [1] : YES  , Press[0] : NO) : "))
    for i in range(n):
        if(flag==1):
            at.append(0)
        else:    
            at.append(int(input("Enter the Arrival time of Process P{} : ".format(i+1))))
        bt.append(int(input("Enter the Burst time of Process P{} : ".format(i+1))))
    tl=0
    wt=[]
    tat=[]
    done_at_position=[]
    for i in range(len(bt)):
        wt.append(0)
        tat.append(0)
        done_at_position.append(None)

    for i in range(len(bt)):
        if(tl>=at[i]):
            tmp=[]
            for j in range(len(bt)):
                if j in done_at_position:
                    tmp.append(0)
                elif (at[j]<=tl):
                    tmp.append(bt[j])
                else:
                    tmp.append(0)
            m=0
            min=0
            while(min==0):
                min=tmp[m]
                m +=1

            for j in tmp:
                if (j<=min and j!=0):
                    min=j

            done_at_position[tmp.index(min)] = tmp.index(min)
            wt[tmp.index(min)]=tl-at[tmp.index(min)]
            tat[tmp.index(min)]=bt[tmp.index(min)]+wt[tmp.index(min)]
            tl +=bt[tmp.index(min)]
        else:
            tl +=1
    print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurn Around Time")
    for i in range(len(bt)):
        print("  P{}         {}             {}                 {}                 {}".format(i+1,at[i],bt[i],wt[i],tat[i]))
    print("Average Waiting Time : {} ms".format(sum(wt)/len(bt)))
    print("Average Turn Around Time : {} ms".format(sum(tat)/len(bt)))

def PriorityAlgo():
    n=int(input("Enter the Number of Processes : "))
    bt=[]
    at=[]
    priority=[]
    flag=int(input("Have all the processes arrived at same time (Press [1] : YES  , Press[0] : NO) : "))
    for i in range(n):
        if(flag==1):
            at.append(0)
        else:    
            at.append(int(input("Enter the Arrival time of Process P{} : ".format(i+1))))
        bt.append(int(input("Enter the Burst time of Process P{} : ".format(i+1))))
        priority.append(int(input("Enter the Priority of Process P{} : ".format(i+1))))

    tl=0
    wt=[]
    tat=[]
    done_at_position=[]
    for i in range(len(bt)):
        wt.append(0)
        tat.append(0)
        done_at_position.append(None)

    for i in range(len(bt)):
        if(tl>=at[i]):
            tmp_priority=[]
            for j in range(len(bt)):
                if j in done_at_position:
                    tmp_priority.append(0)
                elif (at[j]<=tl):
                    tmp_priority.append(priority[j])
                else:
                    tmp_priority.append(0)
            m=0
            min=0
            while(min==0):
                min=tmp_priority[m]
                m +=1

            for j in tmp_priority:
                if (j<=min and j!=0):
                    min=j

            done_at_position[tmp_priority.index(min)] = tmp_priority.index(min)
            wt[tmp_priority.index(min)]=tl-at[tmp_priority.index(min)]
            tat[tmp_priority.index(min)]=bt[tmp_priority.index(min)]+wt[tmp_priority.index(min)]
            tl +=bt[tmp_priority.index(min)]
        else:
            tl +=1
    print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurn Around Time")
    for i in range(len(bt)):
        print("  P{}         {}             {}                 {}                 {}".format(i+1,at[i],bt[i],wt[i],tat[i]))
    print("Average Waiting Time : {} ms".format(sum(wt)/len(bt)))
    print("Average Turn Around Time : {} ms".format(sum(tat)/len(bt)))
    
print('----MENU----')
print('1. FCFS')
print('2. SJF (Non-Preemptive)')
print('3. Priority Algorithm')
choice = int(input('Enter your Choice : '))
if(choice == 1):
    FCFS()
elif(choice == 2):
    SJF()
elif(choice == 3):
    PriorityAlgo()
else:
    print('Invalid Input!')

            



    


            



