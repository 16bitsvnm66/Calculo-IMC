def calcular_imc(peso, altura_cm):
    

    altura_m = altura_cm / 100
    imc = peso / (altura_m ** 2)

    return imc


def verificar_peso(imc: float) -> str:
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25<= imc < 30:
        return "Sobrepeso"
    else: 
        return "Obesidade"
    
if __name__ == "__main__":

    print("Calculadora de IMC")
    print("---------------------------")

    try:
       
        peso = float(input("Introduza o peso (kg): "))
        altura = float(input("Introduza a altura (cm): "))

        imc = calcular_imc(peso, altura)

        resultado = verificar_peso(imc)

        print(f"\nIMC: {imc:.1f}")
        print(resultado)
    

    except ValueError:
        print("Por favor, introduza valores numéricos válidos para peso e altura.")

    except ZeroDivisionError:
        print("A altura não pode ser zero.")