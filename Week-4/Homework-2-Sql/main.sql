q1:
SELECT * FROM customer WHERE store_id = 2


q2:
INSERT INTO customer (customer_id, store_id, first_name, last_name, email, address_id, active, create_date, last_update)
VALUES
(602, 1, 'Guy', 'Incognito', 'Who.Is@Homer.mynameis', 1, 1, time(), time()),
(603, 1, 'Joey Jo Junior', 'Shabadoo', 'worstName@IEver.heard', 1, 1, time(), time()),
(604, 1, 'Hugh', 'Jass', 'what@aNiceYoung.man', 1, 1, time(), time());

q3:
UPDATE customer SET store_id = 2 WHERE store_id = 1 LIMIT 5

q4:
SELECT customer_id, customer.first_name, customer.last_name, customer.email
FROM customer JOIN store ON customer.store_id = store.store_id
JOIN staff ON store.store_id = staff.staff_id
WHERE staff.first_name = "Mike"

q5:
INSERT INTO store (store_id, manager_staff_id, address_id, last_update)
VALUES (3, (SELECT staff_id FROM staff WHERE staff.first_name = "Jon"), 1, time())




q6:
-- (SELECT customer_id from customer ORDER BY customer_id DESC LIMIT 1)
INSERT INTO customer (customer_id, store_id, first_name, last_name, email, address_id, active, create_date, last_update)
VALUES
(606, 3, "Rand", "Mcnally", "sdj@sfdsf.sdf", 1, 1, time(), time()),
(607, 3, "Rand", "Mcnally", "sdj@sfdsf.sdf", 1, 1, time(), time()),
(608, 3, "Rand", "Mcnally", "sdj@sfdsf.sdf", 1, 1, time(), time())

q7:
SELECT staff.first_name AS store_manager, customer.* FROM customer JOIN staff WHERE customer.store_id = 3