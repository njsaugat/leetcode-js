function groupAnagrams(strs) {
  const ans = new Object({});
  for (let i = 0; i < strs.length; i++) {
    const count = Array(26).fill(0);
    let str = strs[i];
    for (let j = 0; j < str.length; j++) {
      let diff = str[j].charCodeAt(0) - "a".charCodeAt(0);
      count[diff] += 1;
    }
    const previous = ans[count];

    ans[count] = previous ? [...previous, str] : [str];
  }
  return Object.values(ans);
}
const strs = ["eat", "tea", "tan", "ate", "nat", "bat"];
console.log(groupAnagrams(strs));
