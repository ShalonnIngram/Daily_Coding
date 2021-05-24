# Sleep Debt Calculator

This project is from a tutorial where I created the code to calculate Sleep Debt based on the users inputted daily sleep hours versus thier ideal sleep hours. The hours are calculated by day & totaled for the week. After the actuals are compared to the ideal, the amount of potential debt/surplus sleep is displayed.

Topic Covered
- Control Flow
- Functions

```javascript
//function to allow user to input number of daily sleep time per week
const getSleepHours = day => {
  switch(day) {
    case 'monday':
      return 8
      break;
    case 'tuesday':
      return 7
      break;
    case 'wednesday':
      return 6;
      break;
    case 'thursday':
      return 7
      break;   
    case 'friday':
      return 6
      break;
    case 'saturday':
      return 5
      break;
    case 'sunday':
      return 7
      break;
    default:
      return 'Error'
  }    
};

//function to sum hours of inputted sleep from getSleepHours
getActualSleepHours = () => 
  getSleepHours('monday') +
  getSleepHours('tuesday') +
  getSleepHours('wednesday') +
  getSleepHours('thursday') +
  getSleepHours('friday') +
  getSleepHours('saturday') +
  getSleepHours('sunday');   

//function to calculate total ideal hours the user would like to sleep per week
getIdealSleepHours = () => {
  const idealHours = 8;
  return idealHours * 7;
};

//function to calculate the comparison of the users actual sleep hours to their ideal sleep hours & provides the amount of hours needed +/- to reach their goal
calculateSleepDebt = () => {
  const actualSleepHours = getActualSleepHours();
  const idealSleepHours = getIdealSleepHours();
  if (actualSleepHours === idealSleepHours) {
    console.log('Goal sleep reached!');
  } else if (actualSleepHours > idealSleepHours) {
    console.log('You slept ' + (actualSleepHours - idealSleepHours) + ' ' + 'hours more than your goal!');
  } else if (actualSleepHours < idealSleepHours) {
    console.log('You should get some rest, you slept' + ' ' + (idealSleepHours - actualSleepHours) + ' ' + 'hours less than your goal.');
  } else{
    console.log('Error: Please check your code.')
  }
};

//function to display results of sleep hours
calculateSleepDebt()
```
