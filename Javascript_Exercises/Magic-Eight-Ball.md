# Magic Eight Ball Project

This project is from a tutorial where I created the code that mimics the Magic Eight Ball game. A user asks a question & based on a random number (0 to 8), a generic response is provided.

Topic Displayed
- Control Flow


```javascript
//The user enters their name, if blank, no name will return
let userName = 'Shalonn'
userName ? console.log(`Hello, ${userName}`): console.log('Hello!');

//User question is asked
let userQuestion  = 'Hi Magic Eight Ball, Please tell me what will happen in my future?';
console.log(`${userQuestion}.`);

//random whole number generator between 0 & 8
let randomNumber = Math.floor(Math.random() * 8)

//create empty string variable to hold various reponses
let eightBall = '';

//contol flow to reply with random responses based on the random number generator
switch(randomNumber){
  case 0:
    eightball = 'It is certain';
    break;
  case 1:
    eightball = 'It is decidedly so';
    break;
  case 2:
    eightball = 'Reply hazy try again';
    break;
  case 3:
    eightball = 'Cannot predict now';
    break;
  case 4:
    eightball = 'Do not count on it';
    break;
  case 5:
    eightball = 'My sources say no';
    break;
  case 6:
    eightball = 'Outlook not so good';
    break;
  case 7:
    eightball = 'Signs point to yes';
    break;    
}

//prints the Magic Eight Balls reponse
console.log(eightball)
```
