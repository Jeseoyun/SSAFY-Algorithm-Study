-- 코드를 입력하세요
# 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 
# 이때 결과는 보호 시작일 순으로 조회해야 합니다.
SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS AS I
LEFT JOIN ANIMAL_OUTS AS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.ANIMAL_ID IS NULL
ORDER BY I.DATETIME ASC
LIMIT 3