-- Create new Table

CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
    UNIQUE KEY unique_id_idx (id)
);
