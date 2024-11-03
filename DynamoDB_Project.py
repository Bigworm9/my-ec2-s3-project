# DynamoDB Project

## Overview
This project demonstrates basic CRUD (Create, Read, Update, Delete) operations on an Amazon DynamoDB table using Python and the AWS `boto3` SDK. It’s designed for beginners to get hands-on experience with DynamoDB.

## Project Steps
- **Create a Key-Value Table**: Using DynamoDB in the AWS Console to create a `Music` table with `Artist` as the partition key and `SongTitle` as the sort key.
- **Add Data to the Table**: Insert multiple items representing songs by different artists.
- **Read the Table**: Retrieve specific items from the table using partition and sort keys.
- **Query the Table**: Perform query operations to find specific items based on `Artist`.
- **Delete an Item**: Delete a single item from the table.
- **Delete the Table**: Permanently delete the DynamoDB table.

## Prerequisites
- AWS account with access to DynamoDB.
- AWS CLI configured with valid credentials.
- Python 3 installed.
- `boto3` library installed (`pip install boto3`).

## Setup and Usage
1. Clone the repository.
2. Run `DynamoDB_Project.py` using `python DynamoDB_Project.py` to execute the script.

## Code Explanation
- **`create_table()`**: Creates a DynamoDB table named `Music`.
- **`add_data()`**: Adds items to the `Music` table.
- **`read_data()`**: Reads an item from the table based on the `Artist` and `SongTitle`.
- **`query_table()`**: Queries the table to fetch all songs by a specified artist.
- **`delete_item()`**: Deletes a specified item.
- **`delete_table()`**: Deletes the entire table.

## Screenshots
Add screenshots here if you have any, showing different steps in the AWS Console or terminal.

## Summary
In this project, we performed basic DynamoDB operations:
1. Created a Key-Value Table.
2. Added Data to the Table.
3. Read and Queried the Table.
4. Deleted an Item and the Table itself.

## License
Feel free to use this project as a learning reference.
