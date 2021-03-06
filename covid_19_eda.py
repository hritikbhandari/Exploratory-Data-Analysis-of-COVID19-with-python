# -*- coding: utf-8 -*-
"""COVID-19-EDA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16OFAMKLgyjOFs-eYOvwjcMNVb2JQjGmL

# COVID19 EXPLORATORY DATA ANALYSIS WITH PYTHON

This notebook conatins an Exploratory Data Analysis of the pandemic Covid19 based on the dataset available from the Johns Hopkins University(https://github.com/CSSEGISandData/COVID-19).
I have made no statistical or predictive modeling as of now keeping in mind the sesitivity of the situation and some problems that predictions can create.

The main reasons for using the JHU data are:

JHU is already a trusted and respected institution,
They cite many sources, which are themselves reputable,
The data is updated daily, and
It is provided directly in the github repository (.csv in a github repository).

## Exploratory data analysis and visualization using Python

### Imports and data

Let's import the necessary packages from the SciPy stack and get [the data](https://github.com/CSSEGISandData/COVID-19).
"""

# Commented out IPython magic to ensure Python compatibility.
# Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Set style & figures inline
sns.set()
# %matplotlib inline

# Data urls
base_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'
confirmed_cases_data_url = base_url + 'time_series_covid19_confirmed_global.csv'
death_cases_data_url = base_url + 'time_series_covid19_deaths_global.csv'
recovery_cases_data_url = base_url+ 'time_series_covid19_recovered_global.csv'

# Import datasets as pandas dataframes
raw_confirmed_df = pd.read_csv(confirmed_cases_data_url)
raw_deaths_df = pd.read_csv(death_cases_data_url)
raw_recovered_df = pd.read_csv(recovery_cases_data_url)

"""### Analysing the Confirmed cases of COVID-19"""

raw_confirmed_df.head()

"""Using .info() and .describe()"""

raw_confirmed_df.info()

raw_confirmed_df.describe()

"""### Number of confirmed cases by country"""

raw_confirmed_df.tail()

raw_confirmed_df.head()

"""From the head and tail observations, its visible that each entry contains the data belonging to the Province/State of a country.

We will take all the rows (*regions/provinces*) that correspond to that country and add up the numbers for each. To put this in data-analytic-speak, we want to **group by** the country column and sum up all the values for the other columns.
"""

# Group by region (we'll also drop 'Lat', 'Long' as it doesn't make sense to sum them here)
confirmed_df = raw_confirmed_df.groupby(['Country/Region']).sum().drop(["Lat", "Long"], axis=1)
confirmed_df.head()

"""So each row of our new dataframe `confirmed_df` is a time series of the number of confirmed cases for each country.
Now we'll have a look at the index of our dataframe.
"""

confirmed_df.index

"""It's indexed by `Country/Region`. That's all good **but** if we index by date **instead**, it will allow us to produce some visualizations almost immediately. 

To make the index the set of dates, notice that the column names are the dates. To turn column names into the index, we essentially want to make the columns the rows and vice versa. This corresponds to taking the transpose of the dataframe:
"""

confirmed_df = confirmed_df.transpose()
confirmed_df.head()

"""Now, let's have a look at our index to see whether it actually consists of DateTimes or not"""

confirmed_df.index

"""Note that `dtype='object'`which means that these are strings, not DateTimes. We will use `pandas` to turn it into a DateTimeIndex:"""

# Set index as DateTimeIndex
datetime_index = pd.DatetimeIndex(confirmed_df.index)
confirmed_df.set_index(datetime_index, inplace=True)
# Check out index
confirmed_df.index

"""Now we have a DateTimeIndex and Countries for columns, we can use the dataframe plotting method to visualize the time series of confirmed number of cases by country.

### Plotting confirmed cases by country
"""

# Plotting time series of several countries (as plotting for all the countries will make the visualization a mess)
countries = ['China', 'US', 'Italy', 'France', 'Spain', 'Australia', 'India']
confirmed_df[countries].plot(figsize=(20,10), linewidth=5, colormap='Accent', fontsize=20)

"""Now, Let's label our axes and give the figure a title. We'll also thin the line and add points for the data."""

