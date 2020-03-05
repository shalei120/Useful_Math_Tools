import math


def p_value(model_num, baseline_accuracy, model_accuracy, double_sided, baseline_num=None):

    if baseline_num is None:
        baseline_num = model_num

    pavg = (baseline_num * baseline_accuracy + model_num * model_accuracy) / (baseline_num + model_num)
    z = (model_accuracy - baseline_accuracy) / (pavg * (1 - pavg) * (1.0 / model_num + 1.0 / baseline_num)) ** 0.5
    pvalue = 1 - 0.5 * (1 + math.erf(z / 2.0 ** 0.5))
    if double_sided:
        pvalue = pvalue * 2
    return pvalue



if __name__ == '__main__':
    print(p_value(10, 0.9544, 0.9666, False))
    print(p_value(1000, 0.9544, 0.9666, False))
    print(p_value(10, 0.9544, 0.9666, True))
    print(p_value(1000, 0.9544, 0.9666, True))