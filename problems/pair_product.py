# Write a function, pair_product, that takes in a list and a target product as arguments.
# The function should return a tuple containing a pair of indices whose elements multiply to the given target.
# The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair whose product is the target.

#PYTHON IMPLEMENTATION
def pair_product(numbers, target_product):
  map = {}
  for index, num in enumerate(numbers):
    complement = target_product / num
    if complement in map:
      return (map[complement], index)
    map[num] = index

#JAVASCRIPT IMPLEMENTATION:
const pairProduct = (numbers, targetProduct) => {
  const previousNums = {};
  for (let i = 0; i < numbers.length; i += 1) {
    const num = numbers[i];
    const complement = targetProduct / num;

    if (complement in previousNums) return [ previousNums[complement], i ];

    previousNums[num] = i;
  }
};
#Time Complexity:
# The time complexity for this O(n) as it will only have to iterate through the list once.
#Inserting and lookup in the hashmap created will also be constant time O(n)
