<h1>Analysis of input data and constraints of columns</h1>
<h2>Jakub Jachowicz </h2>

As said in course's walk-through, I used the dataset from previous lab. It contains data about hotels in New York. I have slightly changed the layout of my "to-be-database", and splitted data into 4 instead of 2 tables.

First, I imported a dataset from csv file.


```python
import pandas as pd

data = pd.read_csv(r'C:\Studia\S8\DA & ADb\Advanced Databases\LAB3\AB_NYC_2019.csv')

data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>host_id</th>
      <th>host_name</th>
      <th>neighbourhood_group</th>
      <th>neighbourhood</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>room_type</th>
      <th>price</th>
      <th>minimum_nights</th>
      <th>number_of_reviews</th>
      <th>last_review</th>
      <th>reviews_per_month</th>
      <th>calculated_host_listings_count</th>
      <th>availability_365</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>2539</td>
      <td>Clean &amp; quiet apt home by the park</td>
      <td>2787</td>
      <td>John</td>
      <td>Brooklyn</td>
      <td>Kensington</td>
      <td>40.64749</td>
      <td>-73.97237</td>
      <td>Private room</td>
      <td>149</td>
      <td>1</td>
      <td>9</td>
      <td>2018-10-19</td>
      <td>0.21</td>
      <td>6</td>
      <td>365</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2595</td>
      <td>Skylit Midtown Castle</td>
      <td>2845</td>
      <td>Jennifer</td>
      <td>Manhattan</td>
      <td>Midtown</td>
      <td>40.75362</td>
      <td>-73.98377</td>
      <td>Entire home/apt</td>
      <td>225</td>
      <td>1</td>
      <td>45</td>
      <td>2019-05-21</td>
      <td>0.38</td>
      <td>2</td>
      <td>355</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3647</td>
      <td>THE VILLAGE OF HARLEM....NEW YORK !</td>
      <td>4632</td>
      <td>Elisabeth</td>
      <td>Manhattan</td>
      <td>Harlem</td>
      <td>40.80902</td>
      <td>-73.94190</td>
      <td>Private room</td>
      <td>150</td>
      <td>3</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>365</td>
    </tr>
    <tr>
      <td>3</td>
      <td>3831</td>
      <td>Cozy Entire Floor of Brownstone</td>
      <td>4869</td>
      <td>LisaRoxanne</td>
      <td>Brooklyn</td>
      <td>Clinton Hill</td>
      <td>40.68514</td>
      <td>-73.95976</td>
      <td>Entire home/apt</td>
      <td>89</td>
      <td>1</td>
      <td>270</td>
      <td>2019-07-05</td>
      <td>4.64</td>
      <td>1</td>
      <td>194</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5022</td>
      <td>Entire Apt: Spacious Studio/Loft by central park</td>
      <td>7192</td>
      <td>Laura</td>
      <td>Manhattan</td>
      <td>East Harlem</td>
      <td>40.79851</td>
      <td>-73.94399</td>
      <td>Entire home/apt</td>
      <td>80</td>
      <td>10</td>
      <td>9</td>
      <td>2018-11-19</td>
      <td>0.10</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



Then I have checked the dataset columns:


```python
print(data.columns)
```

    Index(['id', 'name', 'host_id', 'host_name', 'neighbourhood_group',
           'neighbourhood', 'latitude', 'longitude', 'room_type', 'price',
           'minimum_nights', 'number_of_reviews', 'last_review',
           'reviews_per_month', 'calculated_host_listings_count',
           'availability_365'],
          dtype='object')
    


```python
data.name.describe()
```




    count              48879
    unique             47905
    top       Hillside Hotel
    freq                  18
    Name: name, dtype: object




```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 48895 entries, 0 to 48894
    Data columns (total 16 columns):
    id                                48895 non-null int64
    name                              48879 non-null object
    host_id                           48895 non-null int64
    host_name                         48874 non-null object
    neighbourhood_group               48895 non-null object
    neighbourhood                     48895 non-null object
    latitude                          48895 non-null float64
    longitude                         48895 non-null float64
    room_type                         48895 non-null object
    price                             48895 non-null int64
    minimum_nights                    48895 non-null int64
    number_of_reviews                 48895 non-null int64
    last_review                       38843 non-null object
    reviews_per_month                 38843 non-null float64
    calculated_host_listings_count    48895 non-null int64
    availability_365                  48895 non-null int64
    dtypes: float64(3), int64(7), object(6)
    memory usage: 6.0+ MB
    

