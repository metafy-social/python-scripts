# Digital Clock
## code
```
import tkinter
from time import strftime

top = tkinter.Tk()
top.title('Digital Clock')
top.resizable(0,0)

def time():
    string = strftime('%H: %M: %S %p')
    clockTime.config(text=string)
    clockTime.after(1000, time)

clockTime = tkinter.Label(top, font=('courier new', 40),
background='white',foreground='black')
clockTime.pack(anchor='center')
time()
top.mainloop()

```

![Screenshot 2022-10-04 195233](https://user-images.githubusercontent.com/104223444/193844936-aee558c0-6b43-4096-9b9c-cc3ef23a29ed.png)
