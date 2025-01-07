
# Data Product Canvas - Berlin Election Results

## Metadata

* owner: Open Lifeworlds
* description: Data product combining Berlin election results and geodata
* url: https://github.com/open-lifeworlds/-open-lifeworlds-data-product-berlin-election-results
* license: CC-BY 4.0
* updated: 2025-05-15

## Input Ports

### Berlin LOR geodata

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/tree/main/data
* license: CC-BY-4.0
* updated: 2023-07-22

**Files**

* [berlin-lor-city.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-city/berlin-lor-city.geojson)
* [berlin-lor-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-districts/berlin-lor-districts.geojson)
* [berlin-lor-forecast-areas-until-2020.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-forecast-areas-until-2020/berlin-lor-forecast-areas-until-2020.geojson)
* [berlin-lor-forecast-areas-from-2021.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-forecast-areas-from-2021/berlin-lor-forecast-areas-from-2021.geojson)
* [berlin-lor-district-regions-until-2020.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-district-regions-until-2020/berlin-lor-district-regions-until-2020.geojson)
* [berlin-lor-district-regions-from-2021.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-district-regions-from-2021/berlin-lor-district-regions-from-2021.geojson)
* [berlin-lor-planning-areas-until-2020.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-planning-areas-until-2020/berlin-lor-planning-areas-until-2020.geojson)
* [berlin-lor-planning-areas-from-2021.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-planning-areas-from-2021/berlin-lor-planning-areas-from-2021.geojson)

### Berlin Electoral Districts Berlin Election 2016

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/tree/main/data/02-silver/berlin-electoral-districts-berlin-election-2016
* license: CC-BY 4.0
* updated: 2024-12-04

**Schema**

| Name | Description |
| --- | --- |
| electoral_district_id | ID of the electoral district (5 digits) |
| postal_voting_district_id | ID of the postal voting district (3 digits + 1 letter) |
| electoral_district_berlin_election_id | ID of the electoral district for the election of House of Representatives (4 digits) |

**Files**

* [berlin-electoral-districts-berlin-election-2016.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/main/data/02-silver/berlin-electoral-districts-berlin-election-2016/berlin-electoral-districts-berlin-election-2016.geojson)

### Berlin Electoral Districts Berlin Election 2021

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/tree/main/data/02-silver/berlin-electoral-districts-berlin-election-2021
* license: CC-BY 4.0
* updated: 2024-12-04

**Schema**

| Name | Description |
| --- | --- |
| electoral_district_id | ID of the electoral district (5 digits) |
| electoral_district_id_3 | ID of the polling district (3 digits), unique for each district |
| postal_voting_district_id | ID of the postal voting district (3 digits + 1 letter), first 2 digits represent the district |
| postal_voting_district_id_2 | ID of the postal voting district (1 digit + 1 letter) |
| electoral_district_berlin_election_id | ID of the electoral district for the election of House of Representatives (4 digits) |
| electoral_district_federal_election_id | ID of the electoral district for the federal election (3 digits) |

**Files**

* [berlin-electoral-districts-berlin-election-2021.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/main/data/02-silver/berlin-electoral-districts-berlin-election-2021/berlin-electoral-districts-berlin-election-2021.geojson)

### Berlin Electoral Districts European Election 2014

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/tree/main/data/02-silver/berlin-electoral-districts-european-election-2014
* license: CC-BY 4.0
* updated: 2024-12-04

**Schema**

| Name | Description |
| --- | --- |
| electoral_district_id | ID of the electoral district (5 digits) |
| constituency_id | ID of the constituency for Berlin election (4 digits) |
| postal_voting_district_id | ID of the postal voting district (3 digits + 1 letter), first 2 digits represent the district |

**Files**

* [berlin-electoral-districts-european-election-2014.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/main/data/02-silver/berlin-electoral-districts-european-election-2014/berlin-electoral-districts-european-election-2014.geojson)

### Berlin Electoral Districts European Election 2019

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/tree/main/data/02-silver/berlin-electoral-districts-european-election-2019
* license: CC-BY 4.0
* updated: 2024-12-04

**Schema**

| Name | Description |
| --- | --- |
| electoral_district_id | ID of the electoral district (5 digits) |
| electoral_district_id_3 | ID of the polling district (3 digits), unique for each district |
| postal_voting_district_id | ID of the postal voting district (3 digits + 1 letter), first 2 digits represent the district |
| postal_voting_district_id_2 | ID of the postal voting district (1 digit + 1 letter) |
| electoral_district_berlin_election_id | ID of the electoral district for the election of House of Representatives (4 digits) |
| electoral_district_federal_election_id | ID of the electoral district for the federal election (3 digits) |

