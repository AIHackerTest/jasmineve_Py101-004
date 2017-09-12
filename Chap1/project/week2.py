# -*- coding: utf-8 -*-
weather = open('weather_info.txt')
w_dict = {}
for i in weather.readlines():
    t = i.strip('\n')
    lis = t.split(',')
    w_dict[lis[0]] = lis[1]

his = ''
while True:
    w = input("请输入指令或您要查询的城市名： ")
    if w == 'help':
        print('''
输入城市名，查询该城市的天气；
输入 help，获取帮助文档；
输入 history，获取查询历史；
输入 quit，退出天气查询系统。
        ''')
    elif w == 'quit':
        break
    elif w == 'history':
        print(his)
    else:
        if w in w_dict:
            print(w_dict[w])
            his = his + w + w_dict[w]+ '\n'
        else:
            print('您的输入有误，请重新输入')

quit()
