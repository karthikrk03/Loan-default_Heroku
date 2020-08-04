#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime


# In[13]:


#import dataset
bank =pd.read_csv("k:\\ExcelR\\Project\\bank_final.csv")


# In[4]:


bank


# In[5]:


bank.describe()


# In[6]:


bank.columns


# In[7]:


bank.isna().sum()


# In[8]:


bank[bank.duplicated()] #15 duplicates


# In[9]:


#Duplicate records removed
bank.drop_duplicates(inplace=True)


# In[10]:


bank.reset_index(drop=True)


# In[11]:


#removing $ symbol
dollar_var=['DisbursementGross','BalanceGross','ChgOffPrinGr','GrAppv','SBA_Appv']


# In[14]:


for i in dollar_var:
    for j in range(len(bank)):
        bank[i][j]=float(bank[i][j].replace("$","").replace(",",""))
        if j%5000==0:
            print(j)


# In[15]:


#OUTPUT VARIABLE ---> MIS_STATUS
sns.countplot(x='MIS_Status', data=bank)


# In[16]:


bank['MIS_Status'].value_counts()


# In[17]:


len(bank.loc[(bank.ChgOffPrinGr>0) & (bank.MIS_Status=='P I F')])


# In[18]:


len(bank.loc[(bank.ChgOffPrinGr==0) & (bank.MIS_Status=='CHGOFF')])


# In[19]:


x=[]
for i in range(len(bank)):
    if bank['MIS_Status'][i] not in ['CHGOFF','P I F']:
        x.append(i)


# In[20]:


a=bank.iloc[x,[18,22,23]]


# In[21]:


#Replacing the NA values of MIS_Status by comparing with values in ChgOffPrinGr
for i in range(len(bank)):
    if bank['MIS_Status'][i] not in ['CHGOFF','P I F']:
        if bank['ChgOffPrinGr'][i]>0:
            bank['MIS_Status'][i]='CHGOFF'
        else:
            bank['MIS_Status'][i]='P I F'
            
#Null values imuted            


# In[22]:


#creating output variable
bank['default']=bank['MIS_Status'].map({'P I F':0,'CHGOFF':1})


# In[23]:


plt.rcParams.update({'figure.figsize':(10,7)})


# In[24]:


sns.countplot(x='default',data= bank)


# In[25]:


bank['default'].value_counts()


# In[26]:


len(bank['Name'].unique())


# In[27]:


len(bank['City'].unique())


# In[28]:


len(bank['State'].unique())


# In[29]:


len(bank['Zip'].unique())


# In[30]:


len(bank['Bank'].unique())


# In[31]:


len(bank['BankState'].unique())


# In[32]:


len(bank['CCSC'].unique())


# In[33]:


len(bank['ApprovalDate'].unique())


# In[34]:


len(bank['ApprovalFY'].unique())


# In[35]:


len(bank['Term'].unique())


# In[36]:


len(bank['NoEmp'].unique())


# In[37]:


len(bank['NewExist'].unique())


# In[38]:


len(bank['CreateJob'].unique())


# In[39]:


len(bank['RetainedJob'].unique())


# In[40]:


len(bank['FranchiseCode'].unique())


# In[41]:


len(bank['UrbanRural'].unique())


# In[42]:


len(bank['RevLineCr'].unique())


# In[43]:


len(bank['LowDoc'].unique())


# In[44]:


len(bank['ChgOffDate'].unique())


# In[45]:


len(bank['DisbursementDate'].unique())


# In[46]:


len(bank['DisbursementGross'].unique())


# In[47]:


len(bank['BalanceGross'].unique())


# In[48]:


len(bank['MIS_Status'].unique())


# In[49]:


len(bank['ChgOffPrinGr'].unique())


# In[50]:


len(bank['GrAppv'].unique())


# In[51]:


len(bank['SBA_Appv'].unique())


# In[52]:


###NewExist###
sns.countplot(x='NewExist',data=bank)
bank['NewExist'].value_counts()


# In[53]:


sns.countplot(x='default',hue='NewExist',data=bank)
bank[['NewExist','default']].groupby(['NewExist']).mean().sort_values(by='default',ascending=False)


# In[54]:


#Imputing with mode
bank.loc[(bank.NewExist !=1) & (bank.NewExist !=2),'NewExist']=1


# In[55]:


###FranchiseCode #####
len(bank.loc[bank['FranchiseCode']>1])


# In[56]:


bank['Franchise']=0
bank.loc[bank.FranchiseCode>1, 'Franchise']=1
bank['Franchise'].unique()


