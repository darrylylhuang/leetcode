// 3. Longest Substring Without Repeating Characters

// REFINED

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  // return lengthOfLongestSubstring1(s);
  return lengthOfLongestSubstring2(s);
};

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring1 = function (s) {
  let seen = {};
  let lastSeen = -1;
  let longest = 0;
  let current = 0;
  for (let i = 0; i < s.length; i++) {
    if (seen[s[i]] === undefined) {
      // i is the index where the letter s[i] was last seen
    } else {
      if (current > longest) longest = current;
      if (lastSeen < seen[s[i]]) {
        current -= seen[s[i]] + 1;
        lastSeen = seen[s[i]];
      }
    }
    seen[s[i]] = i;
    current++;
  }

  if (current > longest) longest = current;
  return longest;
};

// INTUITION - RETURN STRING VERSION

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring2 = function (s) {
  return findLongestSubstring(s).length;
};

/**
 * @param {string} s
 * @returns {string}
 */
var findLongestSubstring = function (s) {
  let lastSeen = -1;
  let seen = {};
  let longestSubstring = "";
  let currentSubstring = "";
  for (let i = 0; i < s.length; i++) {
    if (seen[s[i]] !== undefined) {
      if (currentSubstring.length > longestSubstring.length)
        longestSubstring = currentSubstring;
      if (lastSeen < seen[s[i]]) {
        currentSubstring = currentSubstring.slice(seen[s[i]] - lastSeen);
        lastSeen = seen[s[i]];
      }
    }
    // i is the index where the letter s[i] was last seen
    seen[s[i]] = i;
    currentSubstring += s[i];

    // debugging
    console.log("curr", currentSubstring);
    console.log("long", longestSubstring);
  }

  if (currentSubstring.length > longestSubstring.length)
    longestSubstring = currentSubstring;
  return longestSubstring;
};

var testCases = function () {
  let cases = [];

  cases.push(["abcabcbb", 3]);
  cases.push(["bbbbb", 1]);
  cases.push(["pwwkew", 3]);
  cases.push(["aab", 2]);
  cases.push(["dvdf", 3]);
  cases.push(["tmmzuxt", 5]);
  cases.push(["bbtablud", 6]);

  cases.forEach((s) => test(s));
};

var test = function (s) {
  const test = lengthOfLongestSubstring(s[0]);
  console.log(`Expected:${s[1]}`, `Received:${test}`);
};

testCases();
