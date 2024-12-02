import os
import matplotlib.pyplot as plt


def load_style_sheet():
    base_dir = os.path.dirname(__file__)
    style_path = os.path.join(base_dir, 'assets', 'JS.mplstyle')

    if os.path.exists(style_path):
        plt.style.use(style_path)
        print('style loaded')
    else:
        print('could not find style sheet file')