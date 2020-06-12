'''
The proper divisors of a number are all the divisors excluding the number itself.
For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these
divisors is equal to 28, we call it a perfect number.
Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper
divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284
are called an amicable pair.
Perhaps less well known are longer chains. For example, starting with 12496, we form
a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.
Find the smallest member of the longest amicable chain with no element exceeding
one million.
'''

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
    
