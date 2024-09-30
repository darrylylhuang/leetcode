// Minimum Swaps to Group All 1's Together II

/**
 * @param {number[]} nums
 * @return {number}
 */
var minSwaps = function (nums) {
  // [0], [1], [0, 0], [0, 1], [1, 0], [1, 1]
  // Include len 3: array is circular
  if (nums.length < 4) return 0;
  let swaps = 0;
  let attached = false;
  const deatched1s = [];
  for (let i = 0; i < nums.length; i++) {
    // check neighbours
    const curr = nums[i];
    const prev = nums[i - 1];
    const next = nums[i + 1];
    // current 1 is detached
    if (curr === 1 && prev === 0 && next === 0) {
      deatched1s.push(i);
      attached = false;
    }
    // attach a 1
    else if (curr === 0 && deatched1s.length !== 0 && next === 1) {
      nums[i] = 1;
      nums[deatched1s.pop()] = 0;
      swaps++;
    }
  }
  return swaps;
};

var testCases = function () {
  let cases = [];

  cases.push([[0, 1, 0, 1, 1, 0, 0], 1]);
  cases.push([[0, 1, 1, 1, 0, 0, 1, 1, 0], 2]);
  cases.push([[1, 1, 0, 0, 1], 0]);

  cases.forEach((s) => test(s));
};

var test = function (s) {
  const test = minSwaps(s[0]);
  console.log(`Expected:${s[1]}`, `Received:${test}`);
};

testCases();
