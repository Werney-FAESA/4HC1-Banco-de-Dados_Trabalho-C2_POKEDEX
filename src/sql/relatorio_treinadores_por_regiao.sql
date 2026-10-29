SELECT r.nome_regiao,
       COUNT(t.id_treinador) AS quantidade_treinadores,
       ROUND(AVG(t.idade), 2) AS idade_media,
       MAX(t.idade) AS maior_idade
FROM tb_regiao r
LEFT JOIN tb_treinador t ON t.id_regiao = r.id_regiao
GROUP BY r.id_regiao, r.nome_regiao
ORDER BY r.nome_regiao;

SELECT b.id_batalha,
       t1.nome AS treinador_1,
       t2.nome AS treinador_2,
       vencedor.nome AS vencedor,
       b.local_batalha,
       b.data_batalha
FROM tb_batalha b
JOIN tb_treinador t1 ON t1.id_treinador = b.id_treinador_1
JOIN tb_treinador t2 ON t2.id_treinador = b.id_treinador_2
JOIN tb_treinador vencedor ON vencedor.id_treinador = b.id_vencedor;