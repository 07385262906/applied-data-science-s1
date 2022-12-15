import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def extract_data(filename, countries, indicator):
    data_frame = pd.read_csv(filename, skiprows=(4), index_col=False)
    data_frame.info()
    data_frame = data_frame.loc[:, ~data_frame.columns.str.contains('^Unnamed')]
    data_frame = data_frame.loc[data_frame['Country Name'].isin(countries)]
    data_frame = data_frame.loc[data_frame['Indicator Code'].eq(indicator)]
    df2 = data_frame.melt(id_vars=['Country Name', 'Country Code',
                  'Indicator Name', 'Indicator Code'], var_name='Years')
    del df2['Country Code']
    df2 = df2.pivot_table('value', [
                          'Years', 'Indicator Name', 'Indicator Code'], 'Country Name').reset_index()
    df_countries = data_frame
    df_years = df2
    df_countries.dropna()
    df_years.dropna()

    return df_countries, df_years


countries = ['Germany', 'Australia',
             'United States', 'China', 'United Kingdom']
df_c, df_y = extract_data(
    'data.csv', countries, 'AG.LND.FRST.ZS')


num = np.arange(5)
width = 0.2
df_y = df_y.loc[df_y['Years'].isin(['2000', '2001', '2002', '2003', '2004'])]
years = df_y['Years'].tolist()

plt.figure(dpi=144)
plt.title('Forest area (% of land area)')
plt.bar(num, df_y['Germany'], width, label='Germany')
plt.bar(num+0.2, df_y['Australia'], width, label='Australia')
plt.bar(num-0.2, df_y['United States'], width, label='United States')
plt.bar(num-0.4, df_y['China'], width, label='China')
plt.xticks(num, years)
plt.xlabel('Years')
plt.ylabel('% of land area')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()

df_c, df_y = extract_data(
    'data.csv', countries, 'AG.LND.AGRI.ZS')
num = np.arange(5)
width = 0.2
df_y = df_y.loc[df_y['Years'].isin(['2000', '2001', '2002', '2003', '2004'])]
years = df_y['Years'].tolist()

plt.figure(dpi=144)
plt.title('Agricultural land (% of land area)')
plt.bar(num, df_y['Germany'], width, label='Germany')
plt.bar(num+0.2, df_y['Australia'], width, label='Australia')
plt.bar(num-0.2, df_y['United States'], width, label='United States')
plt.bar(num-0.4, df_y['China'], width, label='China')
plt.xticks(num, years)
plt.xlabel('Years')
plt.ylabel('% of land area')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
