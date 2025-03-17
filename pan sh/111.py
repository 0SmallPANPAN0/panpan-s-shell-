from tkinter import *

if __name__ == '__main__':
    TRANSCOLOUR = 'gray'
    tk = Tk()
    tk.geometry('500x400+500+150')
    tk.title('')

    canvas = Canvas(tk)
    canvas.pack(fill=BOTH, expand=Y)

    canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), fill=TRANSCOLOUR, outline=TRANSCOLOUR)
    TRANSCOLOUR = 'gray'
    tk.wm_attributes('-transparentcolor', TRANSCOLOUR)
    canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), fill=TRANSCOLOUR, outline=TRANSCOLOUR)
    def on_resize(evt):
        tk.configure(width=evt.width, height=evt.height)
        canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), fill=TRANSCOLOUR,
                                outline=TRANSCOLOUR)
        print(canvas.winfo_width())
    tk.bind('<Configure>', on_resize)
    tk.mainloop()


