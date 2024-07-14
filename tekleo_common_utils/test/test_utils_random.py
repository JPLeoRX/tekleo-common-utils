from tekleo_common_utils.utils_random import UtilsRandom

utils_random = UtilsRandom()

print(utils_random.get_random_year())
print(utils_random.get_random_docker_name())
print(utils_random.get_random_full_name())
print(utils_random.get_random_first_name())
print(utils_random.get_random_last_name())
print(utils_random.get_random_country())
print(utils_random.get_random_weighted_bool(0.9))
print(utils_random.get_random_weighted_from_list(["a", "b"], [0.1, 0.9], 10))
