-- Relatório de linhagens evolutivas (junção de tabelas)
-- Para cada evolução: Pokémon base, Pokémon evoluído, como evolui e a região de origem.
SELECT e.id_evolucao,
       pb.id_pokemon                         AS id_base,
       pb.nome_pokemon                       AS pokemon_base,
       pe.id_pokemon                         AS id_evoluido,
       pe.nome_pokemon                       AS pokemon_evoluido,
       COALESCE(CAST(e.nivel_evolucao AS VARCHAR), '-') AS nivel,
       e.modo_evolucao                       AS modo,
       r.nome_regiao                         AS regiao
  FROM tb_evolucao e
 INNER JOIN tb_pokemon pb ON pb.id_pokemon = e.id_pokemon_base
 INNER JOIN tb_pokemon pe ON pe.id_pokemon = e.id_pokemon_evoluido
 INNER JOIN tb_regiao  r  ON r.id_regiao  = pb.id_regiao
 ORDER BY r.nome_regiao, pb.id_pokemon, pe.id_pokemon