After checking the info about dataset, I've decided to split data into 4 tables:
 * neighbourhoods (id - neighbourhood name - neighbourhood group id);
 * neighbourhood groups (id - group name);
 * hosts (id - host_name);
 * hotels (rest of the data with specified neighbourhood id and host id);


```python
all_neighbourhoods = data['neighbourhood'].unique()
print("Neighbourhood array: {0}".format(sorted(all_neighbourhoods)))

all_neighbourhood_groups = data['neighbourhood_group'].unique()
print("Neighbourhood groups array: {0}".format(all_neighbourhood_groups))

all_ids = data['id'].unique()
all_host_ids = data['host_id'].unique()
```

    Neighbourhood array: ['Allerton', 'Arden Heights', 'Arrochar', 'Arverne', 'Astoria', 'Bath Beach', 'Battery Park City', 'Bay Ridge', 'Bay Terrace', 'Bay Terrace, Staten Island', 'Baychester', 'Bayside', 'Bayswater', 'Bedford-Stuyvesant', 'Belle Harbor', 'Bellerose', 'Belmont', 'Bensonhurst', 'Bergen Beach', 'Boerum Hill', 'Borough Park', 'Breezy Point', 'Briarwood', 'Brighton Beach', 'Bronxdale', 'Brooklyn Heights', 'Brownsville', "Bull's Head", 'Bushwick', 'Cambria Heights', 'Canarsie', 'Carroll Gardens', 'Castle Hill', 'Castleton Corners', 'Chelsea', 'Chinatown', 'City Island', 'Civic Center', 'Claremont Village', 'Clason Point', 'Clifton', 'Clinton Hill', 'Co-op City', 'Cobble Hill', 'College Point', 'Columbia St', 'Concord', 'Concourse', 'Concourse Village', 'Coney Island', 'Corona', 'Crown Heights', 'Cypress Hills', 'DUMBO', 'Ditmars Steinway', 'Dongan Hills', 'Douglaston', 'Downtown Brooklyn', 'Dyker Heights', 'East Elmhurst', 'East Flatbush', 'East Harlem', 'East Morrisania', 'East New York', 'East Village', 'Eastchester', 'Edenwald', 'Edgemere', 'Elmhurst', 'Eltingville', 'Emerson Hill', 'Far Rockaway', 'Fieldston', 'Financial District', 'Flatbush', 'Flatiron District', 'Flatlands', 'Flushing', 'Fordham', 'Forest Hills', 'Fort Greene', 'Fort Hamilton', 'Fort Wadsworth', 'Fresh Meadows', 'Glendale', 'Gowanus', 'Gramercy', 'Graniteville', 'Grant City', 'Gravesend', 'Great Kills', 'Greenpoint', 'Greenwich Village', 'Grymes Hill', 'Harlem', "Hell's Kitchen", 'Highbridge', 'Hollis', 'Holliswood', 'Howard Beach', 'Howland Hook', 'Huguenot', 'Hunts Point', 'Inwood', 'Jackson Heights', 'Jamaica', 'Jamaica Estates', 'Jamaica Hills', 'Kensington', 'Kew Gardens', 'Kew Gardens Hills', 'Kingsbridge', 'Kips Bay', 'Laurelton', 'Lighthouse Hill', 'Little Italy', 'Little Neck', 'Long Island City', 'Longwood', 'Lower East Side', 'Manhattan Beach', 'Marble Hill', 'Mariners Harbor', 'Maspeth', 'Melrose', 'Middle Village', 'Midland Beach', 'Midtown', 'Midwood', 'Mill Basin', 'Morningside Heights', 'Morris Heights', 'Morris Park', 'Morrisania', 'Mott Haven', 'Mount Eden', 'Mount Hope', 'Murray Hill', 'Navy Yard', 'Neponsit', 'New Brighton', 'New Dorp', 'New Dorp Beach', 'New Springville', 'NoHo', 'Nolita', 'North Riverdale', 'Norwood', 'Oakwood', 'Olinville', 'Ozone Park', 'Park Slope', 'Parkchester', 'Pelham Bay', 'Pelham Gardens', 'Port Morris', 'Port Richmond', "Prince's Bay", 'Prospect Heights', 'Prospect-Lefferts Gardens', 'Queens Village', 'Randall Manor', 'Red Hook', 'Rego Park', 'Richmond Hill', 'Richmondtown', 'Ridgewood', 'Riverdale', 'Rockaway Beach', 'Roosevelt Island', 'Rosebank', 'Rosedale', 'Rossville', 'Schuylerville', 'Sea Gate', 'Sheepshead Bay', 'Shore Acres', 'Silver Lake', 'SoHo', 'Soundview', 'South Beach', 'South Ozone Park', 'South Slope', 'Springfield Gardens', 'Spuyten Duyvil', 'St. Albans', 'St. George', 'Stapleton', 'Stuyvesant Town', 'Sunnyside', 'Sunset Park', 'Theater District', 'Throgs Neck', 'Todt Hill', 'Tompkinsville', 'Tottenville', 'Tremont', 'Tribeca', 'Two Bridges', 'Unionport', 'University Heights', 'Upper East Side', 'Upper West Side', 'Van Nest', 'Vinegar Hill', 'Wakefield', 'Washington Heights', 'West Brighton', 'West Farms', 'West Village', 'Westchester Square', 'Westerleigh', 'Whitestone', 'Williamsbridge', 'Williamsburg', 'Willowbrook', 'Windsor Terrace', 'Woodhaven', 'Woodlawn', 'Woodrow', 'Woodside']
    Neighbourhood groups array: ['Brooklyn' 'Manhattan' 'Queens' 'Staten Island' 'Bronx']
    

