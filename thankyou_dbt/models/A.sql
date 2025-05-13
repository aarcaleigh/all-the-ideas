-- models/A.sql
SELECT 'A' AS letter
FROM {{ ref('H') }}
