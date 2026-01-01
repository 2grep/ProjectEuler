# def import_data():
file = open('data.txt', 'r')
content = file.read()
file.close()
content = content.splitlines()
for i in range(1,len(content)):
    content[i] = content[i].split()
content[0] = [content[0]]
content = [[int(item) for item in sublist] for sublist in content]
#    return content

def find_max_path(content):
    max_total = 0
    level_sums = [[0 for item in sublist] for sublist in content]
    i = len(content)-2
    for j in range(0,len(content[i])): 
        if content[i][j]+content[i+1][j] >= content[i][j]+content[i+1][j+1]:
            total = content[i][j] + content[i+1][j]
        else:
            total = content[i][j] + content[i+1][j+1]
        level_sums[i][j] = total
        if total > max_total:
            max_total = total
    for i in range(len(content)-3,-1,-1):
        for j in range(0,len(content[i])): 
            if content[i][j]+level_sums[i+1][j] >= content[i][j]+level_sums[i+1][j+1]:
                total = content[i][j] + level_sums[i+1][j]
            else:
                total = content[i][j] + level_sums[i+1][j+1]
            level_sums[i][j] = total
            if total > max_total:
                max_total = total
    return max_total, level_sums

print(max_total, level_sums)