ALTER TABLE entry ADD COLUMN keyword_length INT UNSIGNED AS (CHARACTER_LENGTH(keyword)) NOT NULL AFTER keyword;
ALTER TABLE entry ADD INDEX idx_entry_keyword_length(keyword_length);
