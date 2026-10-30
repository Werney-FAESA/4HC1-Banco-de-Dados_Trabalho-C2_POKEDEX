select count(1) as "Total de Pokémons"
	 , p.tipo_primario
	 from tb_pokemon p
	 group by p.tipo_primario;