# Plot time series of several countries of interest
confirmed_df[countries].plot(figsize=(20,10), linewidth=2, marker='.', colormap='brg', fontsize=20)
plt.xlabel('Date', fontsize=20);
plt.ylabel('Reported Confirmed cases count', fontsize=20);
plt.title('Reported Confirmed Cases Time Series', fontsize=20);

"""Now, since the US data seems to be going really high. lets take the y-axis on logarithmic scale:"""

# Plot time series of several countries of interest
confirmed_df[countries].plot(figsize=(20,10), linewidth=2, marker='.', fontsize=20, logy =True )
plt.xlabel('Date', fontsize = 20)
plt.ylabel('Reported Confirmed Cases on Log Scale')
plt.title('Reported Confirmed Cases Time Series Plot')

"""Till now, we have explored the confirmed cases data and :
- looked at the dataset containing the number of reported confirmed cases for each region,
- wrangled the data to look at the number of reported confirmed cases by country,
- plotted the number of reported confirmed cases by country (both log and semi-log),
- Used log plots for the data.

### Number of reported deaths

As we did above for `raw_data_confirmed`, let's check out the head and the info of the `raw_data_deaths` dataframe:
"""

raw_deaths_df.head()

raw_deaths_df.info()

"""The structure of this data is similar to the `raw_confirmed_df`, so we can apply the same steps used above.

### Number of reported deaths by country
"""

#group-by countries
deaths_df = raw_deaths_df.groupby(['Country/Region']).sum().drop(['Lat','Long'], axis=1)
deaths_df.head()

# Transpose
deaths_df = deaths_df.transpose()

deaths_df.head()

# Set index as DateTimeIndex
datetime_index = pd.DatetimeIndex(deaths_df.index)
deaths_df.set_index(datetime_index, inplace=True)

# Check out head
deaths_df.head()

deaths_df.index

"""### Plotting number of reported deaths by country

Visualizing the number of reported deaths:
"""

# Plot time series of several countries of interest
deaths_df[countries].plot(figsize=(20,10), linewidth=2, marker='.', colormap='CMRmap_r', fontsize=20)
plt.xlabel('Date', fontsize=20);
plt.ylabel('Number of Reported Deaths', fontsize=20);
plt.title('Reported Deaths Time Series', fontsize=20);

# Plot time series of several countries of interest
deaths_df[countries].plot(figsize=(20,10), linewidth=2, marker='.', colormap='brg', fontsize=20)
plt.xlabel('Date', fontsize=20);
plt.ylabel('Number of Reported Deaths', fontsize=20);
plt.title('Reported Deaths Time Series', fontsize=20);

"""Now on a semi-log plot:"""

# Plot time series of countries on log scale
deaths_df[countries].plot(figsize=(20,10), linewidth=2, marker='.', colormap='brg', fontsize=20, logy=True)
plt.xlabel('Date', fontsize=20);
plt.ylabel('Number of Reported Deaths', fontsize=20);
plt.title('Reported Deaths Time Series', fontsize=20);

"""### Aligning growth curves to start with day of number of known deaths ≥ 25

To compare what's happening in different countries, we can align each country's growth curves to all start on the day when the number of known deaths ≥ 25, such as reported in the first figure [here](https://www.nytimes.com/interactive/2020/03/21/upshot/coronavirus-deaths-by-country.html).
To achieve this, first off, let's set set all values less than 25 to NaN so that the associated data points don't get plotted at all when we visualize the data:
"""

# Loop over columns & set values < 25 to None
for col in deaths_df.columns:
    deaths_df.loc[(deaths_df[col] < 25),col] = None

# Check out tail
deaths_df.tail()

"""Now let's plot as above to make sure we see what we think we should see:"""

# Plot time series of several countries of interest
countries = ['China', 'US', 'Italy', 'France', 'Spain', 'India']
deaths_df[countries].plot(figsize=(20,10), linewidth=2, marker='.', colormap='Accent_r', fontsize=20)
plt.xlabel('Date', fontsize=20)
plt.ylabel('Number of Reported Deaths', fontsize=20)
plt.title('Reported Deaths Time Series', fontsize=20)

