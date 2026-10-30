-- Relatório de treinadores (junção de tabelas)
-- Para cada treinador: nome, idade e a região.
SELECT t.id_treinador,
       t.nome,
       t.idade,
       r.nome_regiao
FROM tb_treinador t
JOIN tb_regiao r ON r.id_regiao = t.id_regiao
ORDER BY t.id_treinador;