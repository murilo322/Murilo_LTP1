import tkinter as tk

 

def mostrar_mensagem():

    label.config(text="ola, iesgo!")

 

janela = tk.Tk()
janela.title("exemplo de gui em python")


#criar um rotulo
label = tk.Label(janela, text="bem vindo a interface do usuario")
label.pack(padx= 10, pady=10)

#criar um botão do tipo CTA (call to action)
botao = tk.Button(janela, text="clique aqui!", command=mostrar_mensagem)
botao.pack(padx=10, pady=10)
botao.config(width=15, height=20)

#iniciar a gui em loop
janela.mainloop()