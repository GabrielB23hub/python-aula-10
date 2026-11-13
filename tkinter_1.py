import tkinter as tk

janela = tk.Tk()
janela.title("Minha Janela")
janela.configure(bg="white")
janela.geometry("800x600")

cor_fundo = "white"

frame = tk.Frame(janela)
frame.pack(pady=100)
frame.configure(bg=cor_fundo)
frame.pack(padx=150, pady=100)

img = tk.PhotoImage(file="imagem.png")
img_label = tk.Label(frame, image=img, bg=cor_fundo)
img_label.pack(pady=20)


caixa1 = tk.Entry(frame)
caixa1.configure(font=("Arial", 16), text="e-mail", bg="lightgray", fg="white", relief="flat", bd=1, highlightthickness=0)
caixa1.pack(pady=10)

caixa2 = tk.Entry(frame)
caixa2.configure(font=("Arial", 16), text="senha", bg="lightgray", fg="white", relief="flat", bd=1, highlightthickness=0)
caixa2.pack(pady=10)

label = tk.Label(frame)
label.configure(font=("Arial", 16), text="ACESSAR", bg="#298FC2", fg="white", padx=70, pady=5, relief="solid")
label.pack()


janela.after(10000, janela.destroy)

janela.mainloop()

