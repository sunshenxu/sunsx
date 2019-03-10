import tkinter
from treeWindows import TreeWindows
from infoWindows import InfoWindows


win = tkinter.Tk()
win.title("sunsx")
win.geometry("600x400+500+200")
iw = InfoWindows(win)
tw = TreeWindows(win,iw)


win.mainloop()