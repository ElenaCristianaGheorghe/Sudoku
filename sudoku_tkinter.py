from tkinter import *
from tkinter.ttk import *
from time import *
from tkinter import messagebox
from sudoku_backtracking import unsolved, solved

class Sudoku():

    def __init__(self, unsolved_bo, solved_bo):
        '''param unsolved_bo: 2d lists of ints
        param solved_bo: 2d lists of ints'''

        self.root = Tk()
        self.root.title("Sudoku")
        self.unsolved_bo = unsolved_bo
        self.solved_bo = solved_bo
        self.create_gui()
        self.root.mainloop()

    def create_gui(self):
        '''It initializes all the components of the graphic user interface.'''

        for i in range(len(self.unsolved_bo)):
            for j in range(len(self.unsolved_bo[0])):
                if self.unsolved_bo[i][j] != 0:
                    self.widget = Label(self.root,
                                text = str(self.unsolved_bo[i][j]), width=7,
                                anchor="center", background="LavenderBlush3")
                else:
                    self.sv = StringVar()
                    self.widget = Entry(self.root, width=7, textvariable=self.sv)
                    self.sv.trace("w", lambda name, index, mode, sv=self.sv,
                                    widget=self.widget: self.get_input(sv, widget))
                self.boxes_separation(self.widget, i, j)

        self.min = 9
        self.sec = 59
        self.timer_str = StringVar()
        self.timer_str.set(f"{self.min}:{self.sec}")
        self.timer_label = Label(self.root, textvariable=self.timer_str,
                        background="LavenderBlush3", width = 25, anchor="center")
        self.timer_label.grid(row=9, column=2, columnspan=5, pady=20, padx=20)
        self.timer(self.min, self.sec)

    def boxes_separation(self, widget, r, c):
        '''It generates the spaces between the components of the GUI in a way
        that the elements of the puzzle are grouped nine by nine and
        places them in their spots.
        param widget: Tk() object
        param r: int
        param c: int'''

        if (r % 3 == 0 and r  != 0):
            widget.grid(row=r, column=c,pady=(20, 0))
        if c % 3 == 0 and c != 0:
             widget.grid(row=r, column=c,padx=(20, 0))
        else:
            widget.grid(row=r, column=c)

    def get_input(self, sv, widget):
        '''It gets the user's input in order to verify it with self.check_val()
        function.
        param sv: string
        param widget: Tk() object'''

        input = sv.get()
        info = widget.grid_info()
        r, c = info['row'], info['column']
        self.check_val(r,c,input,widget)

    def check_val(self, row, col, value, widget):
        '''It verifies if the user's input corresponds to the value from
        the self.solved_bo[row][col]. If those two correspond the Entry box is
        transfromed into a Label and self.unsolved_bo[row][col] is changed with
        the input.
        param row: int
        param col: int
        param value: int
        param widget: Tk() object'''

        if value != "" and self.solved_bo[row][col] == int(value):
            widget = Label(self.root, text = value, width=7, anchor="center")
            self.boxes_separation(widget, row, col)
            self.unsolved_bo[row][col] = value

    def timer(self, m, s):
        '''It initializes a timer at the bottom of the GUI.
        param m: int
        param s: int'''
        if s in [0,1,2,3,4,5,6,7,8,9]:
            self.timer_str.set(f"{m}:0{s}")
        else:
            self.timer_str.set(f"{m}:{s}")
        s -= 1
        if s == -1 and m == 0:
            self.timer_str.set(f"{m}:00")
            messagebox.showinfo("", 'Timpul a expirat!')
            return
        if s == -1:
            m -= 1
            s = 59
        if self.check_for_empties() is None:
            self.timer_str.set(f"{m}:{s}")
            messagebox.showinfo("", 'You have won!')
            return
        self.timer_label.after(1000, lambda m=m, s=s: self.timer(m, s))

    def check_for_empties(self):
        '''It checks for empty spots in the self.unsolved_bo which must be
        filled in.
        It returns True if there are empty boxes else returns None. '''

        for list in self.unsolved_bo:
            if 0 in list:
                return True
        return

#======================================

unsolved_bo = list(map(list, unsolved))
solved_bo = list(map(list, solved))

sudoku = Sudoku(unsolved_bo, solved_bo)
