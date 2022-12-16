#   curiosa xeretano meu cod ZZZzzZZZ
#!/usr/bin/python
# coding: utf-8

import time
import sys
import os
banner = (r"""
    ███╗   ███╗ ██████╗ ███╗   ███╗ ██████╗ ██████╗ 
    ████╗ ████║██╔═══██╗████╗ ████║██╔═══██╗██╔══██╗
    ██╔████╔██║██║   ██║██╔████╔██║██║   ██║██████╔╝
    ██║╚██╔╝██║██║   ██║██║╚██╔╝██║██║   ██║██╔══██╗
    ██║ ╚═╝ ██║╚██████╔╝██║ ╚═╝ ██║╚██████╔╝██║  ██║
    ╚═╝     ╚═╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝
    ~~~~~~~~ top motivos para amar-te ~~~~~~~~                                                
""")
print(banner)

x = input("Escolha um número natural de 1 a 50: ")
while (int(x) <=50):
    if x=="1":
        print('\n1 - Eu te amo pq vc me faz sorrir\n')
    elif x=="2":
        print('\n2 - Eu te amo pq vc tem olhos brilhantes\n')
    elif x=="3":
        print('\n3 - Eu te amo pq vc consegue me acalmar\n')
    elif x=="4":
        print('\n4 - Vc consegue me inspirar, mesmo em meus piores momentos\n')
    elif x=="5":
        print('\n5 - Brilho muito, mas vc me ofusca \isso n eh ruim/\n')
    elif x=="6":
        print('\n6 - Amo nossos assuntos extremamente abstratos sobre tudo\n')
    elif x=="7":
        print('\n7 - Vc sempre é muito atenciosa cmg, 87%\n')
    elif x=="8":
        print('\n8 - Vc me apresenta a luz quando nao penso direito\n')
    elif x=="9":
        print('\n9 - AMO suas fofocas\n')
    elif x=="10":
        print('\n10 - Eu te amo pq vc é muito pura :D\n')
    elif x=="11":
        print('\n11 - Amo qnd vc rouba meus bordoes,\nparece uma patinha quackquack\n')
    elif x=="12":
        print('\n12 - Amo a sua maneira de pensar, a sua organização e intuição\n')
    elif x=="13":
        print('\n13 - Eu te amo porque voce nn tem favoritismo político\n')
    elif x=="14":
        print('\n14 - Amo qnd vc me inclui em seus planos\n')
    elif x=="15":
        print('\n15 - Eu te amo pq vc é original, vc sendo vc, apenas vc\n')
    elif x=="16":
        print('\n16 - Tenho maior orgulho de suas conquistas\n')
    elif x=="17":
        print('\n17 - Amo vê-la feliz, animada com algo \n')
    elif x=="18":
        print('\n18 - Amo quando vc cita várias fontes diferentes de diversas áreas,\ncomo uma polímata\n')
    elif x=="19":
        print('\n19 - Amo suas crises de fofura, mds mt fof\n')
    elif x=="20":
        print('\n20 - Vc é mt estilosa, nss. "I believe in Mirela Supremacy!!1".\n')
    elif x=="21":
        print('\n21 - EXTREMAMENTE LINDA, EDUcADA, XEROSA, ALEGRE, MDS AMO Vc.\n')
    elif x=="22":
        print('\n22 - Eu te amo por vc nao ser uma pessoa polarizada, perfff\n')
    elif x=="23":
        print('\n23 - Eu te amo pq vc me apoia em td, vc me ajuda até qnd nao mereço.\n')
    elif x=="24":
        print('\n24 - Vc n sente vergonha di eu\n')
    elif x=="25":
        print('\n25 - Acho q já disse, mas eu sou seu admirador n°1.\n')
    elif x=="26":
        print('\n26 - Amo qnd vc ri das minhas piadocas idiotas.. Acho incrível\n')
    elif x=="27":
        print('\n27 - Você é a própria definiçao de perfeição.\n')
    elif x=="28":
        print('\n28 - Eu amo sua determinação, tudo oq vc quer, vc consegue!!\n')
    elif x=="29":
        print('\n29 - Eu te amo por ser saudável kkjm\n')
    elif x=="30":
        print('\n30 - Amo qnd vc passa a mao nos meus cachinhoss *-*\n')
    elif x=="31":
        print('\n31 - Eu te amo por ser realista-otimista.\n')
    elif x=="32":
        print('\n32 - Eu te amo por ser momorosa cmg.. <3\n')
    elif x=="33":
        print('\n33 - Vc respeita meu espaço..\n')
    elif x=="34":
        print('\n34 - Apesar de preferir nao discutir,\namo amadurecer cntg e aprender a respeitar.\n')
    elif x=="35":
        print('\n35 - Amo qnd vc visualiza qualidades que nao vejo em mim..\n')
    elif x=="36":
        print('\n36 - Amo saber q posso confiar em vc\n')
    elif x=="37":
        print('\n37 - Fico feliz quando vc me entende \n')
    elif x=="38":
        print('\n38 - AMO dividir meu tempo contigo\n')
    elif x=="39":
        print('\n39 - Adoro assistir filmes com vc, até qnd são ruins.\n')
    elif x=="40":
        print('\n40 - Vc me inspira (eu ja disse isso?)\n')
    elif x=="41":
        print('\n41 - Adoro suas soluções de problemas, ou sao ótimas, ou sao geniais.\n')
    elif x=="42":
        print('\n42 - AMO a nossa cONEXAO, compartilhamos muitas similaridades.\n')
    elif x=="43":
        print('\n43 - Sua comapanhia me faz feliz\n')
    elif x=="44":
        print('\n44 - Amo aprender com vc, vc só diz coisas interessantes.\n')
    elif x=="45":
        print('\n45 - Fico surpreendido com suas análises, sua compreensão,\neu te acho muito inteligente.\n')
    elif x=="46":
        print('\n46 - Amo suas reações genuínas, vc n tem q forçar nada\n')
    elif x=="47":
        print('\n47 - Amo jogar com vc\n')
    elif x=="48":
        print('\n48 - Adoro qnd vc é arrogante (na medida certa)\n')
    elif x=="49":
        print('\n49 - Amo qnd vc compartilha/fala sobre TODOS os seus gostos cmg\n')
    elif x=="50":
        print('\n50 - Vc está numa posição hierarquica muito alta em minha vida,\n eu tenho prazer te tê-la ao meu lado,\n vc merece tudo o que é bom.\nEu espero ser pelo menos metade do que vc é para mim..\n')
    x = input("Escolha um número natural de 1 a 50: ")    
