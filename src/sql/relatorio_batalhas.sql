SELECT b.id_batalha,
       TO_CHAR(b.data_batalha, 'DD/MM/YYYY') AS data_batalha,
       b.local_batalha,
       t1.nome AS treinador_1,
       t2.nome AS treinador_2,
       v.nome AS vencedor,
       rv.nome_regiao AS regiao_vencedor
  FROM tb_batalha b
 INNER JOIN tb_treinador t1 ON t1.id_treinador = b.id_treinador_1
 INNER JOIN tb_treinador t2 ON t2.id_treinador = b.id_treinador_2
 INNER JOIN tb_treinador v ON v.id_treinador = b.id_vencedor
 INNER JOIN tb_regiao rv ON rv.id_regiao = v.id_regiao
 ORDER BY b.data_batalha DESC, b.id_batalha
