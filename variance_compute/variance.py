import numpy as np
import argparse


def compute_variance(sample_array):
    mean = np.mean(sample_array)
    squared_average = sum(np.square(sample_array))/len(sample_array)
    return squared_average - mean*mean


if __name__ == '__main__':
    print("Variance Computation of Binomial Samples")
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--num_steps', type=int, default=100)
    parser.add_argument('-p', '--probability', type=float, default=0.5)
    args = parser.parse_args()

    print("Number of steps: ", args.num_steps)

    n, p = 1, args.probability
    samples = np.random.binomial(n, p, args.num_steps)

    var = compute_variance(samples)
    print('variance (numerical) = ', var)
    print('variance (analytical) = ', n*p*(1.0-p))
