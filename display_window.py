from tkinter import Toplevel

class DisplayWindow(Toplevel):
    """
    CLASS FOR IMAGE WINDOW TO ALLOW FOR BORDLERLESS DRAGABLE FRAME
    """
    def __init__(self,master=None):
        Toplevel.__init__(self,master)
        self.overrideredirect(True)
        self._offsetx = 0
        self._offsety = 0
        self.bind('<Button-1>',self.clickwin)
        self.bind('<B1-Motion>',self.dragwin)

    def dragwin(self,event):
        x = self.winfo_pointerx() - self._offsetx
        y = self.winfo_pointery() - self._offsety
        self.geometry('+{x}+{y}'.format(x=x,y=y))

    def clickwin(self,event):
        self._offsetx = event.x
        self._offsety = event.y
