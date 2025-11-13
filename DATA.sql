-- 1. Create table
CREATE TABLE IF NOT EXISTS daily_playback (
    id SERIAL PRIMARY KEY,
    singer_name VARCHAR(100),
    playback_count INTEGER,
    playback_date DATE
);

-- 2. Insert dummy data for 7 days
INSERT INTO daily_playback (singer_name, playback_count, playback_date)
VALUES
('Singer A', 1200, '2025-11-07'),
('Singer A', 1500, '2025-11-08'),
('Singer A', 1300, '2025-11-09'),
('Singer A', 1600, '2025-11-10'),
('Singer A', 1400, '2025-11-11'),
('Singer A', 1700, '2025-11-12'),
('Singer A', 1800, '2025-11-13'),

('Singer B', 800, '2025-11-07'),
('Singer B', 900, '2025-11-08'),
('Singer B', 850, '2025-11-09'),
('Singer B', 950, '2025-11-10'),
('Singer B', 870, '2025-11-11'),
('Singer B', 920, '2025-11-12'),
('Singer B', 980, '2025-11-13');

-- 3. Verify data
SELECT * FROM daily_playback ORDER BY singer_name, playback_date;