# In[57]:


sns.countplot(x='default',hue='Franchise',data=bank)
bank[['default','Franchise']].groupby(['Franchise']).mean().sort_values(by='Franchise',ascending=True)


# In[58]:


### urbanRural#####
sns.countplot(x='UrbanRural',data=bank)
bank['UrbanRural'].value_counts()


# In[59]:


sns.countplot(x='default',hue='UrbanRural',data=bank)#more cases of urban; majority of unidentified in non-default 
bank[['UrbanRural','default']].groupby(['UrbanRural']).mean().sort_values(by='default',ascending=False)


# In[60]:


####  RevLineCr  ####
sns.countplot(x='RevLineCr',data=bank)
bank['RevLineCr'].value_counts() #0-23659 , T-4819 , (`)-2 , (,)-1


# In[61]:


sns.countplot(x='default',hue='RevLineCr',data=bank)#RevLine of credit not availbale for majority of the businesses
bank[['RevLineCr','default']].groupby(['RevLineCr']).mean().sort_values(by='default',ascending=False)


# In[62]:


#Imputing the wrong entries to 0
bank.loc[(bank.RevLineCr!='Y')&(bank.RevLineCr!='N')&(bank.RevLineCr!='0'),'RevLineCr']='0'


# In[63]:


#creating dummy variable
bank['RevLineCr_yes']=bank['RevLineCr'].map({'N':0,'Y':1,'0':2})


# In[64]:


####  LowDoc  ####
sns.countplot(x='LowDoc',data=bank)
bank['LowDoc'].value_counts()


# In[65]:


sns.countplot(x='default',hue='LowDoc',data=bank)#majority businesses are not under LowDoc
bank[['LowDoc','default']].groupby(['LowDoc']).mean().sort_values(by='default',ascending=False)


# In[66]:


#Imputing with mode
bank.loc[(bank.LowDoc !='Y') & (bank.LowDoc !='N'),'LowDoc']='N' 


# In[67]:


#creating dummy variable
bank['LowDoc_yes']=bank['LowDoc'].map({'N':0,'Y':1})


# In[68]:


####  ChgOffDate  ####
bank['ChgOffDate_Yes']=0
for i in range(len(bank)):
    try:
        if len(bank['ChgOffDate'][i]):
            bank['ChgOffDate_Yes'][i]=1
    except:
        pass


# In[69]:


pd.crosstab(bank.default,bank.ChgOffDate_Yes)


# In[70]:


####  BalanceGross ####
sns.countplot(x='BalanceGross',data=bank)
bank['BalanceGross'].value_counts() 


# In[71]:


bank.loc[bank.BalanceGross != 0,'default']


# In[72]:


####  ChgOffPrinGr  ####
sns.countplot(x=bank['default'],hue=bank['ChgOffPrinGr']==0)


# In[73]:


len(bank.loc[(bank.ChgOffPrinGr>0) & (bank.MIS_Status=='P I F')])


# In[74]:


len(bank.loc[(bank.ChgOffPrinGr==0) & (bank.MIS_Status=='CHGOFF')])


# In[75]:


pd.crosstab(bank.default,bank.ChgOffPrinGr==0)


# In[76]:


####  State  ####
sns.countplot(x='State',data=bank)
bank['State'].value_counts()


# In[77]:


bank[['State','default']].groupby(['State']).mean().sort_values(by='default',ascending=False)


# In[78]:


#Imputing the 2 NA values
a=bank.loc[bank.State.isna()]


# In[79]:


bank.loc[bank.State.isna(),'City']


# In[80]:


bank.loc[bank.State.isna(),'BankState']


# In[81]:


bank.loc[bank.Zip==8070,'State']


# In[82]:


bank.loc[bank.Name=='SO. JERSEY DANCE/MERRYLEES','State']


# In[83]:


bank.loc[bank.City=='PENNSVILLE','State']='NJ'


# In[84]:


bank.loc[bank.City=='JOHNSTOWN       NY','State']='NY'


# In[85]:


#Replacing the States with their probability values(Mean Encoding)
x=bank[['State','default']].groupby(['State']).mean().sort_values(by='default',ascending=False)
x['State']=x.index
x=x.set_index(np.arange(0,51,1))
for i in range(len(x)):
    bank=bank.replace(to_replace =x.State[i], value =x.default[i]) 
    print(i)


# In[86]:


####city####
bank['City'].value_counts()


# In[87]:


