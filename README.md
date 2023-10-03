# Truth-table

## About
This program builds truth tables for logical expressions using reverse Polish notation.
***

## Functionality

The program is waiting for the input of a logical expression that meets the following requirements:
* variables are capital letters of the Latin alphabet
* 0 and 1 can be used in the expression
* available operations:
    * () for setting priority
    * not for logical negation
    * and for conjunction
    * or for disjunction
    * ~ for equivalence
    * -> for implication
    * ^ for addition modulo 2
* all operands, except parentheses, are written with spaces between

Example: A and B or (C -> D) or 1

The result of the program is a truth table displayed in the console, which presents all possible combinations of variable values and the function value for them.

The program does not provide validation of input data

***

## Architecture of the program

The program is separated into 6 functions: prior, oper, get_lexems_var, polish_notation, count_value, perform_truth_table

* *prior*<br>
Accepts a character as input and returns its priority. Used inside the *polish_notation* function.

* *oper*<br>
Accepts as input the operator and the values of the variables to which it is applied. Returns the result. Used inside the *count_value* function.

* *get_lexems_var*<br>
Reads the input string and splits it into lexems, and also extracts a list of variables. Returns a list of lexems and variables.

* *polish_notation*<br>
Accepts a list of tokens and a list of variables as input, and returns a list with an expression in reverse Polish notation.

* *count_value*<br>
Accepts as input a list of variables, a combination of variable values, and an expression in reverse Polish notation. Returns the value of the function.

* *perform_truth_table*<br>
An aggregating function that calls functions *get_lexems_var*, *polish_notation*, *count_value* to build a truth table.