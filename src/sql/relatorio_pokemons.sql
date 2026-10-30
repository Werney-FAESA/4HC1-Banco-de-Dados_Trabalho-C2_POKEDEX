select p.id_pokemon
	 , p.nome_pokemon
	 , p.tipo_primario
	 , r.nome_regiao
	 from tb_pokemon P
	 	inner join tb_regiao r
	 		on p.id_regiao = r.id_regiao;

