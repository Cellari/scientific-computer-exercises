from fizzbuzz import fizzbuzz
import random
def test_fizzbuzz():
    iterations = 100
    min_value = -10000
    max_value = 10000
    rand = random.randrange

    simple_tests = [
        [0, "fizzbuzz"],
        [1, 1],
        [-2, -2],
        [3, "fizz"],
        [-5, "buzz"],
        [15, "fizzbuzz"],
        [-12984, "fizz"],
        [29485, "buzz"]
    ]
    for (value, expected) in simple_tests:
        result = fizzbuzz(value)
        assert result == expected

    robustness_tests = [
        [lambda: rand(min_value,max_value) * 3 * 5, ["fizzbuzz"], True],
        [lambda: rand(min_value,max_value) * 5, ["buzz", "fizzbuzz"], True],
        [lambda: rand(min_value,max_value) * 3, ["fizz", "fizzbuzz"], True]
    ]
    for (rand_function, comparison, expected) in robustness_tests:
        for _ in range(0,iterations):
            value = rand_function() #random value with multiplications
            result = fizzbuzz(value)
            assert (result in comparison) == expected

    robustness_num_return_tests = [[lambda: rand(min_value,max_value), True]]
    for (rand_function, expected) in robustness_num_return_tests:
        for _ in range(0,iterations):
            value = rand_function()
            result = fizzbuzz(value)
            if isinstance(result, int):
                assert (result == value) == expected

if __name__ == "__main__":
    test_fizzbuzz()