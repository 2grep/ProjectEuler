file = open('data.txt', 'r')
content = file.read()
file.close()
content = content.splitlines()

def solution_13(content,n):
    numbers = [int(i) for i in content]
    numsumstr = str(sum(numbers))
    first_n = []
    for i in range(0,10):
        first_n.append(numsumstr[i])
    return first_n 

print(solution_13(content,10))