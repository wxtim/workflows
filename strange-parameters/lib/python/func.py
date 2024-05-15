def list_to_str(list_):
    return ','.join([str(i) for i in list_])


def fib(n=10):
    """get the first n members of the fibonnaci sequence"""
    seq = [1, 1]
    while seq[-1] < n:
        seq.append(seq[-1] + seq[-2])
    return list_to_str(seq)


def prime(n=10):
    """get first n primes"""
    seq = []
    discards = []
    i = 2
    while len(seq) < n:
        prime = True
        for factor in discards:
            if i % factor == 0:
                prime = False
        if prime:
            seq.append(i)
        discards.append(i)
        i += 1
    return seq
