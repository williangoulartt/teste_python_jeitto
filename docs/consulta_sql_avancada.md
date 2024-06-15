# Consulta SQL
Para encontrar o número total de pedidos feitos por cada cliente na tabela 'Pedidos' e incluir apenas os 
clientes que fizeram mais de 5 pedidos, podemos usar a seguinte consulta SQL:

```sh
sql
Copy code
SELECT ClienteID, COUNT(*) AS TotalPedidos
FROM Pedidos
GROUP BY ClienteID
HAVING COUNT(*) > 5;
```

## Explicando a consulta:

- SELECT ClienteID, COUNT(*) AS TotalPedidos: Seleciona o ID do cliente e conta o número de pedidos feitos por cada cliente. A contagem é renomeada como TotalPedidos para clareza.

- FROM Pedidos: Especifica a tabela 'Pedidos' de onde os dados serão extraídos.

- GROUP BY ClienteID: Agrupa os resultados pelo ID do cliente. Isso permite contar o número de pedidos para cada cliente individualmente.

- HAVING COUNT(*) > 5: Filtra os resultados para incluir apenas aqueles grupos (clientes) que têm mais de 5 pedidos. O HAVING é usado em vez de WHERE porque COUNT(*) é uma função de agregação e não pode ser usada diretamente em um WHERE.

Conforme solicitado no teste essa consulta retornará uma lista de ClienteID e o total de pedidos (TotalPedidos) para cada cliente que fez mais de 5 pedidos.