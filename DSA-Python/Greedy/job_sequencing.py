#Job Sequencing with deadlines
def job_seq(profits,deadline,deadlines):
    index = list(range(len(profits)))
    
    job_profit = list(zip(profits,deadlines))

    time_slot = [-1] * deadline
    index.sort(key = lambda x : job_profit[x][1],reverse=True)
    profit = 0
    for job in index:
        for j in reversed(range(deadline)):
            if job_profit[job][1]>= j and time_slot[j] == -1:
                time_slot[j] = ["Job"]+[job]
                profit += profits[job]
                break
    print(profit)
    print(time_slot)

profits = list(map(int,input().split()))
deadlines = list(map(int,input().split()))
deadline = int(input())
job_seq(profits,deadline,deadlines)