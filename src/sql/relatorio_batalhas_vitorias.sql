SELECT t.id_treinador,
       t.nome AS treinador,
       r.nome_regiao AS regiao,
       COUNT(b.id_batalha) AS total_batalhas,
       COUNT(*) FILTER (WHERE b.id_vencedor = t.id_treinador) AS vitorias,
       COUNT(*) FILTER (WHERE b.id_vencedor <> t.id_treinador) AS derrotas,
       ROUND(100.0 * COUNT(*) FILTER (WHERE b.id_vencedor = t.id_treinador)
             / COUNT(b.id_batalha), 1) AS aproveitamento_pct,
       TO_CHAR(MAX(b.data_batalha), 'DD/MM/YYYY') AS ultima_batalha
  FROM tb_treinador t
 INNER JOIN tb_regiao r ON r.id_regiao = t.id_regiao
 INNER JOIN tb_batalha b ON t.id_treinador IN (b.id_treinador_1, b.id_treinador_2)
 GROUP BY t.id_treinador, t.nome, r.nome_regiao
 ORDER BY vitorias DESC, total_batalhas DESC, t.nome
