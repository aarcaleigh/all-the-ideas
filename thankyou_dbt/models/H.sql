-- models/H.sql
SELECT 'H' AS letter
FROM {{ ref('T') }}
