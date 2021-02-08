from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubbleSort
from mergesort import merge_sort
from quickSort import quick_sort
root=Tk()
root.title("Sort Visualizer")
# widthXheight
root.maxsize(900,600)
data=[]

root.config(bg="black")
selected_alg=StringVar()
def draw_data(data,colorarray):
    canvas.delete("all")
    c_height=380
    c_width=600
    x_width=c_width/(len(data)+1) #width of bars/rectangle
    offset=30
    spacing=10
    normalizeDate=[i/max(data) for i in data]
    for i,height in enumerate(normalizeDate):
        # top-left
        x0=i*x_width+offset+spacing
        y0=c_height-height*340
        #bottom-right
        x1=(i+1)*x_width+offset
        y1=c_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorarray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]))
    root.update_idletasks()


def Generate():
    global data
    print("Generate" + selected_alg.get())
    minval=int(minEntry.get())
    maxval=int(maxEntry.get())
    size=int(sizeEntry.get())

    data=[]
    for _ in range(size):
        data.append(random.randrange(minval,maxval+1))
    draw_data(data,["yellow" for x in range(len(data))])
def StartAlgo():
   global data
   if not data:return
   if algMenu.get()=="Quick Sort":
       quick_sort(data,0,len(data)-1,draw_data,speedScale.get())

   if algMenu.get()=="Bubble Sort":
      bubbleSort(data,draw_data,speedScale.get())
   elif algMenu.get()=="Merge Sort":
       merge_sort(data,draw_data,speedScale.get())
   draw_data(data, ["yellow" for x in range(len(data))])
#Frame

UI_frame = Frame(root, width= 600, height=200, bg='#1B2853')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

#User Interface Area
#Row[0]
Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge Sort','Quick Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)
speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2,bg='white', orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgo, bg='red').grid(row=0, column=3, padx=5, pady=5)

sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL,bg='white', label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL,bg='white', label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL,bg='white', label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()