bank[['City','default']].groupby(['City']).mean().sort_values(by='default',ascending=False)


# In[88]:


####  Bank  ####
bank['Bank'].value_counts()


# In[89]:


bank[['Bank','default']].groupby(['Bank']).mean().sort_values(by='default',ascending=False)


# In[90]:


####  BankState  ####
sns.countplot(x='BankState',data=bank)
bank['BankState'].value_counts() 


# In[91]:


bank[['BankState','default']].groupby(['BankState']).mean().sort_values(by='default',ascending=False)


# In[92]:


####  ApprovalFY  ####
sns.countplot(x='ApprovalFY',data=bank)# more approvals in 1997-1998 and 2004-2007
bank['ApprovalFY'].value_counts()


# In[93]:


sns.countplot(x='default',hue='ApprovalFY',data=bank)
bank[['ApprovalFY','default']].groupby(['ApprovalFY']).mean().sort_values(by='ApprovalFY',ascending=True)


# In[94]:


len(bank.loc[(bank['ApprovalFY']<=1980)])


# In[95]:


len(bank.loc[(bank['ApprovalFY']>1980) & (bank['ApprovalFY']<1990)])


# In[96]:


len(bank.loc[(bank['ApprovalFY']>1990) & (bank['ApprovalFY']<2003)])


# In[97]:


len(bank.loc[(bank['ApprovalFY']>2003)])


# In[98]:


bank['ApprovalFY_bin']=pd.cut(bank['ApprovalFY'],bins=[1960,1980,1990,2003,2010],labels=[1,2,3,4])


# In[99]:


sns.countplot(x='default',hue='ApprovalFY_bin',data=bank)


# In[100]:


bank[['default','ApprovalFY_bin']].groupby(['ApprovalFY_bin']).mean().sort_values(by='ApprovalFY_bin',ascending=True)


# In[101]:


####  ApprovalDate  ####
bank['ApprovalMonth']=''  #date mapped to month and day
bank['ApprovalDay']=''
for i in range(len(bank)):
    bank['ApprovalMonth'][i]=bank['ApprovalDate'][i][3:6]    
    bank['ApprovalDay'][i]=int(bank['ApprovalDate'][i][:2])
    if i%5000==0:
        print(i)


# In[102]:


sns.countplot(x='default',hue='ApprovalMonth',data=bank)


# In[103]:


bank[['default','ApprovalMonth']].groupby(['ApprovalMonth']).mean().sort_values(by='default',ascending=False)


# In[104]:


sns.countplot(x='ApprovalDay',data=bank)


# In[105]:


bank[['default','ApprovalDay']].groupby(['ApprovalDay']).mean().sort_values(by='ApprovalDay',ascending=True)
#no pattern, equally likely
#Hence ApprovalDate is irrelavant


# In[106]:


sns.distplot(bank['Term'])


# In[107]:


sns.boxplot(x='default',y='Term',data=bank)


# In[108]:


####  Term  ####
sorted(bank['Term'].unique())
len(bank.loc[(bank['Term']==0)])


# In[109]:


len(bank.loc[(bank['Term']==0) & (bank['default']==1)])


# In[110]:


len(bank.loc[(bank['Term']<=60)])


# In[111]:


len(bank.loc[(bank['Term']<=60) & (bank['default']==1)])


# In[112]:


len(bank.loc[(bank['Term']>120) & (bank['Term']<=180)])


# In[113]:


len(bank.loc[(bank['Term']>120) & (bank['Term']<=180)& (bank['default']==1)])


# In[114]:


len(bank.loc[(bank['Term']>300) & (bank['Term']<=360)])


# In[115]:


len(bank.loc[(bank['Term']>300) & (bank['Term']<=360) & (bank['default']==1)])


# In[116]:


len(bank.loc[(bank['Term']>360)])


# In[117]:


len(bank.loc[(bank['Term']>360) & (bank['default']==1)])


# In[118]:


bank['Term_bin']=0
bank['Term_bin']=pd.cut(bank['Term'],bins=[-1,60,120,180,240,300,360,480],labels=[1,2,3,4,5,6,7])


# In[119]:


sns.countplot(x='default',hue='Term_bin',data=bank)#more defaulters for 0-5 year term; more non defaulters for 5-40 year term
bank[['default','Term_bin']].groupby(['Term_bin']).mean().sort_values(by='Term_bin',ascending=True)


# In[120]:


