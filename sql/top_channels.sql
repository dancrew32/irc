WITH words AS (
    SELECT unnest(string_to_array(lower(words), ' ')) AS word
    FROM table
)
SELECT word, count(*) FROM words
GROUP BY word;
