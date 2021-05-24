# Rock, Paper, Scissors

This project is from a tutorial where I created the code to that mimics the Rock, Paper, Scissor game. The user inputs thier item, the computer replies & the results of the winner is displayed.

Topic Displayed
- Control Flow
- Functions

```javascript
//1. Get the user's choice
//2. Get computer's choice
//3. Compare the two choices and determine a winner.
//4. State the program & display the results.
  

//this function takes users input, makes lowercase & creates valid game choice
const getUserChoice = userInput => {
  userInput = userInput.toLowerCase();
  if (userInput == 'rock' || userInput == 'paper' || userInput == 'scissors') {
    return userInput  
  } else {
    console.log('Error: Invalid Input')
  }
};

//creates random numbers & game choices based on the random numbers
const getComputerChoice = () => {
  const randomNumber = Math.floor(Math.random()* 3);
  switch (randomNumber) {
    case 0:
      return 'rock';
    case 1:
      return 'paper';
    case 2:
      return 'scissors';
  }
}

//determines winners based on different game choice combinations
const determineWinner = (userChoice, computerChoice) => {
  if (userChoice === computerChoice) {
    return 'The game is a tie!';
  }
  if (userChoice === 'rock') {
    if (computerChoice === 'paper') {
      return 'Sorry, computer wins.';
    } else {
      return 'Congrats, you won!'; 
    }
  }
  if (userChoice === 'paper') {
    if (computerChoice === 'scissors') {
      return 'Sorry, computer wins.';
    } else {
      return 'Congrats, you won!';
    }
  }
  if (userchoice === 'scissors') {
    if (computerChoice === 'rock') {
      return 'Sorry, computer wins.';
    } else {
      return 'Congrats you won!';
    }
  }
};

//this function plays the game 
const playGame = () => {
// user inputs choice below 
 const userChoice = getUserChoice('paper');
  const computerChoice = getComputerChoice();
  console.log('You threw: ' + userChoice);
  console.log('The computer threw: ' + computerChoice);
  console.log(determineWinner(userChoice, computerChoice));
};

playGame();
```