p=pd.DataFrame(bank[['default','Term_bin']].groupby(['Term_bin']).mean())
plt.title("Term VS probability to default")
plt.xlabel("Five year Terms")
plt.ylabel("Probability to default")
plt.bar(p.index,p.default,color='crimson')


# In[121]:


####  NoEmp  ####
sorted(bank['NoEmp'].unique())# min=0 ; max=9999
len(bank.loc[bank['NoEmp']>100]) # only 829 businesses have more than 100 employees


# In[122]:


len(bank.loc[bank['NoEmp']<=5])


# In[123]:


len(bank.loc[bank['NoEmp']<=10])


# In[124]:


len(bank.loc[(bank['NoEmp']>30) & (bank['NoEmp']<=100)])


# In[125]:


len(bank.loc[(bank['NoEmp']>100)&(bank['NoEmp']<=10000)])


# In[126]:


bank['Emp_bin']=0
emp_bin= [-1,5,10,15,20,30,100,1000,10000]
emp_lab=list(range(1,9))
bank['Emp_bin']=pd.cut(bank['NoEmp'], bins=emp_bin,labels=emp_lab)


# In[127]:


sns.countplot(x='default',hue='Emp_bin',data=bank)
bank[['default','Emp_bin']].groupby(['Emp_bin']).mean().sort_values(by='default',ascending=False)


# In[128]:


p=pd.DataFrame(bank[['default','Emp_bin']].groupby(['Emp_bin']).mean())
plt.title("Number of Employees VS probability to default")
plt.xlabel("Number of Employees in bins")
plt.ylabel("Probability to default")
plt.bar(p.index,p.default,color='crimson')


# In[129]:


####  CreateJob ####
sorted(bank['CreateJob'].unique()) #min=0 ; max=3000
len(bank.loc[bank['CreateJob']>100])# only 44 businesses create more than 100 jobs


# In[130]:


len(bank.loc[(bank['CreateJob']>10) & (bank['CreateJob']<=100)])# only 3541 business creates jobs between 10 and 100


# In[131]:


len(bank.loc[(bank['CreateJob']>5) & (bank['CreateJob']<=10)])# 4130


# In[132]:


len(bank.loc[bank['CreateJob']==0])


# In[133]:


bank['CreateJob_bin']=0
bank['CreateJob_bin']=pd.cut(bank['CreateJob'],bins=[-1,0,5,10,100,400,3000],labels=[0,1,2,3,4,5])


# In[134]:


sns.countplot(x='default',hue='CreateJob_bin',data=bank)#same pattern
bank[['default','CreateJob_bin']].groupby(['CreateJob_bin']).mean().sort_values(by='CreateJob_bin',ascending=True)


# In[135]:


####  RetainedJob  ####
sorted(bank['RetainedJob'].unique()) # min=0 ; max=9500
len(bank.loc[bank['RetainedJob']>100])


# In[136]:


len(bank.loc[bank['RetainedJob']<10])


# In[137]:


len(bank.loc[bank['RetainedJob']==0])


# In[138]:


len(bank.loc[(bank['RetainedJob']>100) & (bank['RetainedJob']<=400)])


# In[139]:


len(bank.loc[bank['RetainedJob']>400])


# In[140]:


len(bank.loc[(bank['RetainedJob']>400) & (bank['default']==1)])


# In[141]:


bank['RetainedJob_bin']=0
bank['RetainedJob_bin']=pd.cut(bank['RetainedJob'],bins=[-1,0,5,10,100,400,9500],labels=[0,1,2,3,4,5])


# In[142]:


sns.countplot(x='default',hue='RetainedJob_bin',data=bank)
bank[['default','RetainedJob_bin']].groupby(['RetainedJob_bin']).mean().sort_values(by='RetainedJob_bin',ascending=True)


# In[143]:


####  DisbursementDate  ####
bank['DisbursementYear']=0  #extracting the year alone from date
for i in range(len(bank)):
    try:
        bank['DisbursementYear'][i]=datetime.strptime(bank['DisbursementDate'][i], "%d-%b-%y").year
        if i%5000==0:
            print(i)
    except:                    # due to presence of NA values
        pass


# In[144]:


sns.countplot(x='DisbursementYear',data=bank)


# In[145]:


bank['DisbursementYear'].value_counts()


# In[146]:


bank.loc[bank.DisbursementYear<2000]
bank.loc[bank.DisbursementYear>2010,'default']
bank[['default','DisbursementYear']].groupby(['DisbursementYear']).mean().sort_values(by='DisbursementYear',ascending=True)


# In[147]:


