Title: aws-rds-query-executor

Description: This repository contains a Python script that connects to an AWS RDS database and executes queries. It provides a convenient way to interact with the database and retrieve results. The script prompts the user for the necessary information such as host, username, password, and database name to establish the connection. It then executes a sample query to fetch all rows from the 'users' table and prints the results.

With the AWS RDS Query Executor repository, you can easily connect to your AWS RDS database and perform queries without the need for manual configuration or complex setup.

Step 1: Create an RDS instance
--> Sign in to the AWS Management Console and open the RDS service.
--> Click on "Create database" to start the instance creation wizard.
--> Choose "MySQL" as the database engine.
--> Select the version and edition of MySQL you want to use.
--> Configure the instance details, such as DB instance identifier, username, password, and storage options.
--> Choose the appropriate VPC, subnet group, and security group settings.
--> Review the configuration and click "Create database" to start the instance creation process.

Step 2: Wait for the instance to be available
--> The RDS instance creation process may take a few minutes. Wait until the instance status is "available" before proceeding.

Step 3: Get the connection details
--> Once the instance is available, go to the RDS dashboard, select your instance, and navigate to the "Connectivity & security" tab.
--> Note down the endpoint (hostname), port, username, and password. These details will be needed to connect to the database.

Step 4: Test RDS Connection using MySQL Workbench
--> Download and install MySQL Workbench on your local machine.
--> Launch MySQL Workbench and click on "New Connection" to set up a new connection.
--> Enter a connection name, the RDS instance endpoint (hostname), port, username, and password.
--> Click "Test Connection" to verify if the connection to the RDS instance is successful.
--> If the connection test is successful, proceed to the next step. If not, double-check the connection details and ensure that the RDS instance is accessible.

Step 5: Add a database, tables and few rows
--> Here's an example query to create a database named "mydatabase": CREATE DATABASE mydatabase;
--> select the database where you want to create the tables using the USE statement. For example: USE your_database_name;
--> Here's an example to create a simple "users" table:

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100),
    age INT
);

--> You can use the INSERT INTO statement to insert some rows. Here's an example:

INSERT INTO users (name, email, age) VALUES
    ('John Doe', 'johndoe@example.com', 25),
    ('Jane Smith', 'janesmith@example.com', 30),
    ('Bob Johnson', 'bobjohnson@example.com', 35);


Step 6: Update the Python script
Modify the Python script you previously used to connect to the MySQL database.
Update the host, user, password, and database values in the script with the connection details of your RDS instance.

Step 7: Connect to the RDS instance
Run the updated Python script to connect to the RDS instance and execute the query.

If the connection is successful, you should be able to retrieve the rows from the database.
By following these steps, you'll be able to create an RDS instance on AWS, wait for it to become available, get the connection details, update your Python script, test the RDS connection using MySQL Workbench, and finally connect to the RDS instance using your Python script. Remember to configure appropriate security group rules to allow access to the RDS instance from your local machine or the desired network.
