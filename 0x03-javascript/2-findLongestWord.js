// Define a function that takes a sentence as a parameter
function findLongestWord(sentence) {
    let words = sentence.split(" ");
    let longestWord = "";
    let longestLength = 0;
  
    for (let word of words) {
      let wordLength = word.length;
      
      if (wordLength > longestLength) {
        longestWord = word;
        longestLength = wordLength;
      }
    }
    return longestWord;
  }
  const sentence = "The quick brown fox jumped over the lazy dog";
  const longest = findLongestWord(sentence);
  console.log("The longest word in the sentence is:", longest)
 
 