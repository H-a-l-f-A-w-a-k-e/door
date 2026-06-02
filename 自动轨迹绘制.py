# AutoTraceDraw.py
import turtle as t

t.title('自动轨迹绘制')
t.setup(800,600,0,0)
t.pencolor('red')
t.pensize(5)
dls=[]
with open(r"D:\python_start\data.txt") as f:
    for line in f:
        line=line.replace('\n','')
        dls.append(list(map(eval,line.split(','))))

for i in range(len(dls)):
    t.pencolor(dls[i][3],dls[i][4],dls[i][5])
    t.forward(dls[i][0])
    if dls[i][1]:
        t.right(dls[i][2])
    else:
        t.left(dls[i][2])