"""The countries that have seen less than 25 total deaths will have columns of all NaNs now so let's drop these and then see how many columns we have left:"""

# Drop columns that are all NaNs (i.e. countries that haven't yet reached 25 deaths)
deaths_df.dropna(axis=1, how='all', inplace=True)
deaths_df.info()

"""As we're going to align the countries from the day they first had at least 25 deaths, we won't need the DateTimeIndex. In fact, we won't need the date at all. So we can 
- Reset the Index, which will give us an ordinal index (which turns the date into a regular column) and
- Drop the date column (which will be called 'index) after the reset.
"""

# sort index, drop date column
deaths_df_drop = deaths_df.reset_index().drop(['index'], axis=1)
deaths_df_drop.head()

"""Now it's time to shift each column so that the first entry is the first NaN value that it contains! To do this, we can use the `shift()` method on each column. How much do we shift each column, though? The magnitude of the shift is given by how many NaNs there are at the start of the column, which we can retrieve using the `first_valid_index()` method on the column **but** we want to shift **up**, which is negative in direction (by convention and perhaps intuition). SO let's do it."""

# shift
for col in deaths_df_drop.columns:
    deaths_df_drop[col] = deaths_df_drop[col].shift(-deaths_df_drop[col].first_valid_index())
# check out head
deaths_df_drop.head()

"""Now we get to plot our time series, first with linear axes, then semi-log:"""

# Plot time series 
ax = deaths_df_drop.plot(figsize=(20,10), linewidth=2, marker=".", fontsize=20)
ax.legend(ncol=3, loc='upper right')
plt.xlabel('Days', fontsize=20);
plt.ylabel('Number of Reported Deaths', fontsize=20);
plt.title('Total reported coronavirus deaths for places with at least 25 deaths', fontsize=20);

# Plot time series 
ax = deaths_df_drop.plot(figsize=(20,10), linewidth=2, marker=".", fontsize=20, logy=True)
ax.legend(ncol=3, loc='upper right')
plt.xlabel('Days', fontsize=20);
plt.ylabel('Number of Reported Deaths', fontsize=20);
plt.title('Total reported coronavirus deaths for places with at least 25 deaths', fontsize=20);

"""**Note:** although the plot is what we wanted, the above plots are challenging to retrieve any meaningful information from. 
There are too many growth curves so that it's very crowded **and** too many colours look the same so it's difficult to tell which country is which from the legend. 
So, I'll plot less curves now and further down in the notebook I'll use the python package Altair to introduce interactivity.
"""

# Plot semi log time series 
ax = deaths_df_drop[countries].plot(figsize=(20,10), linewidth=2, marker='.', fontsize=20, logy=True)
ax.legend(ncol=3, loc='upper right')
plt.xlabel('Days', fontsize=20);
plt.ylabel('Deaths Patients count', fontsize=20);
plt.title('Total reported coronavirus deaths for places with at least 25 deaths', fontsize=20);

"""Till Now, We  
- looked at the dataset containing the number of reported deaths for each region,
- wrangled the data to look at the number of reported deaths by country,
- plotted the number of reported deaths by country on linear and log scale.
- aligned growth curves to start with day of number of known deaths ≥ 25.

### Plotting number of recovered people

The third dataset in the Hopkins repository is the number of recovered. We want to do similar data wrangling as in the two cases above so we *could* copy and paste our code again *but*, if you're writing the same code three times, it's likely time to write a function.
"""

# Function for grouping countries by region
def group_by_country(raw_data):
    
    # Group by
    data = raw_data.groupby(['Country/Region']).sum().drop(['Lat', 'Long'], axis=1)
    # Transpose
    data = data.transpose()
    # Set index as DateTimeIndex
    datetime_index = pd.DatetimeIndex(data.index)
    data.set_index(datetime_index, inplace=True)
    return data

# Function to align growth curves
def align_curves(data, min_val):
    
    # Loop over columns & set values < min_val to None
    for col in data.columns:
        data.loc[(data[col] < min_val), col] = None
    # Drop columns with all NaNs
    data.dropna(axis=1, how="all", inplace=True)
    # Reset index, drop date
    data = data.reset_index().drop(['index'], axis=1)
    # Shift each column to begin with first valid index
    for col in data.columns:
        data[col] = data[col].shift(-data[col].first_valid_index())
    return data

