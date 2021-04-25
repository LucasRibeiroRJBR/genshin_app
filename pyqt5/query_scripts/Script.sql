
-- Retornar mais de 1 item da mesma tabela em outro campo (ARMA)
 SELECT
	c.name,
	w_dps.name AS id_weapon_dps,
	w_dps_or.name AS id_weapon_dps_or,
	w_sup.name AS id_weapon_sup,
	w_sup_or.name AS id_weapon_sup_or
FROM
	chars as c
LEFT JOIN weapon AS w_dps ON
	c.id_weapon_dps = w_dps.id
LEFT JOIN weapon AS w_dps_or ON
	c.id_weapon_dps_or = w_dps_or.id
LEFT JOIN weapon AS w_sup ON
	c.id_weapon_sup = w_sup.id
LEFT JOIN weapon AS w_sup_or ON
	c.id_weapon_sup_or = w_sup_or.id;
