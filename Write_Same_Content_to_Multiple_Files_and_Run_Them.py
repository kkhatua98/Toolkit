# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 17:42:16 2020

@author: kkhatua
"""

import os
os.chdir('C:\\Users\\kkhatua\\Desktop\\All Usage Tables')

files = ["VOICE_OG_LOCAL_MOU_N2N",
"VOICE_IC_LOCAL_MOU_N2N",
"VOICE_OG_ISD_MOU_N2N",
"VOICE_IC_ISD_MOU_N2N",
"VOICE_OG_OR_MOU_LOCAL_N2N",
"VOICE_IC_OR_MOU_LOCAL_N2N",
"VOICE_OG_OR_MOU_ISD_N2N",
"VOICE_IC_OR_MOU_ISD_N2N",
"VOICE_OG_LOCAL_MOU_N2O",
"VOICE_IC_LOCAL_MOU_N2O",
"VOICE_OG_ISD_MOU_N2O",
"VOICE_IC_ISD_MOU_N2O",
"VOICE_OG_OR_MOU_LOCAL_N2O",
"VOICE_IC_OR_MOU_LOCAL_N2O",
"VOICE_OG_OR_MOU_ISD_N2O",
"VOICE_IC_OR_MOU_ISD_N2O",
"VAS1",
"VAS2",
"VAS3",
"GPRS_TOTAL_MB",
"GPRS_VIDEO",
"GPRS_COMMUNICATION",
"GPRS_GAMING",
"GPRS_E_COMM",
"GPRS_MUSIC",
"GPRS_TRANSPORTATION",
"GPRS_EDUCATION",
"GPRS_TRAVEL",
"GPRS_BANKING",
"GPRS_F_and_B",
"GPRS_SOCIAL_MEDIA",
"GPRS_2G_USAGE",
"GPRS_3G_USAGE",
"GPRS_4G_USAGE",
"GPRS_5G_USAGE"
]



for file in files:
    print(file)
    content = f'''# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 18:19:01 2020

@author: abilare
"""

import datetime
import os
import random
import csv

os.chdir("C:/Users/kkhatua/Desktop/All Usage Tables")
random.seed(990)

start=datetime.datetime.now()

{file}_csv_open=open(f'{file}.csv','w',newline='')
{file}_csv_writer =csv.writer({file}_csv_open)


{file}_csv_writer.writerow((
"T_ID",
"{file}_SUM_PM12_/SUM_PM34_",
"{file}_MEAN_PM12_/MEAN_PM34_",
"{file}_MEAN_PM1_/MEAN_PM_12345_",
"{file}_MEAN_PM1_/MEAN_PM_12345_"   
))

for i in range(10000):
    print(i)
    if i<=9000: # Non- churners
        {file}_csv_writer.writerow((
                i+1, # Table_Identifier
                random.choice(range(80,200))/100,   # {file}_SUM_PM12_/SUM_PM34_
                random.choice(range(80,200))/100,   # {file}_MEAN_PM12_/MEAN_PM34_
                random.choice(range(80,200))/100,   # {file}_MEAN_PM1_/MEAN_PM_12345_
                random.choice(range(80,200))/100,   # {file}_MEAN_PM1_/MEAN_PM_12345_  
    ))
    else: # churners
        {file}_csv_writer.writerow((
                    i+1, # Table_Identifier
                    random.choice(range(15,120))/100,   # {file}_SUM_PM12_/SUM_PM34_
                    random.choice(range(15,120))/100,   # {file}_MEAN_PM12_/MEAN_PM34_
                    random.choice(range(15,120))/100,   # {file}_MEAN_PM1_/MEAN_PM_12345_
                    random.choice(range(15,120))/100,   # {file}_MEAN_PM1_/MEAN_PM_12345_  
        ))
{file}_csv_open.close()
print(datetime.datetime.now() - start)
'''
    
    destination_file = file + '_Code.py'
    with open(destination_file, 'w') as f:
        f.write(content)

    exec(content)