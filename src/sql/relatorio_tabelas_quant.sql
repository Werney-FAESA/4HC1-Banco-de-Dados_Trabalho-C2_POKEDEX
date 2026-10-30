select  'TB_REGIAO' as entidade, count(*) as "Total de registros" from tb_regiao
union all 
select  'TB_POKEMON' as entidade, COUNT(*) as total_registros from tb_pokemon
union all
select 'TB_EVOLUCAO' as entidade, COUNT(*) as total_registros from tb_evolucao
union all
select 'TB_TREINADOR' as entidade, COUNT(*) as total_registros from tb_treinador
union all
select 'TB_BATALHA' as entidade, COUNT(*) as total_registros from tb_batalha;

