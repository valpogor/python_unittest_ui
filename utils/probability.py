# # https://nagornyy.me/en/courses/data-science/bayes/
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pymc3 as pm
# from scipy import stats
# from math import factorial
# import arviz as az
# import matplotlib.pyplot as plt
# import unittest
#
# #%config InlineBackend.figure_format = 'svg'
# plt.rcParams['figure.figsize'] = (10, 6)
# SEED = 12
#
# # class probability(unittest.TestCase):
#     # def setUp(self):
#     #     return self
#
# def num_of_successes(n, k):
#     return factorial(n)/(factorial(k) * factorial(n - k))
#
#
# def test_probability_of_success(p, n, k):
#     C_kn = num_of_successes(n, k)
#     return C_kn * (p**k) * (1 - p)**(n - k)
#
# # Формула Бернулли позволяет ответить на вопрос,
# # какова вероятность в 10 бросках монеты получить 9 «орлов»,
# # если монека честная (вероятность «орла» составляет 50%).
# print(test_probability_of_success(p=0.5, n=10, k=9))
#
#
# n_params = [1, 4, 12]
# p_params = [0.25, 0.5, 0.75]
#
# f, ax = plt.subplots(len(n_params), len(p_params), sharex=True, sharey=True)
# for i in range(3):
#     for j in range(3):
#         n = n_params[i]
#         p = p_params[j]
#         y = [test_probability_of_success(p=p, n=n, k=i) for i in range(n+1)]
#         ax[i,j].vlines(range(0, n + 1), 0, y, colors='b', lw=5)
#         ax[i,j].set_ylim(0, 1)
#         ax[i,j].plot(0, 0, label="n = {:3.2f}\np ={:3.2f}".format(n, p), alpha=0)
#         ax[i,j].legend(fontsize=10)
# print(ax[2,1].set_xlabel('$\\theta$', fontsize=14))
# print(ax[1,0].set_ylabel('$p(y|\\theta)$', fontsize=14))
#
#
# n_trials = [0, 1, 2, 3, 4, 8, 16, 32, 50, 150]
# data = [0, 1, 1, 1, 1, 4, 6, 9, 13, 48]
# theta_real = 0.35
#
# beta_params = [(1, 1), (20, 20), (1, 4)]
# x = np.linspace(0, 1, 200)
#
# for idx, N in enumerate(n_trials):
#     if idx == 0:
#         plt.subplot(4, 3, 2)
#     else:
#         plt.subplot(4, 3, idx+3)
#     y = data[idx]
#     for (a_prior, b_prior) in beta_params:
#         # это получилось после перемножения биноминального на бета
#         p_theta_given_y = stats.beta.pdf(x, a_prior + y, b_prior + N - y)
#         plt.fill_between(x, 0, p_theta_given_y, alpha=0.7)
#     plt.xlabel('θ')
#     plt.axvline(theta_real, ymax=0.3, color='k')
#     plt.plot(0, 0, label=f'{N:4d} trials\n{y:4d} heads', alpha=0)
#     plt.legend()
#     plt.tight_layout()
#     # if __name__ == "__main__":
#     #     unittest.main()
#
# np.random.seed(12)
# n_experiments = 4
# theta_real = 0.35
# data = stats.bernoulli.rvs(p=theta_real, size=n_experiments)
#
# with pm.Model() as flip_coin:
#     # a priori
#     θ = pm.Beta('θ', alpha=1., beta=1.)
#     # likelihood
#     y = pm.Bernoulli('y', p=θ, observed=data)
#     trace = pm.sample(1000, random_seed=12, njobs=2)
# pm.model_to_graphviz(flip_coin)
# pm.summary(trace)
# pm.traceplot(trace, lines={'θ':theta_real}, skip_first=100);
# pm.gelman_rubin(trace)
# pm.forestplot(trace);
# pm.plot_posterior(trace, kde_plot=True, rope=[.3, .4]);
# pm.autocorrplot(trace);
# # pm.effective_n(chain)
