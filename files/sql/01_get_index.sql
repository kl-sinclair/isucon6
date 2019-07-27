ALTER TABLE star ADD INDEX star_keyword_idx(keyword);
ALTER TABLE entry ADD INDEX entry_update_idx(updated_at);
