// 1. Two Sum

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let mp = {};
  for (let i = 0; i < nums.length; i++) {
    let num = nums[i];
    if (target - num in mp) {
      return [i, mp[target - num]];
    }
    mp[num] = i;
  }
};

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var solution1 = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) return [i, j];
    }
  }
};

/**
 * Doesn't work
 * @param {number[]} list
 * @param {number} number
 * @returns {number}
 */
var numberInList = function (list, number) {
  if (list.length === 1) return list[0] === number ? 0 : -1;
  else {
    console.log(list.length);
    const mid = Math.floor(list.length / 2);
    // console.log(mid);
    const indexL = numberInList(list.slice(0, mid), number);
    const indexR = numberInList(list.slice(mid, list.length));
    if (indexL !== -1) return indexL;
    if (indexR !== -1) return indexR + 1;
    return -1;
  }
};

// console.log(twoSum([2, 7, 11, 15], 9));
// console.log(twoSum([3, 2, 4], 6));
// console.log(twoSum([3, 3], 6));
