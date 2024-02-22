# NumberGuess-Python
A mini game in which the user and the computer separately try to guess the number.

##

When the User guesses:

It implements a game in which the user guesses a random number between 1 and 100. Here's how it works:

1. The "random" module is used to select a random number. Using the "randint()" function, a random number between 1 and 100 is selected and assigned to the "prediction" variable.

2. A cycle is started and the user is given 6 guesses. The cycle ends when the user exhausts these rights or finds the correct answer.

3. The user is prompted to enter a number at each step.

4. The number entered by the user is compared with the selected random number:
  - If the number entered by the user is larger than the randomly selected number, the user is instructed to enter a smaller number.
  - If the number entered by the user is less than the randomly selected number, the user is instructed to enter a larger number.
  - If the number entered by the user is equal to the randomly selected number, the user has guessed correctly and is congratulated.

5. When the user makes wrong guesses, the remaining guesses are shown. If the user uses all guessing rights, the correct answer is shown.

This code implements a simple console-based number guessing game and provides feedback for the user to guess a randomly selected number.

##

When the Computer guesses:

It implements a game in which the user guesses a number in a certain range (1 to 100). However, this code is more optimized than the previous example because a binary search method is used instead of a random guess at each step. Here's how it works:

1. The "random" module is used to select a random number. However, in this code, random numbers are not generated, but a prediction is made at each step using the binary search method.

2. The user is told which button to use to guess correctly:
  - If the answer is correct, he is asked to press 0,
  - If it is a smaller number, he is asked to press 1,
  - If it is a larger number, he is asked to press 2.

3. A prediction is made at each step using the binary search method. The forecast is set as the midpoint in the current range.

4. Depending on the answer given by the user, the range of the predicted number is narrowed:
  - If the user's answer is smaller than the predicted number, the search range is updated and a new prediction is made in a smaller range.
  - If the user's answer is larger than the predicted number, the search range is updated and a new prediction is made in a larger range.
  - If the user's answer is correct, it is stated that he won the game.

5. When the user makes wrong guesses, the remaining guesses are shown. If the user uses all his guessing rights, he is asked to try again.

This code tries to find the correct answer in fewer steps using the binary search method and helps the user reach the result faster.
