import numpy as np
import time


def finds_pairs(numbers_list: list, number_sum: int) -> list:
    """Method to find pairs of numbers on list which sum is equals to the given value.

    Time complexity: O(n).
    """

    unordered_set: set = set()

    pairs: set = set()

    for i in range(len(numbers_list)):

        if number_sum - numbers_list[i] in unordered_set:
            pairs.add(((number_sum - numbers_list[i]), numbers_list[i]))

        else:
            unordered_set.add(numbers_list[i])

    return pairs


def find_pairs_n2(numbers_list: list, number_sum: int) -> list:
    """Method to find pairs of numbers on list which sum is equals to the given value.

    Time complexity: O(n^2).
    """

    pairs: set = set()

    for i in range(0, len(numbers_list)):

        for j in range(i + 1, len(numbers_list)):

            if numbers_list[i] + numbers_list[j] == number_sum:
                pairs.add((numbers_list[i], numbers_list[j]))

    return pairs


# Given value
sum_number: int = 12

# Example list
#  array: list = [1, 9, 5, 0, 20, -4, 12, 16, 7]

#  Generated list using numpy
array: list = list(set(np.random.randint(-10000, 10000, size=20000)))

if __name__ == '__main__':
    # Using hashing. Time complexity: O(n)
    # Time of execution of finds_pairs method
    start_time = time.time()
    pairs1: list = finds_pairs(array, sum_number)
    print("Seconds: %s" % (time.time() - start_time))
    print(*pairs1)

    # Using for loops. Time complexity: O(n^2)
    # Time of execution of finds_pairs_n2 method
    start_time = time.time()
    pairs2 = find_pairs_n2(array, sum_number)
    print("Seconds: %s" % (time.time() - start_time))
    print(*pairs2)

    # Compare find pairs methods
    print(pairs1 == pairs2)
