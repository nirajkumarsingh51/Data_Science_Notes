import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("trending_videos.csv")

# -----------------------------
# Basic Information
# -----------------------------
print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== NULL VALUES =====")
print(df.isnull().sum())

print("\n===== STATISTICS =====")
print(df.describe())

# -----------------------------
# Remove Missing Values
# -----------------------------
df = df.dropna()

# -----------------------------
# Top Channels
# -----------------------------
if 'channel_title' in df.columns:

    top_channels = df['channel_title'].value_counts().head(10)

    plt.figure(figsize=(12,6))
    sns.barplot(x=top_channels.values, y=top_channels.index, palette='viridis')

    plt.title("Top 10 Channels")
    plt.xlabel("Number of Trending Videos")
    plt.ylabel("Channel Name")

    plt.show()

# -----------------------------
# Most Viewed Videos
# -----------------------------
if 'views' in df.columns:

    top_views = df.nlargest(10, 'views')

    plt.figure(figsize=(12,6))

    sns.barplot(
        x=top_views['views'],
        y=top_views['title'],
        palette='magma'
    )

    plt.title("Top 10 Most Viewed Videos")
    plt.xlabel("Views")
    plt.ylabel("Video Title")

    plt.show()

# -----------------------------
# Likes vs Views
# -----------------------------
if 'likes' in df.columns and 'views' in df.columns:

    plt.figure(figsize=(10,6))

    sns.scatterplot(
        x=df['views'],
        y=df['likes'],
        color='blue'
    )

    plt.title("Views vs Likes")
    plt.xlabel("Views")
    plt.ylabel("Likes")

    plt.show()

# -----------------------------
# Correlation Heatmap
# -----------------------------
numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(10,8))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.show()

# -----------------------------
# Category Analysis
# -----------------------------
if 'category_id' in df.columns:

    plt.figure(figsize=(12,6))

    sns.countplot(
        x='category_id',
        data=df,
        palette='Set2'
    )

    plt.title("Video Categories")
    plt.xlabel("Category ID")
    plt.ylabel("Count")

    plt.show()

# -----------------------------
# Save Cleaned Dataset
# -----------------------------
df.to_csv("cleaned_trending_videos.csv", index=False)

print("\nAnalysis Completed Successfully!")