**Files**

* [berlin-electoral-districts-european-election-2019.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/main/data/02-silver/berlin-electoral-districts-european-election-2019/berlin-electoral-districts-european-election-2019.geojson)

### Berlin Electoral Districts European Election 2024

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/tree/main/data/02-silver/berlin-electoral-districts-european-election-2024
* license: CC-BY 4.0
* updated: 2024-12-04

**Schema**

| Name | Description |
| --- | --- |
| electoral_district_id | ID of the electoral district (5 digits) |
| electoral_district_id_3 | ID of the polling district (3 digits), unique for each district |
| postal_voting_district_id | ID of the postal voting district (3 digits + 1 letter), first 2 digits represent the district |
| postal_voting_district_id_2 | ID of the postal voting district (1 digit + 1 letter) |
| electoral_district_berlin_election_id | ID of the electoral district for the election of House of Representatives (4 digits) |
| electoral_district_federal_election_id | ID of the electoral district for the federal election (3 digits) |

**Files**

* [berlin-electoral-districts-european-election-2024.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/main/data/02-silver/berlin-electoral-districts-european-election-2024/berlin-electoral-districts-european-election-2024.geojson)

### Berlin Electoral Districts Federal Election 2017

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/tree/main/data/02-silver/berlin-electoral-districts-federal-election-2017
* license: CC-BY 4.0
* updated: 2024-12-04

**Schema**

| Name | Description |
| --- | --- |
| electoral_district_id | ID of the electoral district (5 digits) |
| electoral_district_id_3 | ID of the polling district (3 digits), unique for each district |
| postal_voting_district_id | ID of the postal voting district (3 digits + 1 letter), first 2 digits represent the district |
| postal_voting_district_id_2 | ID of the postal voting district (1 digit + 1 letter) |
| electoral_district_berlin_election_id | ID of the electoral district for the election of House of Representatives (4 digits) |
| electoral_district_federal_election_id | ID of the electoral district for the federal election (3 digits) |

**Files**

* [berlin-electoral-districts-federal-election-2017.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/main/data/02-silver/berlin-electoral-districts-federal-election-2017/berlin-electoral-districts-federal-election-2017.geojson)

### Berlin Electoral Districts Federal Election 2021

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/tree/main/data/02-silver/berlin-electoral-districts-federal-election-2021
* license: CC-BY 4.0
* updated: 2024-12-04

**Schema**

| Name | Description |
| --- | --- |
| electoral_district_id | ID of the electoral district (5 digits) |
| electoral_district_id_3 | ID of the polling district (3 digits), unique for each district |
| postal_voting_district_id | ID of the postal voting district (3 digits + 1 letter), first 2 digits represent the district |
| postal_voting_district_id_2 | ID of the postal voting district (1 digit + 1 letter) |
| electoral_district_berlin_election_id | ID of the electoral district for the election of House of Representatives (4 digits) |
| electoral_district_federal_election_id | ID of the electoral district for the federal election (3 digits) |

**Files**

* [berlin-electoral-districts-federal-election-2021.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-electoral-districts-geodata/main/data/02-silver/berlin-electoral-districts-federal-election-2021/berlin-electoral-districts-federal-election-2021.geojson)

### Berlin Election Results Berlin Election 2016

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/tree/main/data/03-gold/berlin-election-results-berlin-election-2016
* license: GPLv3
* updated: 2025-05-13

**Files**

* [berlin-election-results-berlin-election-2016-electoral-results-district-council-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2016/berlin-election-results-berlin-election-2016-electoral-results-district-council-city.csv)
* [berlin-election-results-berlin-election-2016-electoral-results-district-council-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2016/berlin-election-results-berlin-election-2016-electoral-results-district-council-districts.csv)
* [berlin-election-results-berlin-election-2016-electoral-results-district-council-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2016/berlin-election-results-berlin-election-2016-electoral-results-district-council-electoral-districts.csv)
* [berlin-election-results-berlin-election-2016-electoral-results-first-vote-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2016/berlin-election-results-berlin-election-2016-electoral-results-first-vote-city.csv)
* [berlin-election-results-berlin-election-2016-electoral-results-first-vote-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2016/berlin-election-results-berlin-election-2016-electoral-results-first-vote-districts.csv)
* [berlin-election-results-berlin-election-2016-electoral-results-first-vote-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2016/berlin-election-results-berlin-election-2016-electoral-results-first-vote-electoral-districts.csv)
* [berlin-election-results-berlin-election-2016-electoral-results-second-vote-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2016/berlin-election-results-berlin-election-2016-electoral-results-second-vote-city.csv)
* [berlin-election-results-berlin-election-2016-electoral-results-second-vote-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2016/berlin-election-results-berlin-election-2016-electoral-results-second-vote-districts.csv)
* [berlin-election-results-berlin-election-2016-electoral-results-second-vote-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2016/berlin-election-results-berlin-election-2016-electoral-results-second-vote-electoral-districts.csv)

