import tkinter as tk

janela = tk.Tk()
janela.title("Minha Janela")
janela.configure(bg="white")
janela.geometry("1024x754")

cor_fundo = "white"

frame = tk.Frame(janela)
frame.pack(pady=100)
frame.configure(bg=cor_fundo, padx=50, pady=100)

img = tk.PhotoImage(file="image.png")
label_img = tk.Label(frame, image=img, bg=cor_fundo)
label_img.pack(pady=10)

caixa1 = tk.Entry(frame)
caixa1.configure(font=("Arial", 16), text="e-mail", bg="white", fg="white", relief="flat")
caixa1.pack(pady=10)

caixa1 = tk.Entry(frame)
caixa1.configure(font=("Arial", 16), text="senha", bg="white", fg="white", relief="flat")
caixa1.pack(pady=10)

label = tk.Label(frame)
label.configure(font=("Arial", 16), text="Entrar", bg="#298FC2", fg="white", padx=20, pady=20, relief="solid")
label.pack()


janela.after(10000, janela.destroy)

janela.mainloop()

