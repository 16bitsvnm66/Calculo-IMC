def calcular_imc(peso, altura_cm): 
    

    altura_m = altura_cm / 100
    imc = peso / (altura_m ** 2)


    return imc


def classificação_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25<= imc < 30:
        return "Excesso de peso"
    else: 
        return "Obesidade"
    

def mostrar_total(imcs, classificações):
    total_consultas = len(imcs)
    media_imc = sum(imcs) / total_consultas

    print(f"Total de consultas realizadas: {total_consultas}")
    print(f"Média dos IMCs calculados: {media_imc: .2f}")
    

def classificação_mais_frequente(classificações):
     return max(set(classificações), key=classificações.count)  

def pedir_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))

            if valor <= 0:
                print("Erro! O valor deve ser maior que zero.")
            else:
                return valor

        except ValueError:
            print("Erro! Introduza apenas números.")

def main():
     imcs = []
     classificações = []
 
     print("Calculadora de IMC")
     print("---------------------------")

     peso = float(input("Introduzir o seu peso (kg):"))
     altura = float(input("Introduzir a sua altura (cm):"))

   
       
     imc = calcular_imc(peso, altura)

     classificação = classificação_imc(imc)

     print(f"Seu IMC é: {imc: .2f}")
     print(f"Classificação: {classificação}")
main()