After checking the unique values in the column neighbourhood, I've noticed one mistake, which I've corrected in the cell below using mapping:


```python
dictionary_correct = {'Bay Terrace, Staten Island':'Bay Terrace'}
mapping_neighbourhood = data['neighbourhood'].map(dictionary_correct)
```

Sprawdziłem ewentualne puste kolumny w datasecie i w miarę możliwości, uzupełniłem na podstawie danych z powiązanych wersów. 


```python
for ID in all_ids:
    name = data[(data['id']==ID) & (~data['name'].isna())]['name'].unique()
    try:
        data.loc[(data['id']==ID) & (data['name'].isna()), 'name'] = name
    except:
        print('Something went wrong:', ID, name)
```

    Something went wrong: 1615764 []
    Something went wrong: 2232600 []
    Something went wrong: 4209595 []
    Something went wrong: 4370230 []
    Something went wrong: 4581788 []
    Something went wrong: 4756856 []
    Something went wrong: 4774658 []
    Something went wrong: 6782407 []
    Something went wrong: 9325951 []
    Something went wrong: 9787590 []
    Something went wrong: 9885866 []
    Something went wrong: 10052289 []
    Something went wrong: 12797684 []
    Something went wrong: 12988898 []
    Something went wrong: 14135050 []
    Something went wrong: 22275821 []
    


```python
for host_id in all_host_ids:
    host_name = data[(data['host_id']==host_id) & (~data['host_name'].isna())]['host_name'].unique()
    try:
        data.loc[(data['host_id']==host_id) & (data['host_name'].isna()), 'host_name'] = host_name
    except:
        print('Something went wrong:', host_id, host_name)
```

    Something went wrong: 526653 []
    Something went wrong: 7779204 []
    Something went wrong: 919218 []
    Something went wrong: 23077718 []
    Something went wrong: 24576978 []
    Something went wrong: 32722063 []
    Something went wrong: 33134899 []
    Something went wrong: 5162530 []
    Something went wrong: 39608626 []
    Something went wrong: 7822683 []
    Something went wrong: 26138712 []
    Something went wrong: 5300585 []
    Something went wrong: 100971588 []
    Something went wrong: 415290 []
    Something went wrong: 159156636 []
    Something went wrong: 177146433 []
    Something went wrong: 119609345 []
    Something went wrong: 228750026 []
    


