# Criando uma Inspeção

O primeiro passo para executar uma inspeção é o planejamento. Aqui é onde se definem os parâmetros da inspeção e organiza o "ambiente" de trabalho.

Para criar uma nova inspeção, acesse o menu _Criar > Inspeção_ (elemento 4b da [barra de navegação](index.md#navegacao)), que irá te direcionar para a página de criação de uma nova inspeção:

![Criar Inspeção](../assets/tutoriais/criar-inspecao.png"Tela de criação de inspeção")

> Ainda que os parâmetros aqui definidos se farão cumprir pelo sistema, a comunicação com a equipe é indispensável para garantir a efetividade do processo.

## Título

> Elemento 1

É o nome que será definido para a nova inspeção e serve tanto como identificador como parâmetro de busca, portanto deve ser único e específico.

## Inspetores

> Elemento 2

É a lista de todos os inspetores cadastrados no seu sistema. A partir dela você pode atribuir quantos quiser à inspeção, para isso basta selecioná-los.

Para selecionar múltiplos usuários individualmente você pode clicar em cada usuário desejado enquanto segura a tecla "ctrl".

<img src="/assets/tutoriais/ctrl-tutorial.gif" alt="Selecionar Grupo de Usuários" title="Como selecionar múltiplos usuários" width="60%">

---

Você pode também selecionar um grupo de usuários ao clicar no primeiro e segurar a tecla "shift" enquanto clica no segundo.

<img src="/assets/tutoriais/shift-tutorial.gif" alt="Selecionar Grupo de Usuários" title="Como selecionar grupos de usuários" width="60%">

## Artefato

> Elemento 3

É a lista com todos os tipos de inspeção cadastrados, . A partir dela você pode escolher qual será o tipo de artefato da inspeção atual. <!-- Implemente depois a visualização do artefato a partir dessa listagem -->

![Selecionar Artefato](../assets/tutoriais/inspecao-selecionar-artefato.png"Lista 'dropdown' para a seleção do artefato")

Só pode ser selecionado um tipo de artefato e este definirá a formatação de todo o processo de inspeção. O tutorial de [Artefatos](artefato_tutorial.md) traz mais detalhes.

## Link
<!-- Bixo tu é meio burro, nunca disponibilizou o link para o inspetor -->

> Elemento 4

É o endereço de acesso para o artefato a ser inspecionado. Caso ele não seja necessário por algum motivo, basta deixar este campo em branco.

Neste contexto, o artefato se refere diretamente ao objeto de inspeção e não do objeto abstrato que dita a formatação do processo (definido pelo elemento 3).

## Data Limite

> Elemento 5

Especifica a data limite para a etapa de detecção que será exibida para os inspetores. O sistema _não_ finalizará automaticamente a etapa de detecção, visto que ele não permite o retorno a etapas anteriores. Esta data serve para orientar os inspetores e o monitor deve encerrar manualmente a detecção quando assim julgar apropriado.

## Confirmar

> Elemento 6

Este botão realiza o registro da nova inspeção e redireciona para a página home, onde ela deve estar disponível na lista de monitor, com o status de detecção.

Em caso de formatação incorreta ou informação ausente o sistema notificará o usuário para que este corrija os dados antes da submissão.

---

# Monitorando uma Inspeção

Após criada a inspeção o fluxo de operações é linear, conforme definido formalmente para a inspeção de usabilidade (_detecção > coleção > discriminação_). Cada uma dessas etapas estão descritas no guia de uso, comece pela [Detecção](deteccao_tutorial.md)
