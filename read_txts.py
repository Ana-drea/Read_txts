import os
import pandas as pd

sort_order = ["DE-DE", "FR-FR", "IT-IT", "ES-ES", "JA-JP", "KO-KR", "ZH-TW", "ZH-CN", "CS-CZ", "PL-PL", "HU-HU",
              "RU-RU", "PT-BR"]
index_order = ["new", "updated", "repeated", "post-edit", "review"]


def get_word_count(path):
    with open(path, encoding='utf-8') as file:
        content = file.readlines()
        # print(content.rstrip())

    list = []
    i = 0
    j = 0
    while j < 10:
        line = content[i]
        if not line.isspace():
            if 4 < j:
                str_num = line.split()[-2:-1]
                num = int(str_num[0])
                list.append(num)
            j += 1
        i += 1

    # for i in range(6, 11):
    #     # str_num = content[i].rstrip().split()[-3:-2]
    #     str_num = content[i].split()[-3:-2]
    #     num = int(str_num[0])
    #     list.append(num)

    return list


def get_project_word_count(path):
    # dict that uses language as key, and corresponding word count list as value
    dict = {}
    project_list = []

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        lan = filename[:5].upper()
        dict[lan] = get_word_count(file_path)

    for language in sort_order:
        empty_list = [0, 0, 0, 0, 0]
        # empty_list is the default value if target lan doesn't exist in dict
        data = dict.get(language, empty_list)
        lan_df = pd.DataFrame(data,
                              index=index_order, columns=[language])

        project_list.append(lan_df)
    project_df = pd.concat(project_list,
                           axis=1)  # axis = 0, data will concat vertically; axis = 1,data will concat horizontally.
    return (project_df)


def get_projects(path):
    dfs = []
    for subfolder in os.listdir(path):
        sub_path = os.path.join(path, subfolder)
        df = get_project_word_count(sub_path)
        dfs.append(df)

    df = dfs[0]
    shape = df.shape
    # concat all the dataframes into a single sheet
    dataframes = pd.concat(dfs, axis=0)
    df_sum = pd.DataFrame(columns=sort_order, index=index_order)

    # add the wordcount of all sheets together
    for i in range(shape[0]):
        for j in range(shape[1]):
            sum = 0
            for k in range(len(dfs)):
                sum += dfs[k].iloc[i, j]
            df_sum.iloc[i, j] = sum

    # write the result to excel file
    dataframes.to_excel(os.path.join(path, 'wordcounts.xlsx'))
    df_sum.to_excel(os.path.join(path, 'sum.xlsx'))


path = input("Type in the project folder path:")
get_projects(path)

# path = r'c:\Users\AnZhou\Downloads\SW_Statistic_Sample\SW_Analysis\A\cs-CZ_LISP-IDE__csy_Statistics.txt'
# get_word_count(path)
