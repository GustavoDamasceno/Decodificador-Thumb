# Decodificador

## Introdução

Este trabalho consiste em implementar um programa (em python) que decodifique um código Thumb em seu respectivo mapa de memória. 
O decodificador deverá receber como entrada um arquivo de texto contendo o código a ser executado, em Thumb, e retornar seu respectivo mapa de memória. O arquivo de saída deve representar a memória de programa, onde cada linha corresponde a um endereço com alinhamento de 32 bits, no formato:              
                                 
 				                    <endereço>:<conteúdo>

O programa deve também executar até encontrar um loop com a instrução “b .” OU uma instrução de formato indefinido. Além de tudo, o programa deverá ler a entrada de um arquivo.s e salvar o resultado em um arquivo.out
Vale ressaltar que o trabalho foi baseado na tabela abaixo:

## Saída

![](https://pbs.twimg.com/media/EK-anAOWsAAnjh7?format=png&name=small)