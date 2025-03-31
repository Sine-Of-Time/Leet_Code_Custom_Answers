function BracketMatcher(str) {
  const stack = [];
  
  for (let i = 0; i < str.length; i++) {
    if (str[i] === '(') { //Best to use === in js
      stack.push('(');
    } else if (str[i] === ')') {
      if (stack.length === 0) {
        // No matching opening bracket on the stack.
        return 0;
      }
      stack.pop();
    }
  }
  
  // If the stack is empty, all brackets have been matched.
  return stack.length === 0 ? 1 : 0;
}
   
// keep this function call here 
console.log(BracketMatcher(readline()));

//Have the function BracketMatcher(str) take the str parameter being passed and return 1
//if the brackets are correctly matched and each one is accounted for. Otherwise return 0. For example: if str is "(hello (world))",
//then the output should be 1, but if str is "((hello (world))" the the output should be 0 because the brackets do not correctly match up.
//Only "(" and ")" will be used as brackets. If str contains no brackets return 1.
