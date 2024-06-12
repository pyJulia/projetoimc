import tkinter as tk
from tkinter import messagebox


#calcular o IMC
def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura ** 2)
        resultado = f'Seu IMC é {imc:.1f}\n'
        if imc < 18.5:
            status = 'Você está abaixo do peso normal.'
        elif 18.5 <= imc < 25:
            status = 'Você está com o peso ideal.'
        elif 25 <= imc < 30:
            status = 'Você está em SOBREPESO.'
        elif 30 <= imc < 40:
            status = 'Você está em OBESIDADE, cuidado!'
        elif imc >= 40:
            status = 'Você está em OBESIDADE MÓRBIDA, cuidado!'
        resultado += status
        messagebox.showinfo("Resultado do IMC", resultado)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")


#criar a janela
root = tk.Tk()
root.title("Calculadora de IMC")

# Criação dos widgets
label_peso = tk.Label(root, text="Qual é o seu peso? (Kg)")
label_peso.pack()
entry_peso = tk.Entry(root)
entry_peso.pack()

label_altura = tk.Label(root, text="Qual é a sua altura? (m)")
label_altura.pack()
entry_altura = tk.Entry(root)
entry_altura.pack()

button_calcular = tk.Button(root, text="Calcular IMC", command=calcular_imc)
button_calcular.pack()


root.mainloop()
