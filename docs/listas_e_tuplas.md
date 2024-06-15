# Diferenças entre listas e tuplas

Em Python, listas e tuplas são dois tipos de estruturas de dados que permitem armazenar coleções de itens.
No entanto, existem algumas diferenças importantes entre elas:



### Lista é Mutável: 
O conteúdo de uma lista pode ser alterado após sua criação (itens podem ser adicionados, removidos ou modificados).
Sintaxe: Listas são definidas usando colchetes [].

#### Uso comum:
Listas são geralmente usadas quando você precisa de uma coleção de itens que pode mudar ao longo do tempo.

#### Exemplo Prático de Lista
Imagine que você está gerenciando uma lista de tarefas que pode ser atualizada ao longo do dia.

#### Criando uma lista de tarefas
tarefas = ["Comprar leite", "Enviar e-mails", "Estudar Python"]

#### Adicionando uma nova tarefa
tarefas.append("Fazer exercícios")

#### Removendo uma tarefa concluída
tarefas.remove("Enviar e-mails")

#### Modificando uma tarefa
tarefas[1] = "Estudar Django"

#### Exibindo a lista atualizada
print(tarefas)
Saída:
['Comprar leite', 'Estudar Django', 'Fazer exercícios']



### Tupla é Imutável: 
O conteúdo de uma tupla não pode ser alterado após sua criação. Isso significa que itens não podem ser adicionados, removidos ou modificados.
Sintaxe: Tuplas são definidas usando parênteses ().

#### Uso comum: 
Tuplas são geralmente usadas para armazenar coleções de itens que não devem mudar, como coordenadas (x, y) ou outras formas de dados constantes.

#### Exemplo Prático de Tupla
Imagine que você está lidando com coordenadas geográficas que não devem ser alteradas.

#### Criando uma tupla de coordenadas
coordenadas = (40.7128, -74.0060)

#### Tentando modificar uma coordenada (isso causará um erro)
coordenadas[0] = 41.0000  # TypeError: 'tuple' object does not support item assignment

#### Acessando os valores das coordenadas
latitude = coordenadas[0]
longitude = coordenadas[1]

#### Exibindo as coordenadas
print(f"Latitude: {latitude}, Longitude: {longitude}")

Saída:
Latitude: 40.7128, Longitude: -74.0060


# Resumo das Diferenças
- Mutabilidade: Listas são mutáveis, tuplas são imutáveis.
- Sintaxe: Listas usam colchetes [], tuplas usam parênteses ().
- Uso: Listas são usadas para coleções de itens que podem mudar, tuplas para coleções que não devem mudar.