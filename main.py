import matplotlib.pyplot as plt
from ruamel import yaml
import numpy as np

# a dict discribing global configs
with open('./config.yml', 'r') as f:
    configs = yaml.load(f, yaml.Loader)

from Work import *
from Network import *
from Vote import *
from painter import *

"""
#change the number of works here
n_work = 50
#change the number of members here
n_member = 7
#
n_manual_work = 5
works = []
members = []
for i in range(n_work):
    works.append(Work(i, configs))
for i in range(n_manual_work):
    works.append(Work(i+n_work, configs, manual=configs['manual_works'][i]))
for i in range(n_member):
    members.append(Member(i, configs, token=1000.0))

vote_test = Vote_quadratic(members, works, configs)

vote_test.voting(version=1.2)
#you can specify version=1.1/1.2 to get different results
benefit = vote_test.collect_benefit()

#plot configurations
plt.subplot(1, 2, 1)
token_tendency(vote_test.token_voting)
plt.subplot(1, 2, 2)
draw_prefer_diff_minispantree(members)
plt.show()
"""

work = Work(1, configs)
n_member = 10
members = []
benefit = []
for i in range(n_member):
    members.append(Member(i, configs, token=1000.0))
vote_test = Vote_Sequential(members, work, configs)
vote_test.vote()
for i in range(n_member):
    benefit.append(np.sum(members[i].preference * work.preference))

print(vote_test.condition.votes)
print(benefit)
print(sum(vote_test.condition.votes))
print(sum(benefit))
print(vote_test.outcome)
