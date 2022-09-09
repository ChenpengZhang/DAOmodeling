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

n_work = 50
n_member = 7
works = []
members = []
for i in range(n_work):
    works.append(Work(i, configs))
for i in range(n_member):
    members.append(Member(i, configs, token=1000.0))

vote_test = Vote_quadratic(members, works, configs)

vote_test.voting()
#you can specify version_name=1.1/1.2 to get different results
#version 1.2 now have bugs
benefit = vote_test.collect_benefit()

plt.subplot(1, 2, 1)
token_tendency(vote_test.token_voting)
plt.subplot(1, 2, 2)
draw_prefer_diff_minispantree(members)
plt.show()
