// Time O(n^2) space O(1)
var twoSum = (nums, target) => {
  for (let curr = 0; curr < nums.length; curr++) {
    const complement = target - nums[curr];

    for (let next = curr + 1; next < nums.length; next++) {
      const num = nums[next];
      const isTarget = num === complement;
      if (isTarget) return [curr, next];
    }
  }
  return [-1, 1];
};

// Time O(n) space O(n)
var twoSum = (nums, target) => {
  const map = getMap(nums);
  return getSum(nums, target, map);
};

const getMap = (nums, map = new Map()) => {
  for (let index = 0; index < nums.length; index++) {
    map.set(nums[index], index);
  }
  return map;
};

const getSum = (nums, target, map) => {
  for (let index = 0; index < nums.length; index++) {
    const complement = target - nums[index];
    const sumIndex = map.get(complement);

    const isTarget = map.has(complement) && sumIndex !== index; //for duplicate
    if (isTarget) return [index, sumIndex];
  }

  return [-1, -1];
};

// time O(n) | space O(n) | 1 pass

var twoSum = (nums, target, map = new Map()) => {
  for (let index = 0; index < nums.length; index++) {
    const num = nums[index];
    const complement = target - num;
    const sumIndex = map.get(complement);

    const isTarget = map.has(complement);
    if (isTarget) return [index, sumIndex];

    map.set(num, index);
  }
  return [-1, -1];
};

/**
1st approach --> brute force N^2, and check for compliment
2nd approach --> create hash map at first step and then again iterate
3rd approach --> start with empty hash map and start looping and keep adding
 */
