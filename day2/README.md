# Python Practice – Part 1 & Part 2

This project contains a simple Python program designed to practice **strings, string methods, user input, arithmetic operators, and formatted output**.

## Part 1 – Sentence Operations

The program asks the user to enter a sentence and performs the following operations:

* Calculates the total length of the sentence.
* Converts the sentence to uppercase.
* Converts the sentence to lowercase.
* Reverses the sentence.
* Counts the number of words.
* Displays the first and last word.
* Checks whether the sentence is a palindrome, ignoring spaces and letter case.

### Example

```text
Enter a sentence: Madam

Total length: 5
Uppercase: MADAM | Lowercase: madam
Reversed sentence: madaM
Word count: 1
First word: Madam | Last Word: Madam
Is the sentence a palindrome? True
```

## Part 2 – Arithmetic Operations

The program asks the user to enter two integers and displays the results of several arithmetic operations in a formatted table.

The operations include:

| Operation      | Operator |
| -------------- | -------- |
| Addition       | `+`      |
| Subtraction    | `-`      |
| Multiplication | `*`      |
| Division       | `/`      |
| Floor Division | `//`     |
| Modulus        | `%`      |
| Power          | `**`     |

### Example

```text
Enter first number: 10
Enter second number: 3

Operation Output Result
--------------------
Addition         +     13.00
Subtraction      -      7.00
Multiplication   *     30.00
Division         /      3.33
Floor Division  //      3.00
Modulus          %      1.00
Power           **   1000.00
```

## Concepts Practiced

This exercise covers:

* `input()`
* `print()`
* `len()`
* `split()`
* String slicing
* `.upper()`
* `.lower()`
* String replacement with `.replace()`
* Arithmetic operators
* Floor division
* Modulus
* Exponentiation
* f-strings
* String formatting and alignment
* Basic conditional comparison

## How to Run

Make sure Python is installed on your system.

Run the program using:

```bash
python assignment1.py
```

Depending on your system, you may need:

```bash
python3 assignment1.py
```

## Note

The program expects valid numeric input for Part 2. Also, the division operations require the second number to be non-zero.
