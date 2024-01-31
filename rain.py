from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Assume you have a DataFrame `df` with your data
df = pd.read_csv('weather_data.csv')

# Preprocess the data
# Here we just drop missing values for simplicity
df = df.dropna()

# Assume 'Temperature', 'Humidity', 'Pressure' are features
# and 'Rain' is the target
X = df[['Temperature', 'Humidity', 'Pressure']]
y = df['Rain']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Make predictions on the test set
predictions = clf.predict(X_test)

# Now `predictions` is an array with the model's predictions for whether it will rain
