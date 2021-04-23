from math import *

def get_distance(origin, destination):
    # 根据经纬度计算两个点距离
    lon1 = radians(float(destination[0]))
    lon2 = radians(float(origin[0]))
    lat1 = radians(float(destination[1]))
    lat2 = radians(float(origin[1]))
    dlon = lon1 - lon2
    dlat = lat1 - lat2
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    dist = 2 * asin(sqrt(a))*6371*1000
    return dist

f = open("data.csv", encoding='utf-8')
longitude=[];
latitude=[];
for line in f:
    line = line.strip("\n")
    ls = line.split(",")
    longitude.append(ls[1])
    latitude.append(ls[2])
f.close()

# g = open("data_done.csv", encoding='utf-8', mode='w')
# g.write(" ,")
# for _ in range(len(longitude)):
#     g.write("{},".format(_+1))
# g.write("\n")
# for i in range(len(longitude)):
#     g.write("{},".format(i+1))
#     for j in range(len(longitude)):
#         dis=get_distance([longitude[i],latitude[i]],[longitude[j],latitude[i]])+get_distance([longitude[i],latitude[i]],[longitude[i],latitude[j]])
#         g.write("{:0},".format(dis))
#     g.write("\n")
# g.close()

# g = open("data_data.csv", encoding='utf-8', mode='w')
# g.write(" ,")
# for _ in range(len(longitude)):
#     g.write('{},{}\n'.format(longitude[_],latitude[_]))
# g.close()

#选取第一个点为坐标原点
g = open("data_co.csv", encoding='utf-8', mode='w')
for _ in range(len(longitude)):
    x=get_distance([longitude[0],latitude[0]],[longitude[0],latitude[_]])
    y=get_distance([longitude[0],latitude[0]],[longitude[_],latitude[0]])
    if(longitude[0]>longitude[_]):
        y=-y
    if(latitude[0]>latitude[_]):
        x=-x
    g.write('{},{}\n'.format(x,y))
g.close()