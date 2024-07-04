from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score

import pandas as pd

# Define the column names based on the description
columns = [
    "Sample Code Number", "Type", "Clump Thickness", "Uniformity of Cell Size",
    "Uniformity of Cell Shape", "Marginal Adhesion", "Single Epithelial Cell Size",
    "Bare Nuclei", "Bland Chromatin", "Normal Nucleoli", "Mitoses"
]
df = pd.DataFrame(columns=columns)
with open("datacum.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        if line.startswith("#") or line.startswith("\n"):
            lines.remove(line)
        else:
            l=line.strip().split(",")
            new_row = {
                "Sample Code Number": l[0],
                "Type": l[1],
                "Clump Thickness": int(l[2]),
                "Uniformity of Cell Size": int(l[3]),
                "Uniformity of Cell Shape": int(l[4]),
                "Marginal Adhesion": int(l[5]),
                "Single Epithelial Cell Size": int(l[6]),
                "Bare Nuclei": int(l[7]),
                "Bland Chromatin": int(l[8]),
                "Normal Nucleoli": int(l[9]),
                "Mitoses": int(l[10])
            }

            df = df._append(new_row, ignore_index=True)

print("info about the dataset:")
print(df.info())
# print("\nDistribution of classes in the dataset:")
# print(df.value_counts())

#Setup X and y data
# Assuming 'df' is your DataFrame with the data
# Replace 'Type' with the actual column name containing the classification
X_train, X_test, y_train, y_test = train_test_split(
    df.drop(['Type', 'Sample Code Number'], axis=1),  # Features (excluding 'Type' and 'Sample Code Number')
    df['Type'],  # Target variable ('Type' column)
    test_size=120,  # Total test size (80 benign + 40 malignant)
    stratify=df['Type'],  # Ensures equal distribution of classes in train and test sets
    random_state=42
)

# Display the shape of training and testing sets
print("\nTraining and Testing sets:")
print("Training set shape:", X_train.shape)
print("Testing set shape:", X_test.shape)

print("\nDistribution of classes in the test set:")
print(y_test.value_counts())

# df_training = df.sample(frac=0.8, random_state=0)
# X_data = df.drop(["Type","Sample Code Number"], axis=1)
# y_labels = df["Type"]

# Create a Gaussian Naive Bayes classifier
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# Predict the class for the test set
y_pred = gnb.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label="2")  # Assuming 2 is the positive class (benign)
recall = recall_score(y_test, y_pred, pos_label="2")

# Print the evaluation metrics
print("\nEvaluation metrics:")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
