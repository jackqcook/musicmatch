import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs

# Parameters
n_samples = 100000  # Total number of profiles
male_ratio = 0.5  # 50% of profiles will be male

# Generate synthetic cluster centers for musical preferences
n_features = 5  # Number of music preference features
centers = 6 # Number of distinct "music clusters" or archetypes
X, _ = make_blobs(n_samples=n_samples, centers=centers, n_features=n_features, random_state=42)

# Assign gender
genders = np.random.choice(['Male', 'Female'], size=n_samples, p=[male_ratio, 1 - male_ratio])

# Assign other attributes (age, etc.)
ages = np.random.randint(18, 40, n_samples)

# Combine into a DataFrame
data = pd.DataFrame(X, columns=[f'preference_{i}' for i in range(n_features)])
data['gender'] = genders
data['age'] = ages

# Sample output
print(data.head())
