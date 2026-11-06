import tkinter as tk

janela = tk.Tk()
janela.title("Minha Janela")
janela.configure(bg="white")
janela.geometry("400x300")

frame = tk.Frame(janela)
frame.pack(pady=50)
frame.configure(bg="lightblue", padx=20, pady=20)

botao = tk.Button(frame, text="Clique Aqui", command=lambda: print("Botão clicado!"))
botao.pack()



rotulo = tk.Label(frame, text="Olá, Mundo!")
rotulo.pack()

janela.mainloop()