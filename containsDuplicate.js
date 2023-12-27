const arr = [2,2,5];

var checkDuplicate = (arr) => {
  if (arr.length === 0 || arr.length === 1) return false;

  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] === arr[j]) {
        return true;
      }
    }
  }
  return false;
};

var checkDuplicateSorted = (arr) => {
  arr.sort((a, b) => a - b);

  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] === arr[i + 1]) return true;
  }
  return false;
};

var checkDuplicateSet = (arr) => {
  const sortedSet = new Set();

  for (let i = 0; i < arr.length; i++) {
    if (sortedSet.has(arr[i])) return true;
    sortedSet.add(arr[i]);
  }
  return false;
};

console.log(checkDuplicateSet(arr));
// console.log(checkDuplicateSorted(arr));

// console.log(checkDuplicate(arr));
