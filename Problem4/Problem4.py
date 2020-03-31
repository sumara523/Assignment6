
def NumOnes(n):
    if n < 1:
        return 0
    elif n < 10:
        return 1
    elif n > 21 and n < 31:
        return 13
    else:
        runner = 0
        count = 0
        while runner <= n:
            str_runner = str(runner)
            lst_runner = list(str_runner)
            print(lst_runner)
            for i in range(len(lst_runner)):            
                if lst_runner[i] == '1':
                    count += 1
            runner += 1
        return count
