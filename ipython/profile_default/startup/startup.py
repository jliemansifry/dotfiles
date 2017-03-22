import os
import os.path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Bigger default seaborn font size
# See https://stanford.edu/~mwaskom/software/seaborn/tutorial/aesthetics.html
sns.set_context('notebook', font_scale=1.5)

# Show more characters per line than the default of 80
pd.options.display.width = 120
