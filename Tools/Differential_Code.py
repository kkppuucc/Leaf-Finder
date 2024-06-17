def compute_differential_code(chain_code):
    differential_code = []
    n = len(chain_code)

    for i in range(n - 1):
        diff = (chain_code[i] - chain_code[i + 1]) % 8
        differential_code.append(diff)

    final = (chain_code[n - 1] - chain_code[0]) % 8
    differential_code.append(final)

    return differential_code
