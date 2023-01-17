
path = r'c:\Users\AnZhou\Downloads\SW_Statistic_Sample\SW_Analysis\C\cs-CZ_Summary_stats.txt'
with open(path, encoding='utf-8') as file:
    content = file.readlines()
    print(type(content))

list = []
i = 0
j = 0
while j < 10:
    line = content[i]
    if not line.isspace():
        if 4 < j:
            print(line)
        j+=1
    i+=1

# dict[lan] = list
# return list