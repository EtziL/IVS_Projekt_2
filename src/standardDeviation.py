from calcMath import *
from typing import List
import cProfile

def standard_deviation(numbers_list: List[int]) -> float:
    n: int = len(numbers_list)
    mean: float = div(sum(numbers_list), n)  # aritmeticky prumer
    fraction: float = div(1, sub(n, 1))  # 1/n-1
    bracket: float = sum([power(x - mean, 2) for x in numbers_list])  # suma
    result: float = root(2, mul(fraction, bracket))  # smerodatna odchylka
    return result


if __name__ == '__main__':
    prof = cProfile.Profile()
    prof.enable()  # profiling start

    input_str: str = input()
    numbers_string: List[str] = input_str.split()
    numbers: List[int] = [int(i) for i in numbers_string]
    print(standard_deviation(numbers))

    prof.disable()  # profiling end
    prof.print_stats(sort='calls')  # vypise profiling na stdout
    prof.dump_stats("profiling_out.prof")  # vygeneruje prof soubor napr. pro snakeviz

