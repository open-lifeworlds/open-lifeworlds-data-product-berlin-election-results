
# Data Product Canvas - Berlin Election Results

## Metadata

* owner: Open Lifeworlds
* description: Data product combining Berlin election results and geodata
* url: https://github.com/open-lifeworlds/-open-lifeworlds-data-product-berlin-election-results
* license: CC-BY 4.0
* updated: 2025-04-14

## Input Ports

### Berlin LOR geodata

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/tree/main/data
* license: CC-BY-4.0
* updated: 2023-07-22

**Files**

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

### Berlin Election Results Referendum 2008 Tempelhof Bleibt Verkehrsflughafen

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/tree/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen
* license: GPLv3
* updated: 2025-03-15

**Schema**

| Name | Description |
| --- | --- |
| id | combined ID of the district + the electoral (5 digits) |
| district_id | ID of the district (2 digits) |
| electoral_district_id | ID of the electoral district (3 digits) |
| eligible_voters | number of eligible voters |
| voters | number of actual voters |
| invalid_votes | number of invalid votes |
| valid_votes | number of valid votes |
| vote_yes | number of valid votes voting yes |
| vote_no | number of valid votes voting no |
| voter_turnout | percentage of eligible voters that have actually voted |
| invalid_votes_percentage | percentage of invalid votes |
| valid_votes_percentage | percentage of valid votes |
| vote_yes_percentage | percentage of votes voting yes |
| vote_no_percentage | percentage of votes voting no |

**Files**

* [berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-districts.csv)
* [berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-electoral-districts.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results-source-aligned/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-electoral-districts.csv)

## Transformation Steps

* [Data blender](../lib/transform/data_blender.py) blends csv data into geojson files

## Output Ports

### Berlin Election Results Referendum 2008 Tempelhof Bleibt Verkehrsflughafen Geojson

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-geojson
* license: CC-BY 4.0
* updated: 2025-04-14

**Files**

* [berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-geojson/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-districts.geojson)
* [berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-electoral-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-geojson/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-electoral-districts.geojson)

### Berlin Election Results Referendum 2008 Tempelhof Bleibt Verkehrsflughafen Statistics

* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-statistics
* license: CC-BY 4.0
* updated: 2025-04-14

**Files**

* [berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-statistics.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-statistics/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-statistics.json)

## Observability

### Quality metrics
#### geojson_property_completeness
 Describes the percentage of geojson features that have all the properties

| File | Value |
| --- | --- |
| berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-districts.geojson | 1.0 |
| berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-electoral-districts.geojson | 0.37 |

## Classification

**The nature of the exposed data (source-aligned, aggregate, consumer-aligned)**

consumer-aligned


---
This data product canvas uses the template of [datamesh-architecture.com](https://www.datamesh-architecture.com/data-product-canvas).