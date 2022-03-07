import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def display_sources_of_energy_heatmap(df):
    """Displays a heatmap showing sources of energy tendency

    Args:
        df (dataframe)

    """

    df_records_from_28_countries = df[~df['Area'].isin(['EU-27', 'EU27+1'])]

    sns.heatmap(pd.crosstab(df_records_from_28_countries["Variable"],
                            df_records_from_28_countries["Year"],
                            values=df_records_from_28_countries["Generation (TWh)"], aggfunc='mean').round(
        0),
        annot=True,
        cbar=False, linewidths=.5)

    plt.show()


def display_sources_of_energy_production_last_3_years(df):
    """Displays a barplot showing sources of energy and share of production from the last 3 years (2018, 2019, 2020)

    Args:
        df (dataframe)

    """
    df_records_from_all_countries = df[df['Area'].isin(['EU27+1'])]
    df_records_from_all_countries_last_3_years = df_records_from_all_countries[
        df_records_from_all_countries['Year'].isin([2018, 2019, 2020])]
    plt.figure(figsize=(20, 5))

    sns.barplot(x='Variable', y='Share of production (%)', hue='Year', data=df_records_from_all_countries_last_3_years)

    plt.show()


def display_3_sources_of_energy_comparison(df, sources_of_energy_list):
    """Displays a lineplot comparing 3 sources of energy through the years

    Args:
        df (dataframe)
        sources_of_energy_list (list): Identifies the sources of energy considered in the analysis

    """

    df_records_from_28_countries = df[~df['Area'].isin(['EU-27', 'EU27+1'])]
    df_records_from_28_countries_3_sources_of_energy = df_records_from_28_countries[
        df_records_from_28_countries['Variable'].isin(sources_of_energy_list)]

    fig, ax = plt.subplots(1, 2)
    ax[0].title.set_text('Comparison using 95% ci')
    ax[1].title.set_text('Comparison using sd')

    sns.lineplot(x='Year', y='Generation (TWh)', hue='Variable', data=df_records_from_28_countries_3_sources_of_energy,
                 ci=95, estimator='mean', ax=ax[0])

    sns.lineplot(x='Year', y='Generation (TWh)', hue='Variable', data=df_records_from_28_countries_3_sources_of_energy,
                 ci='sd', estimator='mean', ax=ax[1])

    plt.show()


def display_analysis_source_of_energy_per_country(df, sources_of_energy_list):
    """Displays a lineplot showing share of production through the years for sources of energy indicated

    Args:
        df (dataframe)
        sources_of_energy_list (list): Identifies the sources of energy considered in the analysis

    """
    df_records_from_28_countries = df[~df['Area'].isin(['EU-27', 'EU27+1'])]
    df_records_from_28_countries_for_source_of_energy = df_records_from_28_countries[
        df_records_from_28_countries['Variable'].isin(sources_of_energy_list)]

    g = sns.FacetGrid(df_records_from_28_countries_for_source_of_energy, col='Area', hue='Variable')
    g.map(sns.lineplot, "Year", "Share of production (%)")
    g.add_legend()

    plt.show()