#Imputation
bank['DisbursementYear'].value_counts()


# In[148]:


a=bank.loc[bank.DisbursementYear==0]


# In[149]:


bank.loc[bank.DisbursementYear==0,'default'].value_counts()


# In[150]:


bank[['default','DisbursementYear']].groupby(['DisbursementYear']).mean().sort_values(by='DisbursementYear',ascending=True)


# In[151]:


bank.loc[bank.ApprovalFY==bank.DisbursementYear,['ApprovalFY','DisbursementYear']]


# In[152]:


bank.loc[bank.ApprovalFY<bank.DisbursementYear]


# In[153]:


x=bank.loc[bank.ApprovalFY>bank.DisbursementYear,['ApprovalFY','DisbursementYear']]


# In[154]:


for i in range(len(bank)):
    if (bank.DisbursementYear[i]==0) or (bank.DisbursementYear[i]>2013): 
        bank.DisbursementYear[i]=bank.ApprovalFY[i]


# In[155]:


bank['DisbursementYear_bin']=0
bank['DisbursementYear_bin']=pd.cut(bank['DisbursementYear'],bins=[1960,1984,1998,2003,2008,2013],labels=[1,2,3,4,5])


# In[156]:


sns.countplot(x='default',hue='DisbursementYear_bin',data=bank)#most dates are between 1984-1998 and 2003-2008
bank[['default','DisbursementYear_bin']].groupby(['DisbursementYear_bin']).mean().sort_values(by='DisbursementYear_bin',ascending=True)


# In[157]:


bank['DisbursementYear_bin'].unique()


# In[158]:


####  DisbursementGross  ####
sns.distplot(bank['DisbursementGross'])


# In[159]:


sns.boxplot(x='default',y='DisbursementGross',data=bank)


# In[160]:


bank.loc[bank['DisbursementGross']<10000]


# In[161]:


bank.loc[(bank['DisbursementGross']>10000) & (bank['DisbursementGross']<50000)]


# In[162]:


bank.loc[(bank['DisbursementGross']>50000) & (bank['DisbursementGross']<100000)]#26979


# In[163]:


bank.loc[(bank['DisbursementGross']>100000) & (bank['DisbursementGross']<1000000)]


# In[164]:


bank.loc[(bank['DisbursementGross']>1000000) & (bank['DisbursementGross']<4100000)]


# In[165]:


sns.catplot(x='default',y='DisbursementGross',hue='MIS_Status',kind='bar',data=bank)


# In[166]:


sns.countplot(bank.DisbursementGross>500000,hue=(bank.default==1))


# In[167]:


bank.loc[bank.DisbursementGross<100000]
bank.loc[(bank.DisbursementGross<100000) & (bank.default==1)]#27192/92610=0.293
bank.loc[(bank.DisbursementGross>=100000) & (bank.DisbursementGross<1000000)]
bank.loc[(bank.DisbursementGross>=100000) & (bank.DisbursementGross<1000000)&(bank.default==1)]#11698/55057=0.212
bank.loc[(bank.DisbursementGross>=1000000)]
bank.loc[(bank.DisbursementGross>=1000000) & (bank.default==1)]


# In[168]:


bank['LargeAmount']=0
for i in range(len(bank)):
    if (bank.DisbursementGross[i]>=100000) & (bank.DisbursementGross[i]<1000000):
        bank.LargeAmount[i]=1
    elif (bank.DisbursementGross[i]>=1000000):
        bank.LargeAmount[i]=2


# In[169]:


####  GrAppv  ####
sns.distplot(bank['GrAppv'])#right skewed        
               
len(bank.loc[bank.DisbursementGross>bank.GrAppv])#comparing with DisbursementGross     
len(bank.loc[bank.DisbursementGross<bank.GrAppv])    
len(bank.loc[bank.DisbursementGross==bank.GrAppv])    

len(bank.loc[(bank.DisbursementGross>bank.GrAppv) & (bank.default==1)]) #15820/42218 = 0.374   
len(bank.loc[(bank.DisbursementGross<bank.GrAppv) & (bank.default==1)]) #2223/8287   = 0.268   
len(bank.loc[(bank.DisbursementGross==bank.GrAppv)& (bank.default==1)])


# In[170]:


bank['GrAppv_Disbursement']=0   # 1 when GrAppv is less, 2 when GrAppv is more, 0 when equal
for i in range(len(bank)):
    if bank.GrAppv[i] < bank.DisbursementGross[i]:
        bank.GrAppv_Disbursement[i]=1
    elif bank.GrAppv[i] > bank.DisbursementGross[i]:
        bank.GrAppv_Disbursement[i]=2


