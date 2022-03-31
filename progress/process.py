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
mon = pRd.read_data()
#%%
'''
**********************************************************************
*************************[Monthly Evaluation]*************************
**********************************************************************
'''

month = mon.monthly(3,22)

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

'''
In December, I lived a very lazy and non-productive life. 
The graph shows that there was no corr -> non-corr graph, but they are
all non-corr -> corr. Which can demonstrate that there were not enough
productive data that would make difference in correlation. 

Maybe, the more correlation graphs I get when compared two months, 
it means that I lived more lazy day. 
'''



#%%
'''
                                [Total]
'''


def Total_n(x, n):
    # x: all_dat
    
    # Set up xlabels (months)
    if len(x['Name'])/n > 15:
        k = round(len(x['Name'])/10)
    else:
        k = n
    months = []
    c = 0
    for i in range(len(x['Name'])):
        if i == c:
            try:
                date = (x['Date'][i]).replace('/2021','')
                if date in months:
                    pass
                else:
                    months.append(date)
            except:
                date = (x['Name'][i][0:6]).strip('"( M[a-zA-Z]S ')
                months.append(date)
            c += k
    
    '''
    if len(months_key)>len(months):
        a = len(months_key)-len(months)
        for i in range(1,a+1):
            add_mon = months_key[-a]['Date']
            c = []
            for j in add_mon:
                first_date = j.split('/')[0]
                if first_date not in c:
                    c.append(first_date)
                    j = j.split('/')
                    j = j[0].strip('0')+'/'+j[1].strip('0')+'/'+j[2]
                    months.append(j)'''
    
    total_interval = len(x['Name'])/len(months)/n
    # Get all total values inclduing the remainders
    c = 0
    d = 1
    total = []
    Total = []
    for i in x['Total']:
        total.append(i)
        if c == n-1:
            total = round((np.sum(total)/n)*100,2)
            Total.append(total)
            total = []
            c = 0
        elif d == len(x['Total']):
            dif = d % n
            total = round((np.sum(total)/dif*100),2)
            Total.append(total)
        else:
            c += 1
        d += 1

    fig, axe = plt.subplots(figsize = (10,5))
    x_p = np.arange(1,len(Total)+1)
    if n < 3:
        axe.plot(x_p, Total, 'r.-', lw=2)
    else:
        axe.plot(x_p, Total, 'ro-', lw=2)
    axe.bar(x_p, Total, color = 'red', alpha = .3)
    axe.set_title('Total [%d days]\n'%n, fontsize = 15, fontweight = 'bold')
    axe.set_ylim((np.min(Total)-10, np.max(Total)+10))
    axe.set_xlabel('Days [by %d]'%n, fontsize = 13)
    axe.set_ylabel('Total %', fontsize = 13)
    axe.set_xticks(np.arange(min(x_p),max(x_p),total_interval))
    axe.set_xticklabels(months)
    if len(x['Name'])/n < 13:
        for i in range(round(len(x['Name'])/n)+1):
            try:
                axe.text(x_p[i], Total[i]+1.5, Total[i], color = 'r', horizontalalignment='center')
            except IndexError:
                pass
    try: 
        plt.savefig('/Volumes/Programming/Personal/progress/jpg files/Monthly Evaluation/Month.jpg', format = 'jpg'
                , dpi=1000, bbox_inches = 'tight')
    except FileNotFoundError:
        plt.savefig('D:\Personal\progress\jpg files\Monthly Evaluation\Month.jpg', format = 'jpg'
                , dpi=1000, bbox_inches = 'tight')


months_key = mon.all_data()[1]
all_dat = mon.all_data()[0]
Total_n(all_dat,10)


'''
Observation : 
    In 7 days graph, a W-shaped graph can be observed. 
Hypothesis  :
    Maybe everyone has different energy pattern where they have different
    weeks that lack energy or proficiency. (Like how girls have period)
    If this hypothesis is true, this can be applied and utilized to 
    increase proficiency.
'''



#%%
'''
Thought Box
'''
''' RISE TIME & WORK DONE [p-value]
    If the p-value between these two factors is not dependent, 
    maybe it means that I'm not utilizing my time wisely.
    Since the more time I have, I should be able to get more things
    done. IOW, the p-value should be lower if I used my time more
    productively
    -> OR it could also mean that I am setting up goals unrealistically
    -> OR it could mean that I work my ass off when I do wake up late
'''


            
        
        













