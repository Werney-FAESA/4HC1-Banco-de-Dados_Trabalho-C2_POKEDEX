select count(1) as TOTAL_POKEMONS
	 , r.nome_regiao
	 from tb_pokemon p
	 	inner join tb_regiao r
	 		on p.id_regiao = r.id_regiao
	 group by r.nome_regiao;