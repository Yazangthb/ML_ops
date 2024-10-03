import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression


df=pd.read_csv("data\diamonds.csv")
pd.set_option('display.max_columns',None)

tdf=pd.get_dummies(df['cut'])
df=pd.concat([df,tdf],axis=1)
df.drop(columns='cut',axis=1,inplace=True)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['color']=le.fit_transform(df['color'])

tdf=pd.get_dummies(df['clarity'],prefix='clarity')
df=pd.concat([df,tdf],axis=1)
df.drop(columns=['clarity','Unnamed: 0'],axis=1,inplace=True)

df['vol']=df['x']*df['y']*df['z']
df=df.rename(columns={'x':'Length','y':'Width','z':'Depth'})

from sklearn.feature_selection import mutual_info_regression
t_x=df.drop(columns='price')
t_y=df['price']
mi=mutual_info_regression(t_x,t_y)
mi_scores_df = pd.DataFrame({'Feature': t_x.columns, 'MI Score':mi})
mi_scores_df = mi_scores_df.sort_values(by='MI Score', ascending=False)

ss=StandardScaler()
x=df.drop(columns='price')
y=df['price']
x_t,x_te,y_t,y_te=train_test_split(x,y,test_size=0.25,random_state=20)
r_xt=ss.fit_transform(x_t)
r_xte=ss.transform(x_te)
r_yt=y_t.copy()
r_yte=y_te.copy()

reg=LinearRegression()
reg.fit(r_xt,r_yt)
import pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(reg, f)