from timeit import default_timer as timer

def run():
    limit = 1000000
    div_sum = [0] * limit
    for i in range(1, limit):
        for j in range(i * 2, limit, i):
            div_sum[j] += i
            
    max_chain = []
    max_len = 0
    ans =  -1
    for i in range(1, limit):
        checked = list()
        check = i
        while True:
            checked.append(check)
            next_check = div_sum[check]
            if next_check == i:
                if len(checked) > max_len:
                    max_chain = list(checked)
                    max_len = len(checked)
                break
            elif next_check in checked or next_check > limit:
                break
            else:
                check = next_check
    max_chain.append(max_chain[0])
    return max_chain, min(max_chain)
                
if __name__ == "__main__":
    s = timer()
    res = run()
    e = timer()
    print(res[0])
    print("Answer: " + str(res[1]))
    print("Time taken: " + str(e - s) + "s")
    