```python
for neigh in all_neighbourhoods:
    neighbourhood_group = data[(data['neighbourhood']==neigh) & (~data['neighbourhood_group'].isna())]['neighbourhood_group'].unique()
    try:
        data.loc[(data['neighbourhood']==neigh) & (data['neighbourhood_group'].isna()), 'neighbourhood_group'] = neighbourhood_group
    except:
        print('Something went wrong:', neigh, neighbourhood_group)
```

In "something went wrong" cases, there wasn't enough information in related cells of dataframe to fill empty ones.

I've formed four DataFrames and took out only unique values in the most important column of each dataset. If needed, I've also renamed the columns of reseted index.


```python
neighbourhood_group_list = pd.DataFrame(data['neighbourhood_group'].unique(), columns=['neighbourhood_group'])

neighbourhood_group_list.index.name = 'id'
neighbourhood_group_list = neighbourhood_group_list.rename(columns = {'neighbourhood_group':'group_name'})

neighbourhood_group_list
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>group_name</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Brooklyn</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Manhattan</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Queens</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Staten Island</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Bronx</td>
    </tr>
  </tbody>
</table>
</div>




```python
neighbourhood_list = data[['neighbourhood','neighbourhood_group']].drop_duplicates().reset_index().drop(columns = ['index']);

neighbourhood_list.index.name = 'id'

neighbourhood_list = neighbourhood_list.rename(columns = {'neighbourhood_group':'group'})

neighbourhood_list.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>neighbourhood</th>
      <th>group</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Kensington</td>
      <td>Brooklyn</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Midtown</td>
      <td>Manhattan</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Harlem</td>
      <td>Manhattan</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Clinton Hill</td>
      <td>Brooklyn</td>
    </tr>
    <tr>
      <td>4</td>
      <td>East Harlem</td>
      <td>Manhattan</td>
    </tr>
  </tbody>
</table>
</div>




```python
neighbourhood_list['group'] = neighbourhood_list['group'].map(lambda x: neighbourhood_group_list[neighbourhood_group_list['group_name'] == x].index.values.astype(int)[0])

neighbourhood_list.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>neighbourhood</th>
      <th>group</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Kensington</td>
      <td>0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Midtown</td>
      <td>1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Harlem</td>
      <td>1</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Clinton Hill</td>
      <td>0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>East Harlem</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
host_list = data[['host_id','host_name']].drop_duplicates().reset_index().drop(columns = ['index'])
host_list.index.name = 'id'

host_list.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>host_id</th>
      <th>host_name</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>2787</td>
      <td>John</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2845</td>
      <td>Jennifer</td>
    </tr>
    <tr>
      <td>2</td>
      <td>4632</td>
      <td>Elisabeth</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4869</td>
      <td>LisaRoxanne</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7192</td>
      <td>Laura</td>
    </tr>
  </tbody>
</table>
</div>




```python
hotel_list = data[['id','name', 'host_id', 'neighbourhood', 'latitude', 'longitude','room_type','price','minimum_nights','number_of_reviews','last_review','reviews_per_month','calculated_host_listings_count']].drop_duplicates().reset_index().drop(columns = ['index'])
hotel_list.index.name = 'id'

hotel_list = hotel_list.rename(columns = {'id':'hotel_id'})

hotel_list['neighbourhood'] = hotel_list['neighbourhood'].map(lambda x:  neighbourhood_list[neighbourhood_list['neighbourhood'] == x].index.values.astype(int)[0])
hotel_list['reviews_per_month'].fillna(0, inplace = True)
hotel_list['last_review'].fillna('0000-00-00', inplace = True)

