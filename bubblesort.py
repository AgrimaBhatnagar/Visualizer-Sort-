import time

def bubbleSort(data,draw_data,timeClick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
            draw_data(data,["blue" if x==j or x==j+1 else "yellow" for x in range(len(data))])
            time.sleep(timeClick)
    draw_data(data,["purple" for i in range(len(data))])