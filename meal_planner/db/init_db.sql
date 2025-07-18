-- Elimina DB se esiste
DROP DATABASE IF EXISTS meal_planner;

-- Crea DB nuovo
CREATE DATABASE meal_planner;

-- Seleziona DB
USE meal_planner;

-- Utenti (opzionale)
CREATE TABLE utenti (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
);

-- Piatti disponibili
CREATE TABLE piatti (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  descrizione TEXT,
  calorie INT
);

-- Ingredienti (base)
CREATE TABLE ingredienti (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  unita_misura VARCHAR(20)
);

-- Relazione piatti-ingredienti (molti-a-molti)
CREATE TABLE piatti_ingredienti (
  id INT AUTO_INCREMENT PRIMARY KEY,
  piatto_id INT,
  ingrediente_id INT,
  quantita DECIMAL(10,2),
  FOREIGN KEY (piatto_id) REFERENCES piatti(id) ON DELETE CASCADE,
  FOREIGN KEY (ingrediente_id) REFERENCES ingredienti(id) ON DELETE CASCADE
);

-- Planner settimanale di un utente
CREATE TABLE planner (
  id INT AUTO_INCREMENT PRIMARY KEY,
  utente_id INT,
  data DATE,
  piatto_id INT,
  FOREIGN KEY (utente_id) REFERENCES utenti(id) ON DELETE CASCADE,
  FOREIGN KEY (piatto_id) REFERENCES piatti(id) ON DELETE CASCADE
);

-- Dati di prova
INSERT INTO utenti (nome, email, password) VALUES
('Mario Rossi', 'mario@example.com', 'password_hash'),
('Anna Bianchi', 'anna@example.com', 'password_hash');

INSERT INTO piatti (nome, descrizione, calorie) VALUES
('Insalata di Pollo', 'Pollo con verdure fresche.', 350),
('Pasta al Pomodoro', 'Pasta integrale con salsa di pomodoro.', 500);

INSERT INTO ingredienti (nome, unita_misura) VALUES
('Pollo', 'grammi'),
('Pomodoro', 'grammi'),
('Pasta', 'grammi'),
('Insalata', 'grammi');

INSERT INTO piatti_ingredienti (piatto_id, ingrediente_id, quantita) VALUES
(1, 1, 150), -- Pollo
(1, 4, 50),  -- Insalata
(2, 2, 100), -- Pomodoro
(2, 3, 80);  -- Pasta

INSERT INTO planner (utente_id, data, piatto_id) VALUES
(1, '2025-07-18', 1),
(1, '2025-07-19', 2),
(2, '2025-07-18', 2);