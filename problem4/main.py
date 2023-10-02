def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes_grid(width, height, start):
    result = ""
    current_num = start + 1
    for i in range(height):
        row = []
        for j in range(width):
            while not is_prime(current_num):
                current_num += 1
            row.append(current_num)
            current_num += 1
        result += " ".join("{:<2}".format(num) for num in row) + "\n"
    return result

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """