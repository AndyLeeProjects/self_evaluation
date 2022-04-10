# -*- coding: utf-8 -*-
'''
Imports
'''
import numpy as np
from matplotlib import pyplot as plt
import sys
import os
if os.name == 'posix':
    sys.path.append('/Volumes/Programming/Personal/progress/myPackage')
else:
    sys.path.append('D:\Personal\progress\myPackage')
import processReadData as pRd
import processCorr as pCor
import processMonth as pMon

#%%
'''
**********************************************************************
*************************[Monthly Evaluation]*************************
**********************************************************************
'''
mon = pRd.read_data()
month = mon.monthly(4,22)

# Monthly Evaluation Plot
pMon.monthly_eval(month)
#%%
'''
                            [Monthly Improvement]
'''

month1 = mon.monthly(10,21)
month2 = mon.monthly(11,21)
inputMonths = [month1, month2]
a = pMon.improvement(inputMonths)


#%%
'''
                                [Read All Data]
'''

all_dat = mon.all_data()[0]
months_key = mon.all_data()[1]

#%%
'''
                            [Monthly Correlatin Plot]
'''
# Correlations in month_dat
month = mon.monthly(11,21)
test_results_month = pCor.PearsonTest(month)
pCor.All_cor_plots(test_results_month[1],test_results_month[2])

#%%
'''
                            [Plot All Correlations]
'''
# Corrleations in all_dat
all_dat = mon.all_data()[0]
test_results = pCor.PearsonTest(all_dat)
pCor.All_cor_plots(test_results[1],test_results[2])



#%%

'''
**********************************************************************
***************************[Test Dependency]**************************
**********************************************************************
'''
#%%
'''
[Month Correlation Plot: specific variable]
    - Correlation Evaluation by Days 
'''

# Read Data again
month = mon.monthly(11, 21)

# Tests for correlation in data (monthly scope)
# Type in any name of the variable and a month!
pCor.DEP_m('Meditation',month)

#%%
'''
                            [N number of PLOT]
    -Plot Evaluation by n (Dependent variables)
'''

# Type in any title!
pMon.DEP_n('Meditation', 30)


#%%
'''
 [Correlation change within 2 specific months]
'''
mon1 = mon.monthly(10,21)
mon2 = mon.monthly(11,21)

M = [mon1,mon2]
month_cor_change = pCor.correlation_change(M)
print(month_cor_change[1])

#%%
'''
 [Correlation change in Overall & Specific Month]
'''


months_key = mon.all_data()[1]
M = [months_key, mon2]
overall_cor_change = pCor.correlation_change_overall(M)
print(overall_cor_change[1])


#%%

''' Choose Comparison Type [month & ovearll] '''

comp_type = 'overall'

if 'm' in comp_type or 'M' in comp_type:
    cor_dat = month_cor_change[0]
    months = month_cor_change[2]
else:
    cor_dat = overall_cor_change[0]
    months = overall_cor_change[2]


fig, axe = plt.subplots(figsize = (10,6))
for i in cor_dat:
    change = [i[1],i[2]]
    if i[3] < 0:
        axe.plot(change, '--' ,label = i[0][11:].strip('*'))
    else:
        axe.plot(change, label = i[0][11:].strip('*'))
axe.set_title('Change of Correlations\n%s & %s'%(months[0],months[1]), fontsize = 15, fontweight = 'bold')
axe.set_xlabel('\nNEG Slope: became more dependent\nPOS Slope: became more independent', fontsize = 12, fontweight = 'bold')
axe.legend()
try:
    plt.savefig('/Volumes/Programming/Personal/progress/jpg files/Monthly Evaluation/Correlation Change.jpg', format = 'jpg'
            , dpi=1000, bbox_inches = 'tight')
except FileNotFoundError:
    plt.savefig('D:\Personal\progress\jpg files\Monthly Evaluation\Correlation Change.jpg', format = 'jpg'
            , dpi=1000, bbox_inches = 'tight')

        
        













