select r.id_regiao
	 , r.nome_regiao
	 , count(1) as "Pokémons vinculados"
	 from tb_regiao r
	 	inner join tb_pokemon p
	 		on r.id_regiao = p.id_regiao
	 group by r.id_regiao, r.nome_regiao
	 order by r.id_regiao;

     