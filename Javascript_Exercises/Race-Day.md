# Race Day

This project is from a tutorial where I created the code to assign runners their run time based on their registered time & age.

Topic Displayed
- Control Flow


```javascript
//random number generator to assign runner number
let raceNumber = Math.floor(Math.random() * 1000);

//boolean to indicate if runner registered early or not
//early 9:30am   late 11:00am
let early = true;

//variable for runners age 
//adults > 18  youth < 18
let runnersAge = 25

//checks whether runner is an adult & registered early, if true a racenumber is assigned
if (early && runnersAge > 18) {
  raceNumber += 1000
}

//checks whether runner is an adult or youth, & registered time to determine provide run time & racenumber
if (early && runnersAge > 18) {
  console.log(`Your racenumber is ${raceNumber}. Your run time will be 9:30am.`)
} else if (!early && runnersAge >18) {
  console.log(`Your racenumber is ${raceNumber}. Your run time will be 11:00am.`)
} else if (runnersAge < 18) {
  console.log(`Your racenumber is ${raceNumber}. Your run time will be 12.30pm.`)
} else if (runnersAge == 18){
  console.log('Please visit the registration desk.')  
}
```
