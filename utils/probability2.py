# from matplotlib import pyplot
# from numpy.random import normal
# from numpy import hstack
# from numpy import mean
# from numpy import std
# from scipy.stats import norm
# from matplotlib import pyplot
# from numpy.random import normal
# from numpy import hstack
# from numpy import asarray
# from numpy import exp
# from sklearn.neighbors import KernelDensity
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import stats
#
# # # generate a sample
# # sample = normal(loc=50, scale=5, size=1000)
# # # calculate parameters
# # sample_mean = mean(sample)
# # sample_std = std(sample)
# # print('Mean=%.3f, Standard Deviation=%.3f' % (sample_mean, sample_std))
# # # define the distribution
# # dist = norm(sample_mean, sample_std)
# # # sample probabilities for a range of outcomes
# # values = [value for value in range(30, 70)]
# # probabilities = [dist.pdf(value) for value in values]
# # # plot the histogram and pdf
# # pyplot.hist(sample, bins=10, density=True)
# # pyplot.plot(values, probabilities)
# # pyplot.show()
#
# #2
# # # generate a sample
# # sample1 = normal(loc=20, scale=5, size=300)
# # sample2 = normal(loc=40, scale=5, size=700)
# # sample = hstack((sample1, sample2))
# # # plot the histogram
# # pyplot.hist(sample, bins=50)
# # pyplot.show()
#
# #3
# # #generate a sample
# # sample1 = normal(loc=20, scale=5, size=300)
# # sample2 = normal(loc=40, scale=5, size=700)
# # sample = hstack((sample1, sample2))
# # # fit density
# # model = KernelDensity(bandwidth=2, kernel='gaussian')
# # sample = sample.reshape((len(sample), 1))
# # model.fit(sample)
# # # sample probabilities for a range of outcomes
# # values = asarray([value for value in range(1, 60)])
# # values = values.reshape((len(values), 1))
# # probabilities = model.score_samples(values)
# # probabilities = exp(probabilities)
# # # plot the histogram and pdf
# # pyplot.hist(sample, bins=50, density=True)
# # pyplot.plot(values[:], probabilities)
# # pyplot.show()
#
# #4
#
#
#
# np.random.seed(12456)
# x1 = np.random.normal(size=200)  # random data, normal distribution
# xs = np.linspace(x1.min()-1, x1.max()+1, 200)
#
# kde1 = stats.gaussian_kde(x1)
# kde2 = stats.gaussian_kde(x1, bw_method='silverman')
#
# fig = plt.figure(figsize=(8, 6))
#
# ax1 = fig.add_subplot(211)
# ax1.plot(x1, np.zeros(x1.shape), 'b+', ms=12)  # rug plot
# ax1.plot(xs, kde1(xs), 'k-', label="Scott's Rule")
# ax1.plot(xs, kde2(xs), 'b-', label="Silverman's Rule")
# ax1.plot(xs, stats.norm.pdf(xs), 'r--', label="True PDF")
#
# ax1.set_xlabel('x')
# ax1.set_ylabel('Density')
# ax1.set_title("Normal (top) and Student's T$_{df=5}$ (bottom) distributions")
# ax1.legend(loc=1)
#
# x2 = stats.t.rvs(5, size=200)  # random data, T distribution
# xs = np.linspace(x2.min() - 1, x2.max() + 1, 200)
#
# kde3 = stats.gaussian_kde(x2)
# kde4 = stats.gaussian_kde(x2, bw_method='silverman')
#
# ax2 = fig.add_subplot(212)
# ax2.plot(x2, np.zeros(x2.shape), 'b+', ms=12)  # rug plot
# ax2.plot(xs, kde3(xs), 'k-', label="Scott's Rule")
# ax2.plot(xs, kde4(xs), 'b-', label="Silverman's Rule")
# ax2.plot(xs, stats.t.pdf(xs, 5), 'r--', label="True PDF")
#
# ax2.set_xlabel('x')
# ax2.set_ylabel('Density')
#
# plt.show()