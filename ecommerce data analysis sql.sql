-- Q1 What is the total revenue generated each month?
SELECT MONTH(payment_date) as Month, SUM(amount) as Total_Amount FROM payments
GROUP BY Month ORDER BY Month;

-- Q2 Which product categories generated the most revenue?
SELECT category, SUM(oi.quantity*oi.price) as Total_Revenue  FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id 
JOIN products p ON  oi.product_id = p.product_id
GROUP BY category ; 

-- Q3 What is the distribution of revenue by payment methods?
SELECT method as Payment_Method,
 SUM(amount) AS Total_Revenue 
 FROM payments
GROUP BY method 
ORDER BY Total_Revenue desc; 

-- Q4 What is the status breakdown of orders?
SELECT status, COUNT(*) as Order_Status_Count 
FROM orders 
GROUP BY status 
ORDER BY Order_Status_Count desc;

-- Q5 Which Region have highest Number of customers?
SELECT region, COUNT(*) as No_of_Customer FROM customers
GROUP BY region ORDER BY No_of_Customer DESC;  

-- Q6 Which region have highest revenue?
SELECT region, SUM(quantity*price) as Total_revenue FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY region;

-- Q7 Number of customers joined each month ?
SELECT YEAR(join_date) as Year,
MONTH(join_date) as Month,
Count(*) as No_of_Customer
FROM Customers
GROUP BY Year, Month
ORDER BY Year, Month;

-- Q8 What is the average revenue generated per customer in each region?
SELECT c.region, COUNT(DISTINCT c.customer_id) as total_customers,
SUM(oi.quantity*oi.price) as total_revenue, 
ROUND(SUM(oi.quantity*oi.price)/COUNT(DISTINCT c.customer_id),2) as AVG_revenue
FROM customers c
JOIN orders o ON c.customer_id=o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY c.region
order by AVG_revenue DESC;

-- Q9 Revenue by Mononth
SELECT DATE_FORMAT(o.order_date, '%Y-%m') AS month, 
SUM(oi.price * oi.quantity) AS total_revenue
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY month
ORDER BY month;

-- Q10 revenue by category
SELECT p.category, SUM(oi.price * oi.quantity) AS total_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;

-- Q11 repeated customer by region
SELECT c.region,
COUNT(DISTINCT o.customer_id) AS repeat_customers
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.region
HAVING COUNT(o.order_id) > 1;

-- Q12 Top 10 product by revenue
SELECT name, SUM(price*stock) AS revenue
FROM products
GROUP BY name
ORDER BY revenue DESC
LIMIT 10 ;