import math


def n_choose_k(n, k):
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))


def p_bingo(n_total, n_card, n_picked, n_hit):

    x = 1.0 / n_choose_k(n_total, n_picked)
    y = n_choose_k(n_card, n_hit)
    z = n_choose_k(n_total-n_card, n_picked-n_hit)

    return x*y*z


def p_n_ppl_hit(p_hit, n_ppl_total, n_ppl_hit):

    x = n_choose_k(n_ppl_total, n_ppl_hit)
    y = math.pow(p_hit, n_ppl_hit)
    z = math.pow(1-p_hit, n_ppl_total-n_ppl_hit)

    return x*y*z


def p_anyone_normal_bingo(n_picked, n_ppl_total):

    n_total = 15
    n_card = 5
    target_n_hit = 5

    pb = p_bingo(n_total, n_card, n_picked, target_n_hit)

    # 1 - probability that no one has hit yet
    return 1 - p_n_ppl_hit(pb, n_ppl_total, 0)
