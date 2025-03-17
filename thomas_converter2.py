import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image

def compress_image(input_path, output_path, quality):
    try:
        img = Image.open(input_path)
        img.save(output_path, quality=quality, optimize=True)
        messagebox.showinfo("Succès", f"Image compressée enregistrée : {output_path}\nQualité choisie : {quality}/100")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la compression : {e}")

def convert_to_png(input_path, output_path):
    try:
        img = Image.open(input_path)
        img.save(output_path, format="PNG")
        messagebox.showinfo("Succès", f"Image convertie en PNG : {output_path}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la conversion : {e}")

def select_file(action):
    
    file_path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if not file_path:
        return
    
    output_folder = os.path.dirname(file_path)
    filename, ext = os.path.splitext(os.path.basename(file_path))
    
    if action == "compress":
        quality = simpledialog.askinteger(
            "Qualité de compression", 
            "Entrez un niveau de qualité (1-100) :\n\n1 = Forte compression, petite taille, perte de qualité\n100 = Faible compression, grande taille, meilleure qualité",
            minvalue=1, maxvalue=100
        )
        if quality is None:
            return
        output_path = os.path.join(output_folder, f"{filename}_compressed.jpg")
        compress_image(file_path, output_path, quality)
    elif action == "convert":
        output_path = os.path.join(output_folder, f"{filename}.png")
        convert_to_png(file_path, output_path)

def create_gui():
    
    root = tk.Tk()
    root.title("Converter")
    root.geometry("300x150")
    root.resizable(False, False)
    
    label = tk.Label(root, text="Thomas Converter", font=("Arial", 14, "bold"))
    label.pack(pady=10)
    
    compress_btn = tk.Button(root, text="Compresser une image", command=lambda: select_file("compress"))
    compress_btn.pack(pady=5)
    
    convert_btn = tk.Button(root, text="Convertir en PNG", command=lambda: select_file("convert"))
    convert_btn.pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
    
   
    
