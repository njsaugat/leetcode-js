var isValidAnagram = (str, word) => {
  if (str.length !== word.length) return false;
  const visited = new Array(word.length).fill(false);

  for (let i = 0; i < str.length; i++) {
    for (let j = 0; j < word.length; j++) {
      if (str[i] === word[j] && !visited[j]) {
        visited[j] = true;
        ;
      }
    }
  }
  for (let i = 0; i < visited.length; i++) {
    if (!visited[i]) return false;
  }
  return true;
};

var isValidAnagramSorted = (str, word) => {
  if (str.length !== word.length) return false;

  const strArr = Array.from(str).sort();
  const wordArr = Array.from(word).sort();
  for (let i = 0; i < strArr.length; i++) {
    if (strArr[i] !== wordArr[i]) return false;
  }
  return true;
};

const getHash = (str) => {
  const strHash = new Map();
  for (let i = 0; i < str.length; i++) {
    if (strHash.has(str[i])) {
      let repValue = strHash.get(str[i]);
      strHash.set(str[i], ++repValue);
    } else {
      strHash.set(str[i], 1);
    }
  }
  return strHash;
};
var isValidAnagramHash = (str, word) => {
  if (str.length !== word.length) return false;
  const strHash = getHash(str);
  const wordHash = getHash(word);
  if (strHash.size !== wordHash.size) return false;
  for (let i = 0; i < str.length; i++) {
    if (strHash.get(str[i]) !== wordHash.get(str[i])) {
      return false;
    }
  }
  return true;
};

const str = "aacc";
const word = "ccac";
// console.log(isValidAnagramHash(str, word));
console.log(isValidAnagram(str, word));
