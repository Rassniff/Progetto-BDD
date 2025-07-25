DROP VIEW IF EXISTS planner_nutritional_view;

CREATE VIEW planner_nutritional_view AS
SELECT
  planner.utente_id,
  planner.data,
  planner.pasto,
  planner.piatto_id,
  ingredienti.id AS ingrediente_id,
  (ingredienti.proteine * piatti_ingredienti.quantita / 100) AS proteine,
  (ingredienti.carboidrati * piatti_ingredienti.quantita / 100) AS carboidrati,
  (ingredienti.calorie * piatti_ingredienti.quantita / 100) AS calorie
FROM planner
JOIN piatti ON planner.piatto_id = piatti.id
JOIN piatti_ingredienti ON piatti.id = piatti_ingredienti.piatto_id
JOIN ingredienti ON piatti_ingredienti.ingrediente_id = ingredienti.id;

