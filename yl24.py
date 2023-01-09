def upc_check(code):
    check_code = list(code)[0:-1:1]
    check_digit = list(code)[-1]
    even_sum = sum(map(int, check_code[1::2]))
    odd_sum = sum(map(int, check_code[0::2]))
    modulus = ((odd_sum * 3) + even_sum) % 10
    test_digit = (10 - modulus) % 10
    return (True, test_digit) if test_digit == int(check_digit) else (False, test_digit)


def upc_find(check_code):
    print(check_code)


print(upc_check("036000291452")[0])
upc_find(upc_check("12345678910")[1])
