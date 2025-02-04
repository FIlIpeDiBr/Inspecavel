# Discriminação

A discriminação é a etapa final da inspeção. Você pode acessá-la através da lista de inspeções em aberto (elemento 4a da [lista de inspeção](index.md#listagem-de-inspecoes)), que possua o estágio de "Discriminação". Isso irá te redirecionar para a tela de discriminação:

![Tela de Discriminação](../assets/tutoriais/tela-discriminacao.png"Tela de discriminação")

## Título

> Elemento 1

É o título da inspeção, seguido de sua etapa atual, que neste caso é "Discriminação".

## Discrepâncias

> Elemento 2

Lista todas as discrepâncias principais agrupadas, com sua descrição e tipo de defeito (_descrição_ - _tipo_).

As reticências nesse caso são de exemplo, em um caso real aparecerá a descrição completa.

## Severidade

>Elemento 3

Nesta coluna, cada caixa de seleção (elemento 3a) permite escolher uma das severidades definidas pelo tipo de artefato para associar à discrepância correspondente.

## Cancelar Inspeção

> Elemento 4

Este botão requer confirmação. Em caso positivo, encerra a inspeção, impedindo novas submissões e qualquer manipulação a ela.
<!-- Depois altere o nome (id) das inspeções canceladas para possibilitar o reuso -->

A inspeção _não_ será apagada e seu registro ainda constará entre as concluídas.

## Salvar Alterações

> Elemento 5

Este botão registra as alterações realizadas até o momento, isto é, as severidades definidas para cada discrepância mas não encerra a inspeção ou realiza a troca de contexto.

Em caso de salvamento bem sucedido, uma notificação de confirmação é exibida. Você pode agora abandonar a tela de discriminação sem perdas.

## Concluir Inspeção

> Elemento 6

Este botão exige confirmação. Caso positivo, em adição a registrar as alterações já realizadas, este botão encerra a etapa de discriminação e, por consequência, a inspeção como um todo. A inspeção é então registrada como concluída e passa à lista de concluídas.

# Fim da Inspeção

O processo de inspeção está agora encerrado, mas o trabalho do monitor não acabou. Para obter o relatório da inspeção, basta clicar no botão com o carimbo de data/hora da conclusão na página de inspeções concluídas (elemento 4c da [lista de inspeção](index.md#listagem-de-inspecoes)) e será realizado o download do arquivo em pdf.

---

> Em atualizações futuras serão adicionadas as opções de exportar em formato csv e para issues do github, mas ainda não foram implementadas.