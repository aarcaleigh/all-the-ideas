-- models/Y.sql
SELECT 'Y' AS letter
FROM {{ ref('K') }}
