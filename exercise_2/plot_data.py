import matplotlib.pyplot as plt
import seaborn as sns


def display_count_plot(df1, df2):
    """Plot a count plot using the dataframes received as parameters

    Args:
        df1 (dataframe)
        df2 (dataframe)

    """
    fig, ax = plt.subplots(1, 2)
    ax[0].title.set_text('Messi')
    ax[1].title.set_text('Ronaldo')
    sns.countplot(x='lang', ax=ax[0], data=df1)
    sns.countplot(x='lang', ax=ax[1], data=df2)

    plt.show()
