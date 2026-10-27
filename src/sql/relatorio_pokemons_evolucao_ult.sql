-- Relatório de Pokémons na última evolução (junção de tabelas)
-- Pokémons que aparecem como resultado de uma evolução, mas não evoluem para nenhum outro.
SELECT pe.id_pokemon,
       pe.nome_pokemon                       AS pokemon_final,
       pe.tipo_primario,
       COALESCE(pe.tipo_secundario, '-')     AS tipo_secundario,
       pb.nome_pokemon                       AS evolui_de,
       e.modo_evolucao                       AS modo,
       r.nome_regiao                         AS regiao
  FROM tb_evolucao e
 INNER JOIN tb_pokemon pe ON pe.id_pokemon = e.id_pokemon_evoluido
 INNER JOIN tb_pokemon pb ON pb.id_pokemon = e.id_pokemon_base
 INNER JOIN tb_regiao  r  ON r.id_regiao  = pe.id_regiao
 WHERE NOT EXISTS (SELECT 1
                     FROM tb_evolucao prox
                    WHERE prox.id_pokemon_base = pe.id_pokemon)
 ORDER BY pe.id_pokemon