# Function to plot time series
def plot_time_series(df, plot_title, x_label, y_label, logy=False):
    
    ax = df.plot(figsize=(20,10), linewidth=2, marker='.', fontsize=20, logy=logy)
    ax.legend(ncol=3, loc='lower right')
    plt.xlabel(x_label, fontsize=20);
    plt.ylabel(y_label, fontsize=20);
    plt.title(plot_title, fontsize=20);

"""Trying these functions at work on the 'number of deaths' data:"""

deaths_country_drop = (group_by_country(raw_deaths_df))
deaths_country_drop = align_curves(deaths_country_drop, min_val=25)
plot_time_series(deaths_country_drop, 'Number of Reported Deaths', 'Days', 'Reported Deaths by Country', logy=True)

"""Now let's check use our functions to group, wrangle, and plot the recovered patients data:"""

# group by country and check out tail
recovered_df = group_by_country(raw_recovered_df)
recovered_df.tail()

# align curves and check out head
recovered_df_drop = align_curves(recovered_df, min_val=25)
recovered_df_drop.head()

"""Plot time series:"""

plot_time_series(recovered_df_drop, 'Recovered Patients Plot', 'Days', 'Recovered Patients Count')

plot_time_series(recovered_df_drop, 'Recovered Patients Plot', 'Days', 'Recovered Patients Count', True)

"""### Since this plot gets messed up because of the number of countries, I will again go with the selective ones."""

plot_time_series(recovered_df_drop[countries], 'Recovered Patients Time Series', 'Days', 'Recovered Patients count', True)

"""Now, I looked at the dataset containing the number of reported recoveries for each region, written function for grouping, wrangling, and plotting the data along with using these functions.

## Interactive plots with altair

Now for some interactive data visualizations, I will be using Altair which can produce visualizations similar to [this one in the NYTimes](https://www.nytimes.com/interactive/2020/03/21/upshot/coronavirus-deaths-by-country.html), a chart of confirmed number of deaths by country for places with at least 25 deaths, similar to the one above, but with informative hover tools. 
[This one](https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html) is also really good.

Before going to Altair, I will reshape our `deaths_df` dataset. Notice that it's currently in **wide data format**, with a column for each country and a row for each "day" (where day 1 is the first day with over 25 confirmed deaths).
"""

# Look at head
deaths_df_drop.head()

"""For Altair, we'll want to convert the data into **long data format**. What this will do essentially have a row for each country/day pair so our columns will be 'Day', 'Country', and number of 'Deaths'. We do this using the dataframe method `.melt()` as follows:"""

# create long data for deaths
deaths_long = deaths_df_drop.reset_index().melt(id_vars='index', value_name='Deaths').rename(columns={'index':'Day'}) 
deaths_long.head()

deaths_long.info()

"""We'll see the power of having long data when using Altair.
Now having transformed our data, let's import Altair and get a sense of its API.
"""

import altair as alt

alt.data_transformers.disable_max_rows() 
#This particular line of code is to be used when we have more than 5000 rows in our dataset and is vailable in Altair Documentation.
#This limit has just been set to prevent our notebook from growing excessive in size.

# altair plotting
alt.Chart(deaths_long).mark_line().encode(
    x='Day',
    y='Deaths',
    color='Country/Region')

"""So, we have successfully made the plot.

The [Altair documentation states](https://altair-viz.github.io/getting_started/overview.html),

> The key idea is that you are declaring links between *data columns* and *visual encoding channels*, such as the x-axis, y-axis, color, etc. The rest of the plot details are handled automatically. Building on this declarative plotting idea, a surprising range of simple to sophisticated plots and visualizations can be created using a relatively concise grammar.

I can now customize the code to thicken the line width, to alter the opacity, and to make the chart larger:
"""

# altair plot 
alt.Chart(deaths_long).mark_line(strokeWidth=4, opacity=0.7).encode(
    x='Day',
    y='Deaths',
    color='Country/Region'
).properties(
    width=800, height=650
)

