-- Exemplo fictício: consolida lançamentos por empresa.
CREATE TABLE relatorios.resumo_por_empresa AS
SELECT e.nome AS empresa, SUM(l.valor) AS total
FROM financeiro.lancamentos l
JOIN cadastro.empresas e ON e.id = l.empresa_id
GROUP BY e.nome;
