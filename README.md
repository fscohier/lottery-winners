# lottery-winners
This is a simple Python script that will provide you the winning numbers for the next lottery (Eurojackpot - results may vary).

The concept is very simple. One formula that will return a sorted set of numbers (2 or 5 depending on the grid type) picked at random between 1 and a second value (max).
Since we need two sets of numbers (main grid from 1 to 50 and extra grid from 1 to 12), we run this formula to create the two necessary sets.
Then, a short formatting formula allows us to use these sets in a string.
Finally, we print the final numbers.

This is very basic at this point and next step will be to improve it with inputs (depending on different lottery requirements).
