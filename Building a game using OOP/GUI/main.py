from tkinter import *
import settings
from cell import Cell
import utils


root = Tk()
# Window Settings
root.configure(bg="black")
root.geometry('1440x720')
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root, 
    bg="black", 
    width=settings.WIDTH, 
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root, 
    bg="black", 
    width=utils.width_prct(25), 
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(75),
    height=utils.height_prct(75),
)
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column = x, row = y
        )


# https://www.youtube.com/watch?v=K-7Zkgpbi9Q&list=PLOkVupluCIjsyLs2lHL7M3ZubAxH10WHB&index=2



# Runs window
root.mainloop()