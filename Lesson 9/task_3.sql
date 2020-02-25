CREATE TABLE IF NOT EXISTS linked_staff (
id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
leader_id INT UNSIGNED NOT NULL,
staff_id INT UNSIGNED NOT NULL
);

INSERT INTO linked_staff (id, leader_id, staff_id) VALUES (null, 1, 2);
INSERT INTO linked_staff (id, leader_id, staff_id) VALUES (null, 1, 3);
INSERT INTO linked_staff (id, leader_id, staff_id) VALUES (null, 1, 4);
INSERT INTO linked_staff (id, leader_id, staff_id) VALUES (null, 1, 5);
INSERT INTO linked_staff (id, leader_id, staff_id) VALUES (null, 2, 3);
INSERT INTO linked_staff (id, leader_id, staff_id) VALUES (null, 2, 4);
INSERT INTO linked_staff (id, leader_id, staff_id) VALUES (null, 2, 5);
INSERT INTO linked_staff (id, leader_id, staff_id) VALUES (null, 3, 5);
INSERT INTO linked_staff (id, leader_id, staff_id) VALUES (null, 4, 5);

SELECT staff.first_name, staff.last_name, staff.post, staff.salary FROM staff
INNER JOIN linked_staff ON staff.id=linked_staff.staff_id
WHERE linked_staff.leader_id = (SELECT id FROM staff WHERE last_name = 'Banderas');