##Bike Shop Database (WareHouse) optimization Project 

#Description:
Bike Shop is planning to optimize their warehouse operations to improve efficiency and customer satisfaction. Goal of this project is to help employees perform their daily work more efficiently, that they can analyze sales data, check orders, calculate warehouse stock, restock and etc.

#Bike Stock [$filter]:
1. Retrieve bikes who are for sale from the existing database that are currently active.
2. Filter bikes in database with a quantity greater than zero.
3. Collect the essential information for each inventory item, including its ID, name, and quantity.

#Sales Data [$sort]:
1. Extract sales data from the database, including customer details, product information, and sales.
2. Sort the sales data based on specific criteria, such as bike type or sales date.

#Monthly Sales Revenue[$project]:
1. Retrieve the sales data from the database, transaction date and revenue generated.
2. Group the sales data by month and calculate the total revenue for each month.

#Warehouse Stock balance[$project]:
1. Check all available bike stock in warehouse.
2. Sort available bikes in warehouse by quantity.
3. Return bikes ID, manufacturer and quantity.