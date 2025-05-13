-- models/U.sql

WITH previous AS (
  SELECT * FROM {{ ref('O') }}
)

SELECT
  'Dear Brittany,' AS greeting,
  'Thank you so much for the opportunity to speak with you. I left the conversation energized and excited about what you are building at Beam Benefits.' AS message,
  'Best regards,' AS closing,
  'Astrid' AS signature,
  CURRENT_TIMESTAMP AS generated_at
