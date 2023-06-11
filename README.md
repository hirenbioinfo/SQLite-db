# Microbiology Lab Database Project

Author: Hiren Ghosh  
Affiliation: UKF, Freiburg

This project involves creating and interacting with an SQLite database for a microbiology lab. The goal is to store and manage data related to sequencing samples using a graphical user interface (GUI) built with Tkinter.

## Project Steps

1. **Database Creation:** Initially, an SQLite database file named `microbiology_lab.db` is created using the `sqlite3` library. The database is designed to store information about sequencing samples, including sample ID, source, project details, sequencing platform, reads, QC status, species, and ST types.

2. **GUI Development:** Using the Tkinter library, a GUI is built to provide a user-friendly interface for entering and modifying data in the database. Entry fields and buttons are created to collect information from the user and perform the required database operations.

3. **Insertion of Data:** The GUI allows users to enter details for sequencing samples. When the user clicks the "Submit" button, the data is inserted into the "Sequencing" table of the database.

4. **Data Retrieval:** To verify the successful insertion of data, a SELECT statement is executed to retrieve the inserted records from the "Sequencing" table. The retrieved data is then printed to the console.

5. **Modification of Data:** The GUI includes an option to modify or edit existing entries in the "Sequencing" table. Users can select a specific entry and update its fields, triggering an UPDATE statement to modify the corresponding record in the database.

## Dependencies

- Python 3.x
- sqlite3 library
- Tkinter library

## Instructions

1. Run the code to create the SQLite database and start the GUI.
2. Enter the details for each sequencing sample in the provided entry fields.
3. Click the "Submit" button to insert the data into the database.
4. Use the "Edit" buttons to modify specific entries if needed.
5. Run the SELECT statement to retrieve and print the inserted data.

