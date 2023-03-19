# python3

def parallel_processing(n, m, data):
    output = []
    g = []
    for i in range(n):
        g.append(0)
    d = 0
    t = 0
    while d < m:
        for i in range(n):
            if g[i] == t:
                output.append((i, t))
                g[i] = g[i] + data[d]
                d = d + 1
        t = t + 1
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    r = input().split()
    n = int(r[0])
    m = int(r[1])

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    r = input().split()
    for i in range(m):
        data.append(int(r[i]))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i in range(m):
        print(result[i][0], result[i][1])



if _name_ == "_main_":
    main()
