-- 코드를 입력하세요
SELECT `dr_name`, `dr_id`, `mcdp_cd`, DATE_FORMAT(`hire_ymd`, "%Y-%m-%d")
FROM `doctor` 
WHERE (`mcdp_cd` = 'cs') or (`mcdp_cd` = 'gs') order by hire_ymd desc , dr_name asc