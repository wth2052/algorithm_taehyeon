SELECT `id`, `name`, `host_id` FROM `places` 
WHERE `host_id` IN (SELECT `host_id` FROM `places` GROUP BY `host_id` HAVING COUNT(*) > 1);


#자료 2개 = 헤비유저
