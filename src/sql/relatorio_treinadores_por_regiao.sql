SELECT r.nome_regiao,
       COUNT(t.id_treinador) AS quantidade_treinadores,
       ROUND(AVG(t.idade), 2) AS idade_media,
       MAX(t.idade) AS maior_idade
FROM tb_regiao r
LEFT JOIN tb_treinador t ON t.id_regiao = r.id_regiao
GROUP BY r.id_regiao, r.nome_regiao
ORDER BY r.nome_regiao;
