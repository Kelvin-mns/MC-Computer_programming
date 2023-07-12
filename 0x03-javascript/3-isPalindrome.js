//function that reads a word forward and sounds the same asr backward
function isPalindrome(str) {
    str = str.toLowerCase().replace(/[^a-z0-9]/g, "");
    
    return str === str.split("").reverse().join("");
  }
  console.log(isPalindrome("racecar"));  
  console.log(isPalindrome("Hello"));