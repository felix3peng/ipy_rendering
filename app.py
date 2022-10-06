from IPython import embed, get_ipython, start_ipython
from IPython.terminal.embed import InteractiveShellEmbed
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import os
import sys
from io import StringIO
from traitlets.config import Config
c = Config()

old_stdout = sys.stdout

def main():
    code = '''%%capture output
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range('1/1/2000', periods=1000), columns=list('ABCD'))
df.head()'''
    # c.InteractiveShellApp.exec_lines = code.split('\n')
    c.InteractiveShellApp.exec_lines = [code]
    new_stdout = StringIO()
    sys.stdout = new_stdout
    try:
        get_ipython
        print('found ipython')
    except:
        print('starting ipython')
        start_ipython(argv=['--profile=alterigo'], config=c)
        print('finished ipython')
    else:
        start_ipython(argv=['--profile=alterigo'], config=c)
    sys.stdout = old_stdout
    print(new_stdout.getvalue())

import pandas as pd
import numpy as np

