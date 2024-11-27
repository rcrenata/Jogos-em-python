import random

def escolher_palavra():
    palavras = ["onça", "macaco", "preguiça", "cutia", "capivara", "tucano", "tracajá", "cobra", "arara", "tambaqui", "tucunaré"]
    return random.choice(palavras)

def forca():
    palavra = escolher_palavra()
    letras_corretas = ["_"] * len(palavra)
    tentativas = 6
    letras_erradas = []

    while tentativas > 0 and "_" in letras_corretas:  
        print("\nPalavra:", " ".join(letras_corretas))
        print("Tentativas restantes:", tentativas)
        print("Letras erradas:", ", ".join(letras_erradas))

        letra = input("Digite uma letra: ").lower()

        if letra in letras_erradas or letra in letras_corretas:
            print("Você já tentou essa letra. Tente outra.")
            continue  # Volta para o início do loop

        if letra in palavra: 
            for i in range(len(palavra)):  
                if palavra[i] == letra:
                    letras_corretas[i] = letra
        else:
            tentativas -= 1 
            letras_erradas.append(letra)

    # Condição final: venceu ou perdeu
    if "_" not in letras_corretas:
        print("\nParabéns! Você acertou a palavra:", palavra)
    else:
        print("\nVocê perdeu! A palavra era:", palavra)

# Chama a função para iniciar o jogo
forca()
