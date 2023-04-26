// Write a function, fiveSort, that takes in an array of numbers as an argument. The function should rearrange elements of the array such that all 5s appear at the end. Your function should perform this operation in-place by mutating the original array. The function should return the array.

// Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the array.

const fiveSort = (nums) => {
    for (let i = nums.length - 1; i >= 0; i--) {
      if (nums[i] === 5) {
        nums.splice(i, 1);
        nums.push(5);
      }
    }
    return nums;
  };

  module.exports = {
    fiveSort,
  };
