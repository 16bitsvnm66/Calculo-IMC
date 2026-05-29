def calcular_imc(peso: float, altura_cm: float) -> float:
    

    altura_m = altura_cm / 100
    imc = peso / (altura_m * altura_m)

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