"""We can also add a log y-axis. To do this, The long-form, we express the types using the long-form `alt.X('Day',...)`, which is, in the words of the [Altair documentation](https://altair-viz.github.io/user_guide/encoding.html)
> useful when doing more fine-tuned adjustments to the encoding, such as binning, axis and scale properties, or more.

We'll also now add a hover tooltip so that, when we hover our cursor over any point on any of the lines, it will tell us the 'Country', the 'Day', and the number of 'Deaths'.
"""

# altair plot 
alt.Chart(deaths_long).mark_line(strokeWidth=4, opacity=0.7).encode(
    x=alt.X('Day'),
    y=alt.Y('Deaths', scale=alt.Scale(type='log')),
    color='Country/Region',
    tooltip=['Country/Region', 'Day','Deaths']
).properties(
    width=800,
    height=650
)

"""It's great that we could add that useful hover tooltip with one line of code `tooltip=['Country/Region', 'Day','Deaths']`, particularly as it adds such information rich interaction to the chart.
One useful aspect of the NYTimes chart was that, when you hovered over a particular curve, it made it stand out against the other. We're going to do something similar here: in the resulting chart, when you click on a curve, the others turn grey.

**Note:** When first attempting to build this chart, I discovered [here](https://github.com/altair-viz/altair/issues/1552) that "multiple conditional values in one encoding are not allowed by the Vega-Lite spec," which is what Altair uses. For this reason, we build the chart, then an overlay, and then combine them.
"""

# Selection tool
selection = alt.selection_single(fields=['Country/Region'])
# Color change when clicked
color = alt.condition(selection,
                    alt.Color('Country/Region:N'),
                    alt.value('lightgray'))


# Base altair plot 
base = alt.Chart(deaths_long).mark_line(strokeWidth=4, opacity=0.7).encode(
    x=alt.X('Day'),
    y=alt.Y('Deaths', scale=alt.Scale(type='log')),
    color='Country/Region',
    tooltip=['Country/Region', 'Day','Deaths']
).properties(
    width=800,
    height=650
)

# Chart
chart = base.encode(
  color=alt.condition(selection, 'Country/Region:N', alt.value('lightgray'))
).add_selection(
  selection
)

# Overlay
overlay = base.encode(
    color='Country/Region',
  opacity=alt.value(0.5),
  tooltip=['Country/Region:N', 'Name:N']
).transform_filter(
  selection
)

# Sum em up!
chart + overlay

"""It's not super easy to line up the legend with the curves on the chart so let's put the labels on the chart itself."""

# drop NaNs
deaths_long = deaths_long.dropna()

# Selection tool
selection = alt.selection_single(fields=['Country/Region'])
# Color change when clicked
color = alt.condition(selection,
                    alt.Color('Country/Region:N'),
                    alt.value('lightgray'))


# Base altair plot 
base = alt.Chart(deaths_long).mark_line(strokeWidth=4, opacity=0.7).encode(
    x=alt.X('Day'),
    y=alt.Y('Deaths', scale=alt.Scale(type='log')),
    color=alt.Color('Country/Region', legend=None),
).properties(
    width=800,
    height=650
)

# Chart
chart = base.encode(
  color=alt.condition(selection, 'Country/Region:N', alt.value('lightgray'))
).add_selection(
  selection
)

# Overlay
overlay = base.encode(
  color='Country/Region',
  opacity=alt.value(0.5),
  tooltip=['Country/Region:N', 'Name:N']
).transform_filter(
  selection
)

# Text labels
text = base.mark_text(
    align='left',
    dx=5,
    size=10
).encode(
    x=alt.X('Day', aggregate='max',  axis=alt.Axis(title='Day')),
    y=alt.Y('Deaths', aggregate={'argmax': 'Day'}, axis=alt.Axis(title='Reported Deaths')),
    text='Country/Region',  
).transform_filter(
    selection
)

# Sum em up!
chart + overlay + text

"""**Summary:** So, now we have 
- melted the data into long format,
- used Altair to make interactive plots of increasing richness,

Thank You!
You can check out [my github](https://www.github.com/hritikbhandari) for more interesting EDAs and projects.
"""