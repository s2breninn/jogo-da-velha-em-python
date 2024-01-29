# jogo-da-velha-em-python
Jogo da velha em Python utilizando POO - Programação Orientada a Objetos  

## Modelagem da classe:  

Para modelagem do tabuleiro foi utilizado três listas dentro de uma matriz  
Estrutura ilustrada para modelagem do tabuleiro do jogo:  
    ![image](https://github.com/s2breninn/jogo-da-velha-em-python/assets/89087720/43660bf8-dfa4-48f2-bfd3-5863cd014862)

### Descrições das Funções

1. __`print_board()`__:  

    Esta função imprime o tabuleiro vazio, sem nenhuma marcação.  
    ![image.png](attachment:image.png)  
  
2. __`reset()`__:  

    Esta função redefine o tabuleiro, removendo qualquer jogada anteriormente feita e restaurando-o para o estado inicial. Utiliza três listas aninhadas para representar a estrutura do tabuleiro.  

3. __`check_win_or_draw()`__:  

    Esta função verifica se há um vencedor utilizando oito condições diferentes, abrangendo vitórias verticais, horizontais e diagonais. Se um jogador vencer, a função exibe uma mensagem indicando o vencedor. Caso contrário, se não houver vencedor, verifica se ocorreu um empate.  
    
4. __`get_player_move()`__:  

    Esta função solicita que o jogador faça sua jogada, verificando se as coordenadas inseridas são válidas. Se as coordenadas forem inválidas (maiores que 2 ou menores que 0), uma mensagem será exibida ao jogador. Se a posição já estiver ocupada, a função informará que a posição já foi preenchida. Além disso, se forem inseridos caracteres não inteiros, uma mensagem será exibida pedindo para digitar apenas números.  
    
5. __`make_move()`__:  

    A função make_move percorre todas as listas da matriz utilizando uma list comprehension para determinar as posições vazias no tabuleiro. Em seguida, utilizando a biblioteca random e o método choice(), a função seleciona aleatoriamente uma posição para o computador jogar.
    
6. __Loop Principal__:

    O loop principal controla o fluxo do jogo. Ele limpa a tela do console, imprime o tabuleiro, e então inicia outro loop que continua até que o jogo termine. Dentro desse loop, o jogador faz sua jogada, o jogo verifica se houve um vencedor ou empate, e então é a vez do computador fazer sua jogada. Após cada jogada, o tabuleiro é impresso novamente e o jogo verifica se houve um vencedor ou empate. Após o fim do jogo, o jogador é solicitado a digitar '1' para sair do jogo ou qualquer outra tecla para jogar novamente. Se '1' for digitado, o loop principal é encerrado, caso contrário, o tabuleiro é redefinido para uma nova partida.
