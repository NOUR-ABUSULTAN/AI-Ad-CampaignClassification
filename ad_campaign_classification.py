
# مشروع الذكاء الاصطناعي: توقّع تحوّل المستخدم (Conversions) من بيانات الحملات الإعلانية
# مقارنة بين ثلاث خوارزميات تصنيف: SVM / Decision Tree / Random Forest
# البيئة: Google Colab + Python + scikit-learn

import zipfile
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


with zipfile.ZipFile('archive (1).zip', 'r') as zip_ref:
    zip_ref.extractall()


df = pd.read_csv('ad_campaign_data.csv')


X = df[['age', 'gender', 'impressions', 'clicks']]
Y = df['conversions']


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


print("الدقة هي :", SVC(kernel='linear').fit(X_train, Y_train).score(X_test, Y_test))

svm_model = SVC(kernel='linear').fit(X_train, Y_train)
print("1.دقة خوارزمية SVM هي", svm_model.score(X_test, Y_test))

dt_model = DecisionTreeClassifier().fit(X_train, Y_train)
print("2.دقة خوارزمية Desision Tree هي:", dt_model.score(X_test, Y_test))

rf_model = RandomForestClassifier().fit(X_train, Y_train)
print("3. دقة خوارزمية Random Forest هي:", rf_model.score(X_test, Y_test))
