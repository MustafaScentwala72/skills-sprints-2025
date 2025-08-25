    # Minimal sklearn pipeline template
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score
import pandas as pd

df = pd.read_csv('data/sample.csv')  # replace with your path
y = df['target']
X = df.drop(columns=['target'])

numeric = X.select_dtypes(include=['int64','float64']).columns.tolist()
categorical = X.select_dtypes(include=['object','category']).columns.tolist()

pre = ColumnTransformer([
    ('num', Pipeline([
        ('impute', SimpleImputer(strategy='median')),
        ('scale', StandardScaler())
    ]), numeric),
    ('cat', Pipeline([
        ('impute', SimpleImputer(strategy='most_frequent')),
        ('ohe', OneHotEncoder(handle_unknown='ignore'))
    ]), categorical)
])

pipe = Pipeline([
    ('pre', pre),
    ('clf', LogisticRegression(max_iter=1000))
])

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(pipe, X, y, cv=cv, scoring='f1')
print('F1:', scores.mean())
