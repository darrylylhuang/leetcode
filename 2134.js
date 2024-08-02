// Minimum Swaps to Group All 1's Together II

/**
 * @param {number[]} nums
 * @return {number}
 */
var minSwaps = function (nums) {
  // [0], [1], [0, 0], [0, 1], [1, 0], [1, 1]
  if (nums.length < 3) return 0;
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
