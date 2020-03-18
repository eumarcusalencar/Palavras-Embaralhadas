import random
# adicione a lista as palavra de sua preferencia /// add your preferred words to the list
lista_embaralhada = ["oogelg","gleeaaidr","claavo","ols","obla","ythnop"]
lista_certa = ["google","geladeira","cavalo","sol","bola","python"]
numero = random.randint(0,5)
verdade = lista_certa[numero]

tentativa = 1
chute = input("como voce acha que ficaria esta palavra escrita da forma correta ? a palavra embaralhada é:\n"+lista_embaralhada[numero]+"\n")  


if chute == verdade:
    print(f" parabens vc acertou com {tentativa}ª tentativas a palavra correta foi {verdade}")
    
while chute != verdade:
    print(f"[Você errou, tente de novo] \n[voce tem {tentativa}(s)ª chances]")
    chute = input("como vc acha que ficaria esta palavra escrita da forma correta? a palavra embaralhada é:\n"+lista_embaralhada[numero]+"\n")
    tentativa +=1
    
    #limite tentativas /// tentativas claras
    if tentativa > 6:
        print (" voce perdeu, limite de tentativas foi ultrapassado")
        break
    elif chute == verdade:
        print(f" parabens vc acertou com {tentativa}ª tentativas a palavra correta foi {verdade}")
        break
