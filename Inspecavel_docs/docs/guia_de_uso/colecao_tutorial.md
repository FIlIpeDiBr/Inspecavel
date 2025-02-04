# Coleção

Após a conclusão da detecção, na lista de inspeções em aberto (elemento 4a da [lista de inspeção](index.md#listagem-de-inspecoes)), a inspeção possui agora o estágio de "Coleção". Clicar nesse botão ira te redirecionar para a tela de coleção:

![Tela de Coleção](../assets/tutoriais/tela-colecao.png"Tela de coleção")

## Título

> Elemento 1

É o título da inspeção, seguido de sua etapa atual, que neste caso é "Coleção".

## Lista de Discrepâncias

> Elemento 2

É a lista detalhada de todas as discrepâncias submetidas para esta inspeção, descrita a seguir.

### Localização Geral

> Elemento 2a

Lista a localização geral de cada discrepância submetida.

### Localização Específica

> Elemento 2b

Lista a localização específica de cada discrepância submetida.

### Descrição

> Elemento 2c

Lista a descrição atribuida a cada discrepância submetida.

### Tipo

> Elemento 2d

Lista o tipo de cada discrepância submetida.

## Agrupar

> Elemento 3

Este botão define a discrepância correspondente como a principal e redireciona para a página de agrupamento. Aqui você deve selecionar todas as discrepâncias repetidas, que tratam de uma mesma questão ou que de alguma maneira pertençam a um mesmo agrupamento.

Esse também é o momento para agrupar as discrepâncias incorretas ou mal formatadas, visto que <ins>as discrepâncias _não_ podem ser apagadas</ins>.

Para selecionar mais de uma discrepância você pode segurar as teclas "shift" ou "ctrl", da mesma maneira realizada durante a seleção de inspetores na seção de [inspetores](criar_inspecao.md#inspetores).

Há também a possibilidade de não selecionar nenhuma outra discrepância "repetida" para associar à principal caso esta seja uma ocorrência única, mas <ins>todas</ins> as discrepâncias devem ser agrupadas.

## Discrepâncias Filtradas

> Elemento 4

Ainda não foi implementado. Não possui funcionalidade alguma até o presente momento.

## Cancelar Inspeção

> Elemento 5

Este botão requer confirmação. Em caso positivo, encerra a inspeção, impedindo novas submissões e qualquer manipulação a ela.
<!-- Depois altere o nome (id) das inspeções canceladas para possibilitar o reuso -->

A inspeção _não_ será apagada e seu registro ainda constará entre as concluídas.

## Agrupamento

Ao pressionar o botão de agrupar (elemento 3), o monitor será redirecionado para a tela de agrupamento. 

## Como Concluir a Coleção?

Diferente das demais etapas, a coleção não disponibiliza um método para finalizar a etapa. Quando todas as discrepâncias forem agrupadas o sistema encerrará a etapa e irá redirecionar para a de [discrimiação](discriminacao_tutorial.md).

O inspetor pode, sempre que desejar, sair e retornar à tela de coleção. Todo o progresso será registrado e ele sempre irá retornar ao estado em que deixou.