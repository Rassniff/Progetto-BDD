-- Elimina DB se esiste
DROP DATABASE IF EXISTS meal_planner;

-- Crea DB nuovo
CREATE DATABASE meal_planner;

-- Seleziona DB
USE meal_planner;

-- Utenti (opzionale)
CREATE TABLE utenti (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
);

-- Piatti disponibili : pubblici o privati
CREATE TABLE piatti (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  descrizione TEXT,
  validato BOOLEAN DEFAULT 1, -- 0 = privato, 1 = pubblico
  utente_id INT, -- NULL se pubblico creato da admin
  FOREIGN KEY (utente_id) REFERENCES utenti(id) ON DELETE CASCADE
);

-- Ingredienti (base) : globali
CREATE TABLE ingredienti (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  unita_misura VARCHAR(20),
  proteine DECIMAL(6,2) DEFAULT 0,   -- quantità in grammi per unità di misura
  carboidrati DECIMAL(6,2) DEFAULT 0,
  calorie DECIMAL(6,2) DEFAULT 0,
  validato BOOLEAN DEFAULT 1, -- 0 = privato, 1 = pubblico
  utente_id INT, -- NULL se pubblico creato da admin
  FOREIGN KEY (utente_id) REFERENCES utenti(id) ON DELETE CASCADE
);

-- Relazione piatti-ingredienti (molti-a-molti)
CREATE TABLE piatti_ingredienti (
  id INT AUTO_INCREMENT PRIMARY KEY,
  piatto_id INT,
  ingrediente_id INT,
  quantita DECIMAL(10,2), -- quantità dell'ingrediente nel piatto
  FOREIGN KEY (piatto_id) REFERENCES piatti(id) ON DELETE CASCADE,
  FOREIGN KEY (ingrediente_id) REFERENCES ingredienti(id) ON DELETE CASCADE
);

-- Planner settimanale di un utente
CREATE TABLE planner (
  id INT AUTO_INCREMENT PRIMARY KEY,
  utente_id INT,
  data DATE,
  pasto ENUM('colazione', 'pranzo', 'merenda', 'cena') NOT NULL,
  piatto_id INT,
  FOREIGN KEY (utente_id) REFERENCES utenti(id) ON DELETE CASCADE,
  FOREIGN KEY (piatto_id) REFERENCES piatti(id) ON DELETE CASCADE
);

-- Dati di prova

INSERT INTO ingredienti (nome, unita_misura, proteine, carboidrati, calorie) VALUES
  ('Tonno', 'grammi', 25.00, 0.00, 116.00),
  ('Insalata', 'grammi', 1.00, 2.00, 15.00),
  ('Olio di oliva', 'grammi', 0.00, 0.00, 900.00),
  ('Pasta', 'grammi', 10.00, 60.00, 350.00),
  ('Pesto', 'grammi', 3.00, 3.00, 1000.00),
  ('Parmigiano', 'grammi', 35.00, 0.00, 400.00),
  ('Uova', 'grammi', 11.00, 1.00, 155.00),
  ('Patate', 'grammi', 2.00, 20.00, 73.00),
  ('Pane integrale', 'grammi', 10.00, 50.00, 280.00),
  ('Prosciutto cotto', 'grammi', 20.00, 2.00, 200.00),
  ('Formaggio a fette', 'grammi', 20.00, 3.00, 350.00),
  ('Yogurt bianco', 'grammi', 3.50, 4.00, 60.00),
  ('Banana', 'grammi', 1.00, 23.00, 89.00),
  ('Fiocchi di avena', 'grammi', 13.00, 60.00, 380.00);

INSERT INTO piatti (nome, descrizione) VALUES
  ('Insalata di Tonno', 'Tonno con insalata e un filo d’olio d’oliva.'),
  ('Pasta al Pesto', 'Pasta condita con pesto e una spolverata di parmigiano.'),
  ('Uova e Patate', 'Uova strapazzate con contorno di patate e olio d’oliva.'),
  ('Toast con Prosciutto e Formaggio', 'Pane integrale tostato con prosciutto cotto e formaggio fuso.'),
  ('Yogurt e Frutta', 'Yogurt con banana a fette e fiocchi d’avena.');


INSERT INTO piatti_ingredienti (piatto_id, ingrediente_id, quantita) VALUES
  (1, 1, 100.00),  -- Tonno
  (1, 2, 50.00),   -- Insalata
  (1, 3, 10.00);   -- Olio d’oliva


INSERT INTO piatti_ingredienti (piatto_id, ingrediente_id, quantita) VALUES
  (2, 4, 80.00),   -- Pasta
  (2, 5, 30.00),   -- Pesto
  (2, 6, 10.00);   -- Parmigiano


INSERT INTO piatti_ingredienti (piatto_id, ingrediente_id, quantita) VALUES
  (3, 7, 120.00),  -- Uova
  (3, 8, 150.00),  -- Patate
  (3, 3, 10.00);   -- Olio d’oliva


INSERT INTO piatti_ingredienti (piatto_id, ingrediente_id, quantita) VALUES
  (4, 9, 60.00),   -- Pane integrale
  (4, 10, 50.00),  -- Prosciutto cotto
  (4, 11, 30.00);  -- Formaggio a fette


INSERT INTO piatti_ingredienti (piatto_id, ingrediente_id, quantita) VALUES
  (5, 12, 150.00), -- Yogurt bianco
  (5, 13, 100.00), -- Banana
  (5, 14, 30.00);  -- Fiocchi d’avena