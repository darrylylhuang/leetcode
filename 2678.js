// Number of Senior Citizens

/**
 * @param {string[]} details
 * @return {number}
 */
var countSeniors = function (details) {
  let over60 = 0;
  details.forEach((el) => {
    if (parseInt(el.substring(11, 13)) > 60) over60++;
  });
  return over60;
};
