import os
import shutil
import pandas as pd
import numpy as np

# Note: change  \  to  /  to get it to work
SDListFile = ("R:/01_GCP/01_AccuEarth/01_2023_07/6946_AccuEarth_2307_import/6946_Export_JP.csv")
SDList = pd.read_csv(SDListFile)

srcPath  = ("R:/01_GCP/01_AccuEarth/01_2023_07/6946_AccuEarth_2307_import/Temp_SD/")
dstPath =  ("R:/01_GCP/01_AccuEarth/01_2023_07/6946_AccuEarth_2307_import/Temp_SD/out/")

for i in range (0, len(SDList)):
    PIDsd   = SDList.loc[i,'PID'] + ".gif"
    GCPIDsd = str(SDList.loc[i,'GCPID']) + ".gif"  # the GCPID is a num, so str() converts the num to a string so we can append .gif
    print (PIDsd, "-> ", GCPIDsd)
    srcFile = os.path.join(srcPath, PIDsd)
    dstFile = os.path.join(dstPath, GCPIDsd)
    shutil.copy(srcFile, dstFile)