### Berlin Election Results Berlin Election 2023

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/tree/main/data/03-gold/berlin-election-results-berlin-election-2023
* license: GPLv3
* updated: 2025-05-13

**Files**

* [berlin-election-results-berlin-election-2023-electoral-results-district-council-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2023/berlin-election-results-berlin-election-2023-electoral-results-district-council-city.csv)
* [berlin-election-results-berlin-election-2023-electoral-results-district-council-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2023/berlin-election-results-berlin-election-2023-electoral-results-district-council-districts.csv)
* [berlin-election-results-berlin-election-2023-electoral-results-district-council-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2023/berlin-election-results-berlin-election-2023-electoral-results-district-council-electoral-districts.csv)
* [berlin-election-results-berlin-election-2023-electoral-results-first-vote-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2023/berlin-election-results-berlin-election-2023-electoral-results-first-vote-city.csv)
* [berlin-election-results-berlin-election-2023-electoral-results-first-vote-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2023/berlin-election-results-berlin-election-2023-electoral-results-first-vote-districts.csv)
* [berlin-election-results-berlin-election-2023-electoral-results-first-vote-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2023/berlin-election-results-berlin-election-2023-electoral-results-first-vote-electoral-districts.csv)
* [berlin-election-results-berlin-election-2023-electoral-results-second-vote-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2023/berlin-election-results-berlin-election-2023-electoral-results-second-vote-city.csv)
* [berlin-election-results-berlin-election-2023-electoral-results-second-vote-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2023/berlin-election-results-berlin-election-2023-electoral-results-second-vote-districts.csv)
* [berlin-election-results-berlin-election-2023-electoral-results-second-vote-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2023/berlin-election-results-berlin-election-2023-electoral-results-second-vote-electoral-districts.csv)

### Berlin Election Results Referendum 2008 Tempelhof Bleibt Verkehrsflughafen

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/tree/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen
* license: GPLv3
* updated: 2025-04-18

**Files**

* [berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-city.csv)
* [berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-districts.csv)
* [berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-electoral-districts.csv)

### Berlin Election Results Berlin Election 2016

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/tree/main/data/03-gold/berlin-election-results-berlin-election-2016
* license: GPLv3
* updated: 2025-05-13

**Files**

* [berlin-election-results-berlin-election-2016-electoral-results-district-council-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2016/berlin-election-results-berlin-election-2016-electoral-results-district-council-city.csv)
* [berlin-election-results-berlin-election-2016-electoral-results-district-council-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2016/berlin-election-results-berlin-election-2016-electoral-results-district-council-districts.csv)
* [berlin-election-results-berlin-election-2016-electoral-results-district-council-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2016/berlin-election-results-berlin-election-2016-electoral-results-district-council-electoral-districts.csv)
* [berlin-election-results-berlin-election-2016-electoral-results-first-vote-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2016/berlin-election-results-berlin-election-2016-electoral-results-first-vote-city.csv)
* [berlin-election-results-berlin-election-2016-electoral-results-first-vote-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2016/berlin-election-results-berlin-election-2016-electoral-results-first-vote-districts.csv)
* [berlin-election-results-berlin-election-2016-electoral-results-first-vote-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2016/berlin-election-results-berlin-election-2016-electoral-results-first-vote-electoral-districts.csv)
* [berlin-election-results-berlin-election-2016-electoral-results-second-vote-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2016/berlin-election-results-berlin-election-2016-electoral-results-second-vote-city.csv)
* [berlin-election-results-berlin-election-2016-electoral-results-second-vote-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2016/berlin-election-results-berlin-election-2016-electoral-results-second-vote-districts.csv)
* [berlin-election-results-berlin-election-2016-electoral-results-second-vote-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2016/berlin-election-results-berlin-election-2016-electoral-results-second-vote-electoral-districts.csv)

### Berlin Election Results Berlin Election 2023

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/tree/main/data/03-gold/berlin-election-results-berlin-election-2023
* license: GPLv3
* updated: 2025-05-13

