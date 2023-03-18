# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    
    available_threads = [(0, i) for i in range(n)] 
    heapq.heapify(available_threads) 
    
    for x in data:
        next_thread = heapq.heappop(available_threads) 
        start = next_thread[0]
        thread = next_thread[1] 
        
        output.append((thread, start)) 
        available_time = start + x 
        heapq.heappush(available_threads, (available_time, thread)) 

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    inputs = input().split()

    n = int(inputs[0])
    m = int(inputs[1])
    # second line - data
    data = list(map(int, input().split()))
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i, j in result:
        print(i, j)


if __name__ == "__main__":
    main()
