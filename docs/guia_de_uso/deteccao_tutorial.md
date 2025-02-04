# Detecção

O trabalho realizado nesta etapa fica primariamente a cargo dos inspetores designados ([tutorial para inspetores](criar_inspecao.md)), cabendo ao monitor acompanhar as submissões e determinar o fim da etapa. Para isso existe a tela de detecção do inspetor.

Para acessar esta funcionalidade, basta clicar em uma das inspeções em aberto que tenha o status de "Detecção" no botão de estágio (elemento 4a da [lista de inspeção](index.md#listagem-de-inspecoes)) e você será redirecionado para a tela de detecção:

![Monitorar Detecção](../assets/tutoriais/tela-deteccao-monitor.png"Tela de detecção do monitor")

## Título

> Elemento 1

É o título da inspeção, seguido de sua etapa atual, que neste caso é "Detecção".

## Discrepâncias Submetidas

> Elemento 2

É a lista com o número de discrepâncias totais e por inspetor submetidas até o momento. Por motivos de lisura do processo, _não_ é possível visualizar as discrepâncias antes do fim desta etapa.

Ela traz: o nome do inspetor que submeteu (_elemento a_), a quantidade de discrepâncias submetidas por ele (_elemento b_) e o númeto de submissões total (_elemento c_).

Embora a lista receba dados atualizados a cada requisição, uma requisição só ocorre quando o monitor acessa (ou recarrega) a página.

## Artefato

> Elemento 3

É o link de acesso para o artefato a ser inspecionado.

## Prazo Limite

> Elemento 4

É a data e horário definidos para o encerramento da etapa de detecção.

Mesmo que esse limite seja atingido, a etapa não se encerrará. Essa responsabilidade cabe ao monitor.

## Cancelar Inspeção

> Elemento 5

Este botão requer confirmação. Em caso positivo, encerra a inspeção, impedindo novas submissões e qualquer manipulação a ela.
<!-- Depois altere o nome (id) das inspeções canceladas para possibilitar o reuso -->

A inspeção _não_ será apagada e seu registro ainda constará entre as concluídas.

## Concluir Detecção

> Elemento 6

Ao clicar neste botão, o sistema encerra a etapa de detecção e interrompe novas submissões, muda a etapa da inspeção para a de coleção e redireciona o monitor para a tela de coleção. O tutorial de [Coleção](colecao_tutorial.md) orienta como proceder.

Para os inspetores esta inspeção estará agora na tela de concluídas (elemento 4e da [lista de inspeções](index.md#listagem-de-inspecoes))