**Files**

* [berlin-election-results-berlin-election-2023-electoral-results-district-council-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2023/berlin-election-results-berlin-election-2023-electoral-results-district-council-city.csv)
* [berlin-election-results-berlin-election-2023-electoral-results-district-council-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2023/berlin-election-results-berlin-election-2023-electoral-results-district-council-districts.csv)
* [berlin-election-results-berlin-election-2023-electoral-results-district-council-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2023/berlin-election-results-berlin-election-2023-electoral-results-district-council-electoral-districts.csv)
* [berlin-election-results-berlin-election-2023-electoral-results-first-vote-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2023/berlin-election-results-berlin-election-2023-electoral-results-first-vote-city.csv)
* [berlin-election-results-berlin-election-2023-electoral-results-first-vote-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2023/berlin-election-results-berlin-election-2023-electoral-results-first-vote-districts.csv)
* [berlin-election-results-berlin-election-2023-electoral-results-first-vote-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2023/berlin-election-results-berlin-election-2023-electoral-results-first-vote-electoral-districts.csv)
* [berlin-election-results-berlin-election-2023-electoral-results-second-vote-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2023/berlin-election-results-berlin-election-2023-electoral-results-second-vote-city.csv)
* [berlin-election-results-berlin-election-2023-electoral-results-second-vote-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2023/berlin-election-results-berlin-election-2023-electoral-results-second-vote-districts.csv)
* [berlin-election-results-berlin-election-2023-electoral-results-second-vote-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-berlin-election-2023/berlin-election-results-berlin-election-2023-electoral-results-second-vote-electoral-districts.csv)

### Berlin Election Results Referendum 2009 On The Introduction Of The Compulsory Elective Subject Ethics Religion

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/tree/main/data/03-gold/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion
* license: GPLv3
* updated: 2025-04-18

**Files**

* [berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-city.csv)
* [berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-districts.csv)
* [berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-electoral-districts.csv)

### Berlin Election Results Referendum 2011 On The Disclosure Of The Partial Privatisation Contracts At Berliner Wasserbetriebe

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/tree/main/data/03-gold/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe
* license: GPLv3
* updated: 2025-04-18

**Files**

* [berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-city.csv)
* [berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-districts.csv)
* [berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-electoral-districts.csv)

### Berlin Election Results Referendum 2013 On The Remunicipalisation Of Berlins Energy Supply

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/tree/main/data/03-gold/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply
* license: GPLv3
* updated: 2025-04-18

**Files**

* [berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-city.csv)
* [berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-districts.csv)
* [berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-electoral-districts.csv)

### Berlin Election Results Referendum 2014 On The Preservation Of Tempelhofer Feld

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/tree/main/data/03-gold/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld
* license: GPLv3
* updated: 2025-04-18

**Files**

* [berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-city.csv)
* [berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-districts.csv)
* [berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-electoral-districts.csv)

### Berlin Election Results Referendum 2017 On The Continued Operation Of Tegel Airport

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/tree/main/data/03-gold/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport
* license: GPLv3
* updated: 2025-04-18

**Files**

* [berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-city.csv)
* [berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-districts.csv)
* [berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-electoral-districts.csv)

### Berlin Election Results Referendum 2021 Deutsche Wohnen Und Co Enteignen

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/tree/main/data/03-gold/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen
* license: GPLv3
* updated: 2025-04-18

**Files**

* [berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-city.csv)
* [berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-districts.csv)
* [berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-electoral-districts.csv)

### Berlin Election Results Referendum 2023 Berlin 2030 Klimaneutral

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/tree/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral
* license: GPLv3
* updated: 2025-04-18

**Files**

* [berlin-election-results-referendum-2023-berlin-2030-klimaneutral-city.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-city.csv)
* [berlin-election-results-referendum-2023-berlin-2030-klimaneutral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-districts.csv)
* [berlin-election-results-referendum-2023-berlin-2030-klimaneutral-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-electoral-districts.csv)

## Transformation Steps

* [Data blender](../lib/transform/data_blender.py) blends csv data into geojson files

## Output Ports

### Berlin Election Results Berlin Election Geojson

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-berlin-election-geojson
* license: CC-BY 4.0
* updated: 2025-05-15

**Files**

