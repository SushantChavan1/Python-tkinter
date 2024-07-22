import tkinter as tk

# Create a tkinter window
root = tk.Tk()
root.title("Kids' House")

# Create a canvas widget
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Draw the main house structure (rectangle)
house = canvas.create_rectangle(50, 200, 250, 100, outline='black', fill='lightblue')

# Draw the roof (triangle)
roof = canvas.create_polygon(50, 100, 150, 20, 250, 100, outline='black', fill='orange')

# Draw windows (rectangles)
window1 = canvas.create_rectangle(75, 150, 105, 120, outline='black', fill='white')
window2 = canvas.create_rectangle(175, 150, 205, 120, outline='black', fill='white')

# Draw door (rectangle)
door = canvas.create_rectangle(125, 200, 175, 150, outline='black', fill='brown')

# Run the tkinter main loop
root.mainloop()
