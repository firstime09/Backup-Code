import streamlit as st
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
st.write(f"Accuracy: {accuracy:.2f}")

st.sidebar.header("Input New Data")
sepal_length = st.sidebar.slider("Sepal Length", float(iris.data[:, 0].min()), float(iris.data[:, 0].max()))
sepal_width = st.sidebar.slider("Sepal Width", float(iris.data[:, 1].min()), float(iris.data[:, 1].max()))
petal_length = st.sidebar.slider("Petal Length", float(iris.data[:, 2].min()), float(iris.data[:, 2].max()))
petal_width = st.sidebar.slider("Petal Width", float(iris.data[:, 3].min()), float(iris.data[:, 3].max()))

user_input = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = knn.predict(user_input)
st.write(f"Predicted Class: {iris.target_names[prediction[0]]}")