* [berlin-election-results-berlin-election-2016-00-city.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-berlin-election-geojson/berlin-election-results-berlin-election-2016-00-city.geojson)
* [berlin-election-results-berlin-election-2016-00-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-berlin-election-geojson/berlin-election-results-berlin-election-2016-00-districts.geojson)
* [berlin-election-results-berlin-election-2016-00-electoral-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-berlin-election-geojson/berlin-election-results-berlin-election-2016-00-electoral-districts.geojson)
* [berlin-election-results-berlin-election-2023-00-city.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-berlin-election-geojson/berlin-election-results-berlin-election-2023-00-city.geojson)
* [berlin-election-results-berlin-election-2023-00-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-berlin-election-geojson/berlin-election-results-berlin-election-2023-00-districts.geojson)
* [berlin-election-results-berlin-election-2023-00-electoral-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-berlin-election-geojson/berlin-election-results-berlin-election-2023-00-electoral-districts.geojson)

### Berlin Election Results Berlin Election Statistics

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-berlin-election-statistics
* license: CC-BY 4.0
* updated: 2025-05-15

**Files**

* [berlin-election-results-berlin-election-statistics.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-berlin-election-statistics/berlin-election-results-berlin-election-statistics.json)

### Berlin Election Results Referendum 2008 Tempelhof Bleibt Verkehrsflughafen Geojson

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-geojson
* license: CC-BY 4.0
* updated: 2025-05-15

**Files**

* [berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-city.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-geojson/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-city.geojson)
* [berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-geojson/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-districts.geojson)
* [berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-electoral-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-geojson/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-electoral-districts.geojson)

### Berlin Election Results Referendum 2008 Tempelhof Bleibt Verkehrsflughafen Statistics

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-statistics
* license: CC-BY 4.0
* updated: 2025-05-15

**Files**

* [berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-statistics.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-statistics/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-statistics.json)

### Berlin Election Results Referendum 2009 On The Introduction Of The Compulsory Elective Subject Ethics Religion Geojson

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-geojson
* license: CC-BY 4.0
* updated: 2025-05-15

**Files**

* [berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-2009-00-city.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-geojson/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-2009-00-city.geojson)
* [berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-2009-00-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-geojson/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-2009-00-districts.geojson)
* [berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-2009-00-electoral-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-geojson/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-2009-00-electoral-districts.geojson)

### Berlin Election Results Referendum 2009 On The Introduction Of The Compulsory Elective Subject Ethics Religion Statistics

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-statistics
* license: CC-BY 4.0
* updated: 2025-05-15

**Files**

* [berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-statistics.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-statistics/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-statistics.json)

### Berlin Election Results Referendum 2011 On The Disclosure Of The Partial Privatisation Contracts At Berliner Wasserbetriebe Geojson

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-geojson
* license: CC-BY 4.0
* updated: 2025-05-15

**Files**

* [berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-2011-00-city.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-geojson/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-2011-00-city.geojson)
* [berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-2011-00-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-geojson/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-2011-00-districts.geojson)
* [berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-2011-00-electoral-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-geojson/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-2011-00-electoral-districts.geojson)

### Berlin Election Results Referendum 2011 On The Disclosure Of The Partial Privatisation Contracts At Berliner Wasserbetriebe Statistics

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-statistics
* license: CC-BY 4.0
* updated: 2025-05-15

**Files**

* [berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-statistics.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-statistics/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-statistics.json)

### Berlin Election Results Referendum 2013 On The Remunicipalisation Of Berlins Energy Supply Geojson

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-geojson
* license: CC-BY 4.0
* updated: 2025-05-15

**Files**

* [berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-2013-00-city.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-geojson/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-2013-00-city.geojson)
* [berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-2013-00-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-geojson/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-2013-00-districts.geojson)
* [berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-2013-00-electoral-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-geojson/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-2013-00-electoral-districts.geojson)

### Berlin Election Results Referendum 2013 On The Remunicipalisation Of Berlins Energy Supply Statistics

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-statistics
* license: CC-BY 4.0
* updated: 2025-05-15

**Files**

* [berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-statistics.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-statistics/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-statistics.json)

### Berlin Election Results Referendum 2014 On The Preservation Of Tempelhofer Feld Geojson

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-geojson
* license: CC-BY 4.0
* updated: 2025-05-15

**Files**

* [berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-2014-00-city.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-geojson/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-2014-00-city.geojson)
* [berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-2014-00-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-geojson/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-2014-00-districts.geojson)
* [berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-2014-00-electoral-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-geojson/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-2014-00-electoral-districts.geojson)

