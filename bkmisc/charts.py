import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class PredictionsTable():
    def __init__(self, y_true, pred_probas):
        self.y_true = y_true
        self.pred_probas = pred_probas

    def __repr__(self):
        df = np.cumsum(self.y_true)
        return repr(df)




'''
raw_data_pp = raw_data.loc[raw_data.score_pp > 0, ['score_pp', 'YprePierwsze']]
raw_data_kp = raw_data.loc[raw_data.score_kp > 0, ['score_kp', 'YpreKolejne']]
# sort values
sorted_df = raw_data_pp.sort_values(by=['score_pp'])

# computing necessary values

sorted_df['cum_target'] = np.cumsum(sorted_df.YprePierwsze)
sorted_df['cum_nontarget'] = np.cumsum(sorted_df['YprePierwsze'].apply(lambda x: 0 if x==1 else 1))
#sorted_df['n'] = sorted_df.shape[0]
sorted_df['pct_target'] = sorted_df.cum_target / np.max(sorted_df.cum_target)
sorted_df['pct_nontarget'] = sorted_df.cum_nontarget /np.max(sorted_df.cum_nontarget)
sorted_df['KS'] = np.abs(sorted_df.pct_target - sorted_df.pct_nontarget) * 100

plt.plot(sorted_df.score_pp, sorted_df.pct_target)
plt.plot(sorted_df.score_pp, sorted_df.pct_nontarget)
plt.show()
'''