full_list = [[25, 110], [26, 100], [27, 101], [28, 105], [29,99], [30, 120]]

flag_list = []
prev_figure = full_list[0]


for figure in full_list:
    if figure[1] == prev_figure[1]:
        pass
    elif figure[1] < prev_figure[1]:
        answer = prev_figure[1] - figure[1]           
        flag_list.append([figure[0], answer])
        prev_figure = figure
        print(figure)
    else:
        prev_figure = figure
print(flag_list)