### Berlin Election Results Referendum 2014 On The Preservation Of Tempelhofer Feld Statistics

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-statistics
* license: CC-BY 4.0
* updated: 2025-05-15

**Files**

* [berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-statistics.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-statistics/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-statistics.json)

### Berlin Election Results Referendum 2017 On The Continued Operation Of Tegel Airport Geojson

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-geojson
* license: CC-BY 4.0
* updated: 2025-05-15

**Files**

* [berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-2017-00-city.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-geojson/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-2017-00-city.geojson)
* [berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-2017-00-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-geojson/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-2017-00-districts.geojson)
* [berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-2017-00-electoral-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-geojson/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-2017-00-electoral-districts.geojson)

### Berlin Election Results Referendum 2017 On The Continued Operation Of Tegel Airport Statistics

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-statistics
* license: CC-BY 4.0
* updated: 2025-05-15

**Files**

* [berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-statistics.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-statistics/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-statistics.json)

### Berlin Election Results Referendum 2021 Deutsche Wohnen Und Co Enteignen Geojson

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-geojson
* license: CC-BY 4.0
* updated: 2025-05-15

**Files**

* [berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-2021-00-city.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-geojson/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-2021-00-city.geojson)
* [berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-2021-00-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-geojson/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-2021-00-districts.geojson)
* [berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-2021-00-electoral-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-geojson/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-2021-00-electoral-districts.geojson)

### Berlin Election Results Referendum 2021 Deutsche Wohnen Und Co Enteignen Statistics

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-statistics
* license: CC-BY 4.0
* updated: 2025-05-15

**Files**

* [berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-statistics.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-statistics/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-statistics.json)

### Berlin Election Results Referendum 2023 Berlin 2030 Klimaneutral Geojson

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-geojson
* license: CC-BY 4.0
* updated: 2025-05-15

**Files**

* [berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-city.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-geojson/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-city.geojson)
* [berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-geojson/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-districts.geojson)
* [berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-electoral-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-geojson/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-electoral-districts.geojson)

### Berlin Election Results Referendum 2023 Berlin 2030 Klimaneutral Statistics

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-statistics
* license: CC-BY 4.0
* updated: 2025-05-15

**Files**

* [berlin-election-results-referendum-2023-berlin-2030-klimaneutral-statistics.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-statistics/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-statistics.json)

## Observability

### Quality metrics
#### geojson_property_completeness
 The percentage of geojson features that have all necessary properties

| File | Value |
| --- | --- |
| berlin-election-results-berlin-election-2016-00-city.geojson | 100 |
| berlin-election-results-berlin-election-2016-00-districts.geojson | 100 |
| berlin-election-results-berlin-election-2016-00-electoral-districts.geojson | 100 |
| berlin-election-results-berlin-election-2023-00-city.geojson | 100 |
| berlin-election-results-berlin-election-2023-00-districts.geojson | 100 |
| berlin-election-results-berlin-election-2023-00-electoral-districts.geojson | 100 |
| berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-city.geojson | 100 |
| berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-districts.geojson | 100 |
| berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-electoral-districts.geojson | 37 |
| berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-2009-00-city.geojson | 100 |
| berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-2009-00-districts.geojson | 100 |
| berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-2009-00-electoral-districts.geojson | 41 |
| berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-2011-00-city.geojson | 100 |
| berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-2011-00-districts.geojson | 100 |
| berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-2011-00-electoral-districts.geojson | 50 |
| berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-2013-00-city.geojson | 100 |
| berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-2013-00-districts.geojson | 100 |
| berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-2013-00-electoral-districts.geojson | 50 |
| berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-2014-00-city.geojson | 100 |
| berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-2014-00-districts.geojson | 100 |
| berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-2014-00-electoral-districts.geojson | 91 |
| berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-2017-00-city.geojson | 100 |
| berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-2017-00-districts.geojson | 100 |
| berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-2017-00-electoral-districts.geojson | 100 |
| berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-2021-00-city.geojson | 100 |
| berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-2021-00-districts.geojson | 100 |
| berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-2021-00-electoral-districts.geojson | 99 |
| berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-city.geojson | 100 |
| berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-districts.geojson | 100 |
| berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-electoral-districts.geojson | 99 |

## Classification

**The nature of the exposed data (source-aligned, aggregate, consumer-aligned)**

consumer-aligned


---
This data product canvas uses the template of [datamesh-architecture.com](https://www.datamesh-architecture.com/data-product-canvas).