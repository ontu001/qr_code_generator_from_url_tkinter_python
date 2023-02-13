import qrcode
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def generate_qr_code():
    url = entry.get()
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    img.save(file_path)
    messagebox.showinfo("Success", "QR code generated successfully")

root = tk.Tk()
root.title("QR Code Generator")

frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, text="Enter URL: ")
label.pack(side=tk.LEFT)

entry = tk.Entry(frame)
entry.pack(side=tk.LEFT)

generate_button = tk.Button(frame, text="Generate", command=generate_qr_code)
generate_button.pack(side=tk.LEFT)

root.mainloop()
