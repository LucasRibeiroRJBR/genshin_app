SELECT
	c.name,
	w_dps.name AS id_weapon_dps,
	w_dps_or.name AS id_weapon_dps_or,
	w_sup.name AS id_weapon_sup,
	w_sup_or.name AS id_weapon_sup_or,
	a_dps_1.name AS id_artifact_dps_1,
	a_dps_1_or.name AS id_artifact_dps_1_or,
	a_dps_2.name AS id_artifact_dps_2,
	a_dps_2_or.name AS id_artifact_dps_2_or,
	a_sup_1.name AS id_artifact_sup_1,
	a_sup_1_or.name AS id_artifact_sup_1_or,
	a_sup_2.name AS id_artifact_sup_2,
	a_sup_2_or.name AS id_artifact_sup_2_or,
	hypo.name AS id_hypos_mat,
	nature.name AS id_nature_mat,
	common.name AS id_common_mat
FROM
	chars as c
LEFT JOIN weapon AS w_dps ON c.id_weapon_dps = w_dps.id
LEFT JOIN weapon AS w_dps_or ON c.id_weapon_dps_or = w_dps_or.id
LEFT JOIN weapon AS w_sup ON c.id_weapon_sup = w_sup.id
LEFT JOIN weapon AS w_sup_or ON c.id_weapon_sup_or = w_sup_or.id
LEFT JOIN artifact AS a_dps_1 ON c.id_artifact_dps_1 = a_dps_1.id 
LEFT JOIN artifact AS a_dps_1_or ON c.id_artifact_dps_1_or = a_dps_1_or.id
LEFT JOIN artifact AS a_dps_2 ON c.id_artifact_dps_2 = a_dps_2.id 
LEFT JOIN artifact AS a_dps_2_or ON c.id_artifact_dps_2_or = a_dps_2_or.id
LEFT JOIN artifact AS a_sup_1 ON c.id_artifact_sup_1 = a_sup_1.id 
LEFT JOIN artifact AS a_sup_1_or ON c.id_artifact_sup_1_or = a_sup_1_or.id 
LEFT JOIN artifact AS a_sup_2 ON c.id_artifact_sup_2 = a_sup_2.id 
LEFT JOIN artifact AS a_sup_2_or ON c.id_artifact_sup_2_or = a_sup_2_or.id
LEFT JOIN hypos_mat AS hypo ON c.id_hypos_mat = hypo.id
LEFT JOIN nature_mat AS nature ON c.id_nature_mat = nature.id
LEFT JOIN common_mat AS common ON c.id_common_mat = common.id;