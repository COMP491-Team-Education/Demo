#                             Online Bash Shell.
#                 Code, Compile, Run and Debug Bash script online.
# Write your code in this editor and press "Run" button to execute it.


#!/bin/bash

# Update package list and install PostgreSQL
sudo apt update
sudo apt install -y postgresql postgresql-contrib

# Start PostgreSQL service
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Switch to postgres user and create database
sudo -u postgres psql -c "CREATE DATABASE books;"

# Create table in the books database
sudo -u postgres psql -d books -c "
CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL
);"

echo "PostgreSQL installed, 'books' database created with 'books' table."