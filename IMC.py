def calcular_imc(peso: float, altura_cm: float) -> float:
    

    altura_m = altura_cm / 100
    imc = peso / (altura_m * altura_m)

    return imc