hotel_list.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>hotel_id</th>
      <th>name</th>
      <th>host_id</th>
      <th>neighbourhood</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>room_type</th>
      <th>price</th>
      <th>minimum_nights</th>
      <th>number_of_reviews</th>
      <th>last_review</th>
      <th>reviews_per_month</th>
      <th>calculated_host_listings_count</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>2539</td>
      <td>Clean &amp; quiet apt home by the park</td>
      <td>2787</td>
      <td>0</td>
      <td>40.64749</td>
      <td>-73.97237</td>
      <td>Private room</td>
      <td>149</td>
      <td>1</td>
      <td>9</td>
      <td>2018-10-19</td>
      <td>0.21</td>
      <td>6</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2595</td>
      <td>Skylit Midtown Castle</td>
      <td>2845</td>
      <td>1</td>
      <td>40.75362</td>
      <td>-73.98377</td>
      <td>Entire home/apt</td>
      <td>225</td>
      <td>1</td>
      <td>45</td>
      <td>2019-05-21</td>
      <td>0.38</td>
      <td>2</td>
    </tr>
    <tr>
      <td>2</td>
      <td>3647</td>
      <td>THE VILLAGE OF HARLEM....NEW YORK !</td>
      <td>4632</td>
      <td>2</td>
      <td>40.80902</td>
      <td>-73.94190</td>
      <td>Private room</td>
      <td>150</td>
      <td>3</td>
      <td>0</td>
      <td>0000-00-00</td>
      <td>0.00</td>
      <td>1</td>
    </tr>
    <tr>
      <td>3</td>
      <td>3831</td>
      <td>Cozy Entire Floor of Brownstone</td>
      <td>4869</td>
      <td>3</td>
      <td>40.68514</td>
      <td>-73.95976</td>
      <td>Entire home/apt</td>
      <td>89</td>
      <td>1</td>
      <td>270</td>
      <td>2019-07-05</td>
      <td>4.64</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4</td>
      <td>5022</td>
      <td>Entire Apt: Spacious Studio/Loft by central park</td>
      <td>7192</td>
      <td>4</td>
      <td>40.79851</td>
      <td>-73.94399</td>
      <td>Entire home/apt</td>
      <td>80</td>
      <td>10</td>
      <td>9</td>
      <td>2018-11-19</td>
      <td>0.10</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



I've imported sqlalchemy and all necessary variables to connect with my local database and to upload new data.


```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, UniqueConstraint


db_string = "postgres://postgres:jakub_adb@localhost:5432/nyhotels"

engine = create_engine(db_string)

Base = declarative_base()

```

Below, I've created four classes, each one for one DataFrame, and used metadata to assign data from df to these new classes.


```python
class Hotel(Base):
    __tablename__ = 'hotels'
    __table_args__ = (
        UniqueConstraint('hotel_id'),
    )
    hotel_id = Column(Integer, primary_key = True)
    name = Column(String(2000), nullable = False)
    host_id = Column(Integer, nullable = False)
    neighbourhood = Column(Integer, nullable = False)
    latitude = Column(Float)
    longitude = Column(Float)
    room_type = Column(String(200))
    price = Column(Integer)
    minimum_nights = Column(Integer)
    number_of_reviews = Column(Integer)
    last_review = Column(String(20))
    reviews_per_month = Column(Integer)
    calculated_host_listing_count = Column(Integer)


class Host(Base):
    __tablename__ = 'hosts'
    __table_args__ = (
        UniqueConstraint('host_id'),
    )
    host_id = Column(Integer, primary_key = True)
    host_name = Column(String(200))
    
class Neighbourhood(Base):
    __tablename__ = 'neighbourhoods'
    __table_args__ = (
        UniqueConstraint('id'),
    )
    id = Column(Integer, primary_key = True)
    neighbourhood = Column(String(200))
    nieghbourhood_group_id = Column(Integer)

class NeighbourhoodGroup(Base):
    __tablename__ = 'neighbourhood_groups'
    __talbe_args__ = (
        UniqueConstraint('id'),
    )
    group_id = Column(Integer, primary_key = True)
    group_name = Column(String(50))
    
Base.metadata.create_all(engine)
```


```python
hotel_list.to_sql('hotels', engine, if_exists='append')
host_list.to_sql('hosts', engine, if_exists='append')
neighbourhood_list.to_sql('neighbourhoods', engine, if_exists='append')
neighbourhood_group_list.to_sql('neighbourhood_groups', engine, if_exists='append')
```

I've checked in pqsl, if the results came through. All four tables were succesfully updated/added.
