import matplotlib.pyplot as plt
import seaborn as sns

def visualize_distribution(data, column, color):
    """
    Visualize the distribution of a numerical feature.

    Args:
    data (pd.DataFrame): The input dataset.
    column (str): The column to visualize.
    color (str): The color of the plot.
    """
    sns.histplot(data[column], kde=True, color=color)
    plt.title(f'Distribution of {column}')
    plt.show()

def visualize_categorical(data, column, hue, palette):
    """
    Visualize a categorical feature.

    Args:
    data (pd.DataFrame): The input dataset.
    column (str): The column to visualize.
    hue (str): The column to color the plot.
    palette (str): The color palette.
    """
    sns.countplot(data=data, x=column, palette=palette, hue=hue)
    plt.title(f'Distribution of {column}')
    plt.show()

def visualize_correlation(data, columns):
    """
    Visualize the correlation matrix between numerical features.

    Args:
    data (pd.DataFrame): The input dataset.
    columns (list): The list of columns to include in the correlation matrix.
    """
    corr_matrix = data[columns].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()

def visualize_outliers(data, columns):
    """
    Visualize outliers in numerical features using boxplots.

    Args:
    data (pd.DataFrame): The input dataset.
    columns (list): The list of columns to include in the boxplot.
    """
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=data[columns])
    plt.title('Boxplot of Numerical Features')
    plt.show()