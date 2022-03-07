from exercise_1.database_connection import *
from exercise_1.special_customers import *
from exercise_1.high_freight import *
from exercise_1.countries_with_suppliers_or_customers import *
from exercise_2.read_datasource import *
from exercise_2.plot_data import *
from exercise_3.read_datasource import *
from exercise_3.plot_data import *

PATH_TO_DB = 'datasource/Northwind_large.sqlite'
PATH_TO_JSON_FILES = 'datasource'
PATH_TO_EXCEL_FILE = 'datasource/Europe-Power.xlsx'

if __name__ == "__main__":
    # Exercise 1
    with connect_db(PATH_TO_DB) as con:
        df_special_customers = get_special_customers(con)
        customers_greater_than_70000 = [[row['CustomerID'], row['Total']] for index, row in
                                        df_special_customers.iterrows() if row['Total'] > 70000]
        print(customers_greater_than_70000)

        df_high_freight = get_high_freight(con)
        print(df_high_freight)

        df_countries_with_suppliers_or_customers = get_countries_with_suppliers_or_customers(con)
        print(df_countries_with_suppliers_or_customers)

    # Exercise 2
    df_messi = load_dataframe_from_json_files(PATH_TO_JSON_FILES, 'Messi')
    df_ronaldo = load_dataframe_from_json_files(PATH_TO_JSON_FILES, 'Ronaldo')
    display_count_plot(df_messi, df_ronaldo)

    # Exercise 3
    df_europe_power = load_dataframe_from_excel_file(PATH_TO_EXCEL_FILE)

    # Only keep records corresponding to energies
    df_only_energy_records = df_europe_power[df_europe_power['Variable'].isin(
        ['Lignite', 'Hard Coal', 'Gas', 'Other fossil', 'Nuclear', 'Hydro', 'Solar', 'Wind', 'Bioenergy',
         'Other renewables'])]

    # 3.1
    display_sources_of_energy_heatmap(df_only_energy_records)
    # 3.2
    display_sources_of_energy_production_last_3_years(df_only_energy_records)

    # 3.3
    sources_of_energy_list = ['Solar', 'Wind', 'Bioenergy']
    display_3_sources_of_energy_comparison(df_only_energy_records, sources_of_energy_list)

    # 3.4
    display_analysis_source_of_energy_per_country(df_only_energy_records, sources_of_energy_list=['Nuclear'])
    display_analysis_source_of_energy_per_country(df_only_energy_records,
                                                 sources_of_energy_list=['Solar', 'Wind', 'Hydro', 'Bioenergy',
                                                                         'Other renewables'])
