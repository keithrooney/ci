from . import asserts
import math


def euclidean_distance(p, q):
    """
    What would you use this for?
    Why would you use this?
    When do you use this?
    How would you use this?

    :param p:
    :param q:
    :return:
    """
    asserts.is_equal(len(p), len(q))
    divisor = sum(map(lambda pt: pow(pt[0] - pt[1], 2), zip(p, q)))
    if divisor == 0:
        return 0
    else:
        return 1 / (1 + math.sqrt(divisor))


def pearsons_correlation(p, q):
    """
    What would you use this for?
    Why would you use this?
    When do you use this?
    How would you use this?

    :param p:
    :param q:
    :return:
    """
    asserts.is_equal(len(p), len(q))

    sq_sum_p = sum(map(lambda e: e ** 2, p))
    sq_sum_q = sum(map(lambda e: e ** 2, q))

    number = sum(map(lambda pt: pt[0] * pt[1], zip(p, q))) - (sum(p) * sum(q) / len(p))
    divisor = math.sqrt((sq_sum_p - pow(sum(p), 2) / len(p)) * (sq_sum_q - pow(sum(q), 2) / len(q)))

    if divisor == 0:
        return 0
    else:
        return number / divisor
