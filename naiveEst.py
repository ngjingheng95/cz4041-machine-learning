# calculate estimated probability density for each data instance
def naive_estimator(origin, values, width, n, m):
    numerator = 0
    for x in range(n):
        count = 0
        for y in range(m):
            if abs((values[x][y] - origin[y]) / width) < 1/2:
                count += 1
        if count == m:
            numerator += 1
    return (numerator / (n * (width ** m)))

with open("data.txt", "r") as f:
    dataset = f.read().split("\n")
    meta_info =  dataset[0].split(",")
    n = int(meta_info[0])
    m = int(meta_info[1])
    values = []
    for i in range(1, n+1):
        row = dataset[i].split()
        values.append([float(j) for j in row])

width = 2
output = []
for origin in values:
    result = naive_estimator(origin, values, width, n, m)
    output.append(str(result))

with open('output.txt', 'w') as output_f:
    output_f.writelines("%s\n" % prob for prob in output)
