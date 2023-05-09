import os

import sys
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

class game:
    def __init__(self):
        root = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font14 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("1000x800+600+150")
        root.title("The Games")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")



        self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.96, relwidth=0.99)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)

        self.Message5 = Message(self.Frame1)
        self.Message5.place(relx=0.09, rely=0.11, relheight=0.15, relwidth=0.86)
        self.Message5.configure(background="#d9d9d9")
        self.Message5.configure(font=font14)
        self.Message5.configure(foreground="#000000")
        self.Message5.configure(highlightbackground="#d9d9d9")
        self.Message5.configure(highlightcolor="black")
        self.Message5.configure(text='''Use arrow Keys to Play 2048 & snakes''')
        self.Message5.configure(width=791)

        self.Message7 = Message(self.Frame1)
        self.Message7.place(relx=0.09, rely=0.21, relheight=0.15, relwidth=0.86)
        self.Message7.configure(background="#d9d9d9")
        self.Message7.configure(font=font14)
        self.Message7.configure(foreground="#000000")
        self.Message7.configure(highlightbackground="#d9d9d9")
        self.Message7.configure(highlightcolor="black")
        self.Message7.configure(text='''Use Mouse button to to Play Tic Tac Toe''')
        self.Message7.configure(width=791)

        self.Message1 = Message(self.Frame1)
        self.Message1.place(relx=0.01, rely=0.31, relheight=0.15, relwidth=0.90)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(font=font14)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''2048 Rules
        - Merge same numbers to get 2048
        - You can still play the game after you form 2048 to get more highscores''')
        self.Message1.configure(width=791)

        self.Message2 = Message(self.Frame1)
        self.Message2.place(relx=0.01, rely=0.51, relheight=0.15, relwidth=0.90)
        self.Message2.configure(background="#d9d9d9")
        self.Message2.configure(font=font14)
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''Snakes Rule
        - Use arrow keys to move your snake around and eat food
        - The more it eats, the more it grows
        - The more it grows,tougher the games get''')
        self.Message2.configure(width=791)

        self.Message3 = Message(self.Frame1)
        self.Message3.place(relx=0.01, rely=0.71, relheight=0.20, relwidth=0.90)
        self.Message3.configure(background="#d9d9d9")
        self.Message3.configure(font=font14)
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(text='''Tic Tac Toe Rule
        - Use mouse left click to play this game
        - Player one is X
        - Player two is O
        - First who makes a line of X or O will win''')
        self.Message3.configure(width=791)

        root.mainloop()

if __name__ == '__main__':
   game()