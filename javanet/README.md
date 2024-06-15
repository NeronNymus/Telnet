# Sudoku Solver

This Sudoku Solver, written in Java, aims to efficiently solve Sudoku puzzles.

## Project Structure

    .
    ├── bin
    │   ├── Classes
    │   │   ├── Box.class
    │   │   ├── BoxMatrix.class
    │   │   ├── Column.class
    │   │   ├── CustomCSVReader.class
    │   │   ├── Grid.class
    │   │   ├── Group.class
    │   │   └── Row.class
    │   └── Main
    │       └── Main.class
    ├── README.md
    ├── src
    │   ├── Classes
    │   │   ├── Box.java
    │   │   ├── BoxMatrix.java
    │   │   ├── Column.java
    │   │   ├── CustomCSVReader.java
    │   │   ├── Grid.java
    │   │   ├── Group.java
    │   │   └── Row.java
    │   └── Main
    │       └── Main.java
    ├── sudoku.sh
    └── templates
        ├── generator.sh
        └── samples
            ├── sample_1.csv
            ├── sample_1_solution.csv
            ├── sample_2.csv
            ├── sample_3.csv
            ├── sample_4.csv
            ├── sample_5.csv
            ├── sample_6.csv
            ├── sample_7.csv
            ├── sample_8.csv
            ├── sample_9.csv
            └── sample.csv

## Usage

- Clone the repository.
- If on a Linux system, execute `./sudoku.sh` to run the Sudoku Solver.
  
## Templates for Sudoku Resolver

The templates for the Sudoku Resolver consist of:
- CSV files.

- Each CSV file contains 81 lines representing a 9x9 matrix grid, with each line containing three integer values (x, y, z). 
Here, x and y are within the range [1,9], denoting rows and columns, respectively, while z falls within the range [0,9] representing 
the corresponding value in the grid. The value 0 indicates an undiscovered cell.

<a name=""></a>

## License

This project is licensed under the [MIT License](LICENSE).

