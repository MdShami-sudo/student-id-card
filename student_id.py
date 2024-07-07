import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk, ImageDraw

student_name = "MD Shami"
student_age = "15"
student_bg =  "O+"
student_phone =  "+1234567890"
student_address = "123, Elm Street, Springfield"

root = tk.Tk()
root.title("Student ID Card")
root.geometry("400x250")

def create_gradient_background():
    width, height = 400, 250
    image = Image.new("RGB", (width, height), "#FFFFFF")
    draw = ImageDraw.Draw(image)

    start_color = (0, 128, 255)  
    end_color = (0, 255, 128)   

    for i in range(height):
        ratio = i / height
        r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
        g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
        b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
        draw.line([(0, i), (width, i)], fill=(r, g, b))
    
    return image

gradient_image = create_gradient_background()

background_image = ImageTk.PhotoImage(gradient_image)

card_canvas = Canvas(root, width=400, height=250)
card_canvas.pack()

card_canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

card_canvas.create_text(200, 30, text="Student ID Card", font=("Helvetica", 24, "bold"), fill="white")
card_canvas.create_text(50, 70, text="Name:", anchor=tk.W, font=("Helvetica", 14), fill="white")
card_canvas.create_text(150, 70, text=student_name, anchor=tk.W, font=("Helvetica", 14, "bold"), fill="white")
card_canvas.create_text(50, 100, text="Age:", anchor=tk.W, font=("Helvetica", 14), fill="white")
card_canvas.create_text(150, 100, text=student_age, anchor=tk.W, font=("Helvetica", 14, "bold"), fill="white")
card_canvas.create_text(50, 130, text="Blood Group:", anchor=tk.W, font=("Helvetica", 14), fill="white")
card_canvas.create_text(150, 130, text=student_bg, anchor=tk.W, font=("Helvetica", 14, "bold"), fill="white")
card_canvas.create_text(50, 160, text="Phone No:", anchor=tk.W, font=("Helvetica", 14), fill="white")
card_canvas.create_text(150, 160, text=student_phone, anchor=tk.W, font=("Helvetica", 14, "bold"), fill="white")
card_canvas.create_text(50, 190, text="Address:", anchor=tk.W, font=("Helvetica", 14), fill="white")
card_canvas.create_text(150, 190, text=student_address, anchor=tk.W, font=("Helvetica", 14, "bold"), fill="white", width=200)

root.mainloop()
