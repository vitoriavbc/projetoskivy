import random

def criar_tabuleiro():
    """Cria um tabuleiro vazio do jogo da velha"""
    return [" " for _ in range(9)]

def mostrar_tabuleiro(tabuleiro):
    """Exibe o tabuleiro na tela"""
    print("\n")
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("-----------")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("-----------")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print("\n")

def jogada_valida(tabuleiro, posicao):
    """Verifica se uma jogada é válida"""
    return tabuleiro[posicao] == " "

def fazer_jogada(tabuleiro, posicao, jogador):
    """Realiza uma jogada no tabuleiro"""
    if jogada_valida(tabuleiro, posicao):
        tabuleiro[posicao] = jogador
        return True
    return False

def verificar_vencedor(tabuleiro):
    """Verifica se há um vencedor ou empate"""
    # Linhas
    for i in range(0, 9, 3):
        if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] != " ":
            return tabuleiro[i]
    
    # Colunas
    for i in range(3):
        if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] != " ":
            return tabuleiro[i]
    
    # Diagonais
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] != " ":
        return tabuleiro[0]
    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] != " ":
        return tabuleiro[2]
    
    # Empate
    if " " not in tabuleiro:
        return "empate"
    
    return None

def jogada_ia(tabuleiro, jogador_ia):
    """IA faz sua jogada usando o algoritmo Minimax"""
    jogador_humano = "O" if jogador_ia == "X" else "X"
    
    def minimax(tabuleiro, profundidade, eh_maximizando):
        resultado = verificar_vencedor(tabuleiro)
        
        if resultado == jogador_ia:
            return 1
        elif resultado == jogador_humano:
            return -1
        elif resultado == "empate":
            return 0
            
        if eh_maximizando:
            melhor_pontuacao = -float("inf")
            for i in range(9):
                if tabuleiro[i] == " ":
                    tabuleiro[i] = jogador_ia
                    pontuacao = minimax(tabuleiro, profundidade + 1, False)
                    tabuleiro[i] = " "
                    melhor_pontuacao = max(pontuacao, melhor_pontuacao)
            return melhor_pontuacao
        else:
            melhor_pontuacao = float("inf")
            for i in range(9):
                if tabuleiro[i] == " ":
                    tabuleiro[i] = jogador_humano
                    pontuacao = minimax(tabuleiro, profundidade + 1, True)
                    tabuleiro[i] = " "
                    melhor_pontuacao = min(pontuacao, melhor_pontuacao)
            return melhor_pontuacao
    
    melhor_pontuacao = -float("inf")
    melhor_jogada = None
    
    for i in range(9):
        if tabuleiro[i] == " ":
            tabuleiro[i] = jogador_ia
            pontuacao = minimax(tabuleiro, 0, False)
            tabuleiro[i] = " "
            
            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                melhor_jogada = i
    
    fazer_jogada(tabuleiro, melhor_jogada, jogador_ia)
    return melhor_jogada

def jogar():
    """Função principal do jogo"""
    print("Bem-vindo ao Jogo da Velha contra a IA!")
    print("Posições do tabuleiro:")
    print(" 0 | 1 | 2 ")
    print("-----------")
    print(" 3 | 4 | 5 ")
    print("-----------")
    print(" 6 | 7 | 8 ")
    print("\n")
    
    # Escolher quem começa
    primeiro = input("Você quer jogar primeiro? (s/n): ").lower()
    jogador_humano = "X" if primeiro == "s" else "O"
    jogador_ia = "O" if jogador_humano == "X" else "X"
    
    tabuleiro = criar_tabuleiro()
    
    if jogador_humano == "X":
        mostrar_tabuleiro(tabuleiro)
    
    while True:
        # Jogada do humano
        if jogador_humano == "X" or " " in tabuleiro:
            try:
                posicao = int(input("Escolha uma posição (0-8): "))
                if posicao < 0 or posicao > 8:
                    print("Posição inválida! Escolha entre 0 e 8.")
                    continue
                
                if not fazer_jogada(tabuleiro, posicao, jogador_humano):
                    print("Posição já ocupada! Escolha outra.")
                    continue
            except ValueError:
                print("Entrada inválida! Digite um número entre 0 e 8.")
                continue
            
            mostrar_tabuleiro(tabuleiro)
            
            vencedor = verificar_vencedor(tabuleiro)
            if vencedor:
                if vencedor == jogador_humano:
                    print("Parabéns! Você venceu!")
                else:
                    print("Empate!")
                break
        
        # Jogada da IA
        if jogador_ia == "X" or " " in tabuleiro:
            print("IA está pensando...")
            jogada_ia(tabuleiro, jogador_ia)
            mostrar_tabuleiro(tabuleiro)
            
            vencedor = verificar_vencedor(tabuleiro)
            if vencedor:
                if vencedor == jogador_ia:
                    print("A IA venceu! Tente novamente.")
                else:
                    print("Empate!")
                break

if __name__ == "__main__":
    jogar()