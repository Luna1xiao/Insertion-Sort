const assert = require('assert');
const { insertion_sort } = require('../src/Insertion_Sort'); 

describe('Insertion Sort', function () {
  it('should return an empty array for an empty input', function () {
    const arr = [];
    insertion_sort(arr);
    assert.deepStrictEqual(arr, []);
  });

  it('should return the same array for a single-element input', function () {
    const arr = [1];
    insertion_sort(arr);
    assert.deepStrictEqual(arr, [1]);
  });

  it('should sort a sorted array', function () {
    const arr = [1, 2, 3, 4, 5];
    insertion_sort(arr);
    assert.deepStrictEqual(arr, [1, 2, 3, 4, 5]);
  });

  it('should sort a reverse-sorted array', function () {
    const arr = [5, 4, 3, 2, 1];
    insertion_sort(arr);
    assert.deepStrictEqual(arr, [1, 2, 3, 4, 5]);
  });

  it('should sort a randomly ordered array', function () {
    const arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5];
    insertion_sort(arr);
    assert.deepStrictEqual(arr, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]);
  });
});
