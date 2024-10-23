def pularLinha():
    print("\n\n#########################################################################################################################################################################\n")

parar = 0
escolha = -1

while escolha != parar:
    print("1) Sequencia de Fibonacci\n")

    print("2) Contador de letras A\n")

    print("3) Valor de SOMA\n")

    print("4) Descubra a lógica e complete o próximo elemento\n")

    print("5) Salas e Lampadas\n\n")

    escolha = int(input("Selecione a questão desejada:"))

    if escolha == 1:
        print("1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor\n"
            "sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...)\n"
            "escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de\n"
            "Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.\n\n" )

        fib1, fib2, soma = 0,1,0

        escolhido = int(input("Escolha o número para verificação: "))
        encontrado = False

        if (escolhido == 0):
            encontrado = True

        while soma < escolhido:
            soma = fib1 + fib2
            fib1 = fib2
            fib2 = soma
            # print(soma) #debug

            if(escolhido == soma):
                encontrado = True
                break

        if(encontrado):
            print("O número", escolhido, "está na lista")
        else:
            print("O número", escolhido, "não está na lista")

        pularLinha()

    #------------------------------------------------------------------------------------------------------------------------------------------

    elif escolha == 2:
        print("2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.")

        frase = input("Digite sua frase:\n")

            #Testes unitarios
        # qtdMinuscula = frase.count("a")
        # qtdMaiuscula = frase.count("A")
        # qtdGeral = frase.lower().count("a")
        # print(qtdMinuscula)
        # print(qtdMaiuscula)
        # print(qtdGeral)

        print("Na frase",frase, ", a letra 'a', seja maiuscula ou minuscula, aparece em um total de", frase.lower().count("a"), "vez(es).\nSendo", frase.count("a"), "minusculas e", frase.count("A"), "maisuculas.")

        pularLinha()

    #------------------------------------------------------------------------------------------------------------------------------------------

    elif escolha == 3:
        print("3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);\n"
        "Ao final do processamento, qual será o valor da variável SOMA?\n\n")

        INDICE = 12
        SOMA = 0 
        K = 1

        while(K < INDICE):
            K = K + 1
            SOMA = SOMA + K

        print("O resultado final da soma é:",SOMA)

        pularLinha()

    #------------------------------------------------------------------------------------------------------------------------------------------

    elif escolha == 4:
        print("4) Descubra a lógica e complete o próximo elemento:\n",
        "a) 1, 3, 5, 7, 9 •numeros impar\n",
        "b) 2, 4, 8, 16, 32, 64, 128 •2 elevado a n\n",
        "c) 0, 1, 4, 9, 16, 25, 36, 49 •ao quadrado\n",
        "d) 4, 16, 36, 64, 100 •ao quadrado numeros par\n",
        "e) 1, 1, 2, 3, 5, 8, 13 •sequencia de Fibonacci (Cola da primeira questão)\n",
        "f) 2, 10, 12, 16, 17, 18, 19, 200 •numeros começados com D?")

        pularLinha()

    #------------------------------------------------------------------------------------------------------------------------------------------

    elif escolha == 5:
        print("5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes.\n",
                "Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser.\n",
                "Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas\n"
                " idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?\n\n")

        print(" Ligar um interruptor 1 por bastante tempo, a ponto da lampada aquecer, em seguida, desliga-lo e ligar o segundo interruptor,\n",
            "assim, indo até as salas em duas idas, verificar a que está acesa e qual lampada está mais quente.\n",
            "A que estiver mais quente, foi o primeiro interruptor e o que não foi acesso é o da sala faltante.")

        pularLinha()

    #------------------------------------------------------------------------------------------------------------------------------------------

    elif escolha == 0:
        print("Encerrando programa")


    else:
        print("Opção inválida")