# In[171]:


sns.countplot(x='default',hue='GrAppv_Disbursement',data=bank)
bank[['default','GrAppv_Disbursement']].groupby(['GrAppv_Disbursement']).mean().sort_values(by='default',ascending=False)


# In[172]:


####  SBA_Appv  ####
sns.distplot(bank['SBA_Appv'])#right skewed
     
len(bank.loc[bank.DisbursementGross>bank.SBA_Appv]) #comparing with DisbursementGross  
len(bank.loc[bank.DisbursementGross<bank.SBA_Appv])    
len(bank.loc[bank.DisbursementGross==bank.SBA_Appv])    
        
len(bank.loc[(bank.DisbursementGross>bank.SBA_Appv) & (bank.default==1)])  #38875/140123 = 0.277    
len(bank.loc[(bank.DisbursementGross<bank.SBA_Appv) & (bank.default==1)])  #253/2519     = 0.100    
len(bank.loc[(bank.DisbursementGross==bank.SBA_Appv) & (bank.default==1)])


# In[173]:


bank['SBA_Appv_Disbursement']=0   # 1 when SBA_Appv is less, 2 when SBA_Appv is more, 0 when equal
for i in range(len(bank)):
    if bank.SBA_Appv[i] < bank.DisbursementGross[i]:
        bank.SBA_Appv_Disbursement[i]=1
    elif bank.SBA_Appv[i] > bank.DisbursementGross[i]:
        bank.SBA_Appv_Disbursement[i]=2


# In[174]:


sns.countplot(x='default',hue='SBA_Appv_Disbursement',data=bank)
bank[['default','SBA_Appv_Disbursement']].groupby(['SBA_Appv_Disbursement']).mean().sort_values(by='default',ascending=False)


# In[175]:


len(bank.loc[bank.SBA_Appv>bank.GrAppv])#Gross approved amount never less than SBA approved    
len(bank.loc[bank.SBA_Appv<bank.GrAppv])    
len(bank.loc[bank.SBA_Appv==bank.GrAppv])


# In[176]:


bank['NewExist'].value_counts()
a=bank.loc[(bank.NewExist !=1) & (bank.NewExist !=2)]
x=bank.loc[(bank.NewExist ==1),['NoEmp', 'NewExist', 'CreateJob','RetainedJob']]


# In[177]:


bank.loc[(bank.ApprovalFY ==2006),'NewExist'].value_counts()
sns.countplot(bank.CreateJob_bin,hue=bank.NewExist)
bank.loc[(bank.CreateJob_bin ==0),'NewExist'].value_counts()


# In[178]:


sns.countplot(bank.NewExist,hue=bank.NoEmp>100)
sns.countplot(bank.NewExist,hue=bank.CreateJob>100)


# In[179]:


bank['LowDoc'].value_counts()
a=bank.loc[(bank.LowDoc !='Y') & (bank.LowDoc !='N')]
bank.loc[(bank.LowDoc !='Y') & (bank.LowDoc !='N'),'State'].value_counts()
bank.loc[(bank.LowDoc !='Y') & (bank.LowDoc !='N'),'BankState'].value_counts()
bank.loc[(bank.LowDoc !='Y') & (bank.LowDoc !='N'),'ApprovalFY'].value_counts()
bank.loc[(bank.LowDoc !='Y') & (bank.LowDoc !='N'),'DisbursementYear'].value_counts()


# In[180]:


bank.loc[(bank.ApprovalFY==1998),'default'].value_counts()
bank.loc[(bank.State=='TX'),'default'].value_counts()
bank.loc[(bank.ApprovalFY==2006),'LowDoc'].value_counts()#when ApprovalFY=2006 ,LowDoc never Y 
bank.loc[(bank.DisbursementYear==2006),'LowDoc'].value_counts()


# In[181]:


bank['RevLineCr'].value_counts()
a=bank.loc[(bank.RevLineCr!='Y')&(bank.RevLineCr!='N')&(bank.RevLineCr!='0')]
bank.loc[(bank.ApprovalFY ==1998),'RevLineCr'].value_counts()
sns.countplot(bank.UrbanRural,hue=bank.RevLineCr)
sns.countplot(bank.Term_bin,hue=bank.RevLineCr)#if urban,more having revline credit;if rural more not having
sns.countplot(bank.LowDoc,hue=bank.RevLineCr)#if under LowDoc, then no revline credit
a[a.LowDoc=='Y']
a=bank.loc[(bank.RevLineCr!='Y')&(bank.RevLineCr!='N')&(bank.RevLineCr!='0')&(bank.RevLineCr!='T')]
sns.countplot(bank.RevLineCr,hue=bank.LargeAmount)
pd.crosstab(bank.RevLineCr,bank.LargeAmount)


# In[182]:


max(bank.DisbursementGross)
bank[['Term_bin','SBA_Appv']].groupby(['Term_bin']).mean().sort_values(by='Term_bin',ascending=False)
bank[['Term_bin','GrAppv']].groupby(['Term_bin']).mean().sort_values(by='Term_bin',ascending=False)
bank[['Emp_bin','SBA_Appv']].groupby(['Emp_bin']).mean().sort_values(by='Emp_bin',ascending=False)
bank[['CreateJob_bin','SBA_Appv']].groupby(['CreateJob_bin']).mean().sort_values(by='CreateJob_bin',ascending=False)
bank[['RetainedJob_bin','SBA_Appv']].groupby(['RetainedJob_bin']).mean().sort_values(by='RetainedJob_bin',ascending=False)


# In[183]:


bank.loc[bank.SBA_Appv<50000]
bank.loc[(bank.SBA_Appv<50000) & (bank.default==1)]


# In[184]:


bank.loc[(bank.SBA_Appv>=50000) & (bank.SBA_Appv<100000)]
bank.loc[(bank.SBA_Appv>=50000) & (bank.SBA_Appv<100000)&(bank.default==1)]


# In[185]:


bank.loc[(bank.SBA_Appv>=100000) & (bank.SBA_Appv<500000)]
bank.loc[(bank.SBA_Appv>=100000) & (bank.SBA_Appv<500000)&(bank.default==1)]


# In[186]:


bank.loc[(bank.SBA_Appv>=500000)]
bank.loc[(bank.SBA_Appv>=500000) & (bank.default==1)]


# In[187]:


bank.columns

features=['default','State','ApprovalFY','Term','NoEmp','NewExist',
          'CreateJob','RetainedJob','UrbanRural','DisbursementGross',
          'GrAppv','SBA_Appv','Franchise','RevLineCr_yes','LowDoc_yes',
          'DisbursementYear']


bank_clensed=bank[features]


# In[225]:


os.getcwd()
os.chdir("K:/ExcelR/Project")
bank_clensed.to_csv("bank_clean",encoding='utf-8')


# In[188]:


from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
get_ipython().system('pip install xgboost')
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler


# In[189]:


X= bank_clensed.iloc[:,1:]
Y= bank_clensed.iloc[:,0]


# In[190]:


corr_mat= bank_clensed.corr()
top_features = corr_mat.index
sns.heatmap(bank_clensed[top_features].corr(),annot=True, cmap='RdYlGn')


# In[191]:


feature_sel= ExtraTreesClassifier(n_jobs= -1)
feature_sel.fit(X,Y)
score= list(feature_sel.feature_importances_)
col= list(bank_clensed.columns)
col.pop(0)
score_dict= {col[i]:score[i] for i in range(len(col))}
{k: v for k, v in sorted(score_dict.items(), key=lambda item:item[1],reverse =True)}


# In[192]:


#Train-Test-Split
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.25, random_state=0)


# In[193]:


#standardization
sc=StandardScaler()
x_train= sc.fit_transform(x_train)
x_test= sc.transform(x_test)


# In[194]:


####### Model Building#########

# LogisticRegression ######
model = LogisticRegression()
model.fit(x_train,y_train)


# In[195]:


pred =model.predict(x_train)
pd.crosstab(pred, y_train)
np.mean(pred==y_train)


# In[196]:


pred=model.predict(x_test)
pd.crosstab(pred, y_test)
np.mean(pred==y_test)


# In[197]:


#KNN
neigh= KNeighborsClassifier(n_neighbors=3)
neigh.fit(x_train,y_train)
np.mean(neigh.predict(x_train)==y_train)
np.mean(neigh.predict(x_test)==y_test)


# In[198]:


acc=[]
for i in range(3,20,2):
    neigh=KNeighborsClassifier(n_neighbors=i)
    neigh.fit(x_train,y_train)
    accuracy=np.mean(neigh.predict(x_test)==y_test)
    acc.append((i,accuracy))
    print(i)


# In[199]:


#SVM
model=SVC()
model.fit(x_train, y_train)
pred=model.predict(x_train)
np.mean(pred==y_train)


# In[200]:


pred=model.predict(x_test)
np.mean(pred==y_test)


# In[201]:


#Decision Tree
model=DecisionTreeClassifier()
model.fit(x_train,y_train)
pred=model.predict(x_train)
np.mean(pred==y_train)


# In[202]:


pred=model.predict(x_test)
np.mean(pred==y_test)


# In[203]:


#Decision Tree
model=DecisionTreeClassifier()
model.fit(x_train,y_train)
pred=model.predict(x_train)
np.mean(pred==y_train)


# In[204]:


pred=model.predict(x_test)
np.mean(pred==y_test)


# In[229]:


#Random Forest
model=RandomForestClassifier(n_jobs=-1)
model.fit(x_train,y_train)


# In[230]:


pred=model.predict(x_train)
pd.crosstab(pred,y_train)
np.mean(pred==y_train)


# In[231]:


pred=model.predict(x_test)
pd.crosstab(pred,y_test)
np.mean(pred==y_test)
model.score(x_test,y_test)


# In[232]:


cross_val=cross_val_score(model,X,Y,cv=10,n_jobs=-1)
cross_val.mean()


# In[209]:


#XGB
model=XGBClassifier(n_jobs=-1)
model.fit(x_train,y_train)
pred=model.predict(x_train)
np.mean(pred==y_train)


# In[210]:


pred=model.predict(x_test)
np.mean(pred==y_test)
model.score(x_test,y_test)
cross_val=cross_val_score(model,X,Y,cv=10,n_jobs=-1)
cross_val.mean()


# In[211]:


#### Hyperparameter Tuning

#Random Forest
model= RandomForestClassifier(n_jobs=-1)
params= {
         'max_depth':[3,5,10,None],
         'criterion':['gini','entropy'],
         'n_estimators':[100,200,300,400,500],
         'max_features':['auto','sqrt','log2'],
         'bootstrap':[True,False],
         'ccp_alpha':[0.0,0.1,0.2,0.3,0.5]
}


# In[214]:


search=RandomizedSearchCV(estimator=model,param_distributions=params,n_iter=20,n_jobs=-1,cv=5,scoring='roc_auc')
search.fit(X,Y)

search.best_estimator_
search.best_params_
search.best_score_   


# In[215]:


model=RandomForestClassifier(n_jobs=-1,n_estimators=200,)
model.fit(x_train,y_train)
pred=model.predict(x_test)
pd.crosstab(pred,y_test)
np.mean(pred==y_test)


# In[216]:


for i in range(100,1000,100):
    model=RandomForestClassifier(n_jobs=-1,n_estimators=i)
    model.fit(x_train,y_train)
    print((i,model.score(x_test,y_test)))


# In[217]:


#XGBoost
x=np.arange(0.1,0.6,0.2)
for i in x:
    model=XGBClassifier(n_jobs=-1,learning_rate=i)
    model.fit(x_train,y_train)
    print((i,model.score(x_test,y_test)))


# In[218]:


model=XGBClassifier(n_jobs=-1,learning_rate=0.32)
model.fit(x_train,y_train)
model.score(x_train,y_train)
model.score(x_test,y_test)


# In[219]:


for i in range(200,300,10):
    model=XGBClassifier(n_jobs=-1,learning_rate=0.32,n_estimators=i)
    model.fit(x_train,y_train)
    print((i,model.score(x_test,y_test)))


# In[220]:


model=XGBClassifier(n_jobs=-1,learning_rate=0.32,n_estimators=250)
model.fit(x_train,y_train)
model.score(x_train,y_train)
model.score(x_test,y_test)
cross_val=cross_val_score(model,X,Y,cv=10,n_jobs=-1)
cross_val.mean()


# In[221]:


####  Training on whole Dataset  ####

model=XGBClassifier(n_jobs=-1,learning_rate=0.32,n_estimators=250)
sc=StandardScaler()
X_std=sc.fit_transform(X)
model.fit(X_std,Y)


# In[222]:


####  Saving model in system  ####
import pickle
pickle.dump(model,open('model.pkl','wb'))
pickle.dump(sc,open('sc.pkl','wb'))


# In[223]:


####  Load model  ####
model=pickle.load(open('model.pkl','rb'))


# In[224]:


####  testing  ####
response=[0.24,1997,80,4,2,0,0,0,55000,55000,50000,0,0,1,2000]
response=np.array(response).reshape(1,-1)
response=sc.transform(response)
model.predict(response)

