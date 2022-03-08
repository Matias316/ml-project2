import matplotlib.pyplot as plt
import seaborn as sns


def display_count_plot(df1, df2):
    """Plot a count plot using the dataframes received as parameters

    Args:
        df1 (dataframe)
        df2 (dataframe)

    """
    # TODO - Improve function accuracy:
    # This is not best approach to identify positive tweets:
    # 1) It doesn't include keywords in other languages
    # 2) It doesn't apply a semantic analysis
    positive_tweets = ['excellent', 'best', 'awesome', 'fantastic', 'out of this world', 'superior', 'greatest', 'highest goalscorer', 'most assists']
    df1['relevance'] = df1.apply(lambda row: 'Positive' if any([item in row['text'] for item in positive_tweets]) else 'Undetermined', axis = 1)
    df2['relevance'] = df2.apply(lambda row: 'Positive' if any([item in row['text'] for item in positive_tweets]) else 'Undetermined', axis = 1)    

    fig, ax = plt.subplots(1, 2)
    ax[0].title.set_text('Messi')
    ax[1].title.set_text('Ronaldo')
    sns.countplot(x='lang', ax=ax[0], data=df1, hue='relevance')
    sns.countplot(x='lang', ax=ax[1], data=df2, hue='relevance')

    plt.show()
