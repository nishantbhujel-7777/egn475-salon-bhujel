
DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS users;

-- Users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'client'
);

-- Services table
CREATE TABLE services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    duration_minutes INTEGER NOT NULL,
    price_cents INTEGER NOT NULL,
    active INTEGER NOT NULL DEFAULT 1
);

-- Appointments table
CREATE TABLE appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    service_id INTEGER NOT NULL,
    client_name TEXT NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending',
    notes TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (service_id) REFERENCES services(id)
);

-- Insert sample salon services
INSERT INTO services
(name, duration_minutes, price_cents, active)
VALUES
('Haircut', 45, 2500, 1),
('Hair Coloring', 120, 8500, 1),
('Manicure', 40, 3000, 1),
('Pedicure', 50, 4000, 1),
('Facial Treatment', 60, 6500, 1),
('Hair Styling', 45, 3500, 1);

-- Insert sample appointments
INSERT INTO appointments
(user_id, service_id, client_name, date, time, status, notes)
VALUES
(NULL, 1, 'John Smith', '2026-11-25', '10:00', 'confirmed', 'Regular haircut'),
(NULL, 2, 'Sarah Johnson', '2026-11-26', '13:00', 'pending', 'Dark brown hair color'),
(NULL, 3, 'Emily Davis', '2026-11-27', '11:00', 'completed', 'Classic manicure');
