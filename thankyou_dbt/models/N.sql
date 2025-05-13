-- models/N.sql
SELECT 'N' AS letter
FROM {{ ref('A') }}
