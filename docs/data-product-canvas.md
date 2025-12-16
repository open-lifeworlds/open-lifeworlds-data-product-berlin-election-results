
# Data Product Canvas - Berlin Election Results

## Metadata

* owner: Open Lifeworlds
* description: Data product combining Berlin election results and geodata
* url: https://github.com/open-lifeworlds/-open-lifeworlds-data-product-berlin-election-results
* license: CC-BY 4.0
* updated: 2025-11-23

## Input Ports

### berlin-lor-geodata

* manifest URL: https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-lor-geodata/refs/heads/main/data-product-manifest.yml

### berlin-election-results-source-aligned

* manifest URL: https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-election-results-source-aligned/refs/heads/main/data-product-manifest.yml

## Transformation Steps

* [Data extractor](https://github.com/open-lifeworlds/open-lifeworlds-python-lib/blob/main/openlifeworlds/extract/data_extractor.py) extracts data from inout ports
* [Data blender](https://github.com/open-lifeworlds/open-lifeworlds-python-lib/blob/main/openlifeworlds/transform/data_blender.py) blends csv data into geojson files

## Output Ports

### berlin-election-results-berlin-election-geojson
name: Berlin Election Results Berlin Election Geojson
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-berlin-election-geojson
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-berlin-election-2016-00-city.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-berlin-election-geojson/berlin-election-results-berlin-election-2016-00-city.geojson)
* [berlin-election-results-berlin-election-2016-00-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-berlin-election-geojson/berlin-election-results-berlin-election-2016-00-districts.geojson)
* [berlin-election-results-berlin-election-2016-00-electoral-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-berlin-election-geojson/berlin-election-results-berlin-election-2016-00-electoral-districts.geojson)
* [berlin-election-results-berlin-election-2021-00-city.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-berlin-election-geojson/berlin-election-results-berlin-election-2021-00-city.geojson)
* [berlin-election-results-berlin-election-2021-00-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-berlin-election-geojson/berlin-election-results-berlin-election-2021-00-districts.geojson)
* [berlin-election-results-berlin-election-2021-00-electoral-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-berlin-election-geojson/berlin-election-results-berlin-election-2021-00-electoral-districts.geojson)


### berlin-election-results-berlin-election-statistics
name: Berlin Election Results Berlin Election Statistics
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-berlin-election-statistics
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-berlin-election-statistics.json](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-berlin-election-statistics/berlin-election-results-berlin-election-statistics.json)


### berlin-election-results-european-election-geojson
name: Berlin Election Results European Election Geojson
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-european-election-geojson
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-european-election-2019-00-city.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-european-election-geojson/berlin-election-results-european-election-2019-00-city.geojson)
* [berlin-election-results-european-election-2019-00-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-european-election-geojson/berlin-election-results-european-election-2019-00-districts.geojson)
* [berlin-election-results-european-election-2019-00-electoral-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-european-election-geojson/berlin-election-results-european-election-2019-00-electoral-districts.geojson)
* [berlin-election-results-european-election-2024-00-city.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-european-election-geojson/berlin-election-results-european-election-2024-00-city.geojson)
* [berlin-election-results-european-election-2024-00-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-european-election-geojson/berlin-election-results-european-election-2024-00-districts.geojson)
* [berlin-election-results-european-election-2024-00-electoral-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-european-election-geojson/berlin-election-results-european-election-2024-00-electoral-districts.geojson)


### berlin-election-results-european-election-statistics
name: Berlin Election Results European Election Statistics
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-european-election-statistics
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-european-election-statistics.json](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-european-election-statistics/berlin-election-results-european-election-statistics.json)


### berlin-election-results-federal-election-geojson
name: Berlin Election Results Federal Election Geojson
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-federal-election-geojson
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-federal-election-2017-00-city.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-federal-election-geojson/berlin-election-results-federal-election-2017-00-city.geojson)
* [berlin-election-results-federal-election-2017-00-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-federal-election-geojson/berlin-election-results-federal-election-2017-00-districts.geojson)
* [berlin-election-results-federal-election-2017-00-electoral-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-federal-election-geojson/berlin-election-results-federal-election-2017-00-electoral-districts.geojson)
* [berlin-election-results-federal-election-2021-00-city.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-federal-election-geojson/berlin-election-results-federal-election-2021-00-city.geojson)
* [berlin-election-results-federal-election-2021-00-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-federal-election-geojson/berlin-election-results-federal-election-2021-00-districts.geojson)
* [berlin-election-results-federal-election-2021-00-electoral-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-federal-election-geojson/berlin-election-results-federal-election-2021-00-electoral-districts.geojson)
* [berlin-election-results-federal-election-2025-00-city.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-federal-election-geojson/berlin-election-results-federal-election-2025-00-city.geojson)
* [berlin-election-results-federal-election-2025-00-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-federal-election-geojson/berlin-election-results-federal-election-2025-00-districts.geojson)
* [berlin-election-results-federal-election-2025-00-electoral-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-federal-election-geojson/berlin-election-results-federal-election-2025-00-electoral-districts.geojson)


### berlin-election-results-federal-election-statistics
name: Berlin Election Results Federal Election Statistics
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-federal-election-statistics
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-federal-election-statistics.json](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-federal-election-statistics/berlin-election-results-federal-election-statistics.json)


### berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-geojson
name: Berlin Election Results Referendum 2008 Tempelhof Bleibt Verkehrsflughafen Geojson
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-geojson
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-city.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-geojson/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-city.geojson)
* [berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-geojson/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-districts.geojson)
* [berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-electoral-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-geojson/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-electoral-districts.geojson)


### berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-statistics
name: Berlin Election Results Referendum 2008 Tempelhof Bleibt Verkehrsflughafen Statistics
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-statistics
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-statistics.json](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-statistics/berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-statistics.json)


### berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-geojson
name: Berlin Election Results Referendum 2009 On The Introduction Of The Compulsory Elective Subject Ethics Religion Geojson
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-geojson
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-2009-00-city.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-geojson/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-2009-00-city.geojson)
* [berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-2009-00-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-geojson/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-2009-00-districts.geojson)
* [berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-2009-00-electoral-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-geojson/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-2009-00-electoral-districts.geojson)


### berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-statistics
name: Berlin Election Results Referendum 2009 On The Introduction Of The Compulsory Elective Subject Ethics Religion Statistics
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-statistics
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-statistics.json](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-statistics/berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-statistics.json)


### berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-geojson
name: Berlin Election Results Referendum 2011 On The Disclosure Of The Partial Privatisation Contracts At Berliner Wasserbetriebe Geojson
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-geojson
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-2011-00-city.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-geojson/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-2011-00-city.geojson)
* [berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-2011-00-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-geojson/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-2011-00-districts.geojson)
* [berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-2011-00-electoral-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-geojson/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-2011-00-electoral-districts.geojson)


### berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-statistics
name: Berlin Election Results Referendum 2011 On The Disclosure Of The Partial Privatisation Contracts At Berliner Wasserbetriebe Statistics
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-statistics
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-statistics.json](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-statistics/berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-statistics.json)


### berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-geojson
name: Berlin Election Results Referendum 2013 On The Remunicipalisation Of Berlins Energy Supply Geojson
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-geojson
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-2013-00-city.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-geojson/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-2013-00-city.geojson)
* [berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-2013-00-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-geojson/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-2013-00-districts.geojson)
* [berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-2013-00-electoral-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-geojson/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-2013-00-electoral-districts.geojson)


### berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-statistics
name: Berlin Election Results Referendum 2013 On The Remunicipalisation Of Berlins Energy Supply Statistics
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-statistics
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-statistics.json](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-statistics/berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-statistics.json)


### berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-geojson
name: Berlin Election Results Referendum 2014 On The Preservation Of Tempelhofer Feld Geojson
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-geojson
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-2014-00-city.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-geojson/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-2014-00-city.geojson)
* [berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-2014-00-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-geojson/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-2014-00-districts.geojson)
* [berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-2014-00-electoral-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-geojson/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-2014-00-electoral-districts.geojson)


### berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-statistics
name: Berlin Election Results Referendum 2014 On The Preservation Of Tempelhofer Feld Statistics
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-statistics
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-statistics.json](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-statistics/berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-statistics.json)


### berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-geojson
name: Berlin Election Results Referendum 2017 On The Continued Operation Of Tegel Airport Geojson
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-geojson
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-2017-00-city.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-geojson/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-2017-00-city.geojson)
* [berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-2017-00-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-geojson/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-2017-00-districts.geojson)
* [berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-2017-00-electoral-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-geojson/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-2017-00-electoral-districts.geojson)


### berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-statistics
name: Berlin Election Results Referendum 2017 On The Continued Operation Of Tegel Airport Statistics
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-statistics
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-statistics.json](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-statistics/berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-statistics.json)


### berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-geojson
name: Berlin Election Results Referendum 2021 Deutsche Wohnen Und Co Enteignen Geojson
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-geojson
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-2021-00-city.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-geojson/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-2021-00-city.geojson)
* [berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-2021-00-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-geojson/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-2021-00-districts.geojson)
* [berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-2021-00-electoral-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-geojson/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-2021-00-electoral-districts.geojson)


### berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-statistics
name: Berlin Election Results Referendum 2021 Deutsche Wohnen Und Co Enteignen Statistics
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-statistics
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-statistics.json](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-statistics/berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-statistics.json)


### berlin-election-results-referendum-2023-berlin-2030-klimaneutral-geojson
name: Berlin Election Results Referendum 2023 Berlin 2030 Klimaneutral Geojson
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-geojson
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-city.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-geojson/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-city.geojson)
* [berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-geojson/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-districts.geojson)
* [berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-electoral-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-geojson/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-electoral-districts.geojson)


### berlin-election-results-referendum-2023-berlin-2030-klimaneutral-statistics
name: Berlin Election Results Referendum 2023 Berlin 2030 Klimaneutral Statistics
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/tree/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-statistics
* license: CC-BY 4.0
* updated: 2025-11-23

**Files**

* [berlin-election-results-referendum-2023-berlin-2030-klimaneutral-statistics.json](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-election-results/refs/heads/main/data/03-gold/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-statistics/berlin-election-results-referendum-2023-berlin-2030-klimaneutral-statistics.json)


## Observability

### Quality metrics

 * name: geojson_property_completeness
 * description: The percentage of geojson features that have all necessary properties

| Name | Value |
| --- | --- |
| berlin-election-results-berlin-election-2016-00-city.geojson | 100 |
| berlin-election-results-berlin-election-2016-00-districts.geojson | 100 |
| berlin-election-results-berlin-election-2016-00-electoral-districts.geojson | 100 |
| berlin-election-results-berlin-election-2021-00-city.geojson | 100 |
| berlin-election-results-berlin-election-2021-00-districts.geojson | 100 |
| berlin-election-results-berlin-election-2021-00-electoral-districts.geojson | 100 |
| berlin-election-results-federal-election-2017-00-city.geojson | 100 |
| berlin-election-results-federal-election-2017-00-districts.geojson | 100 |
| berlin-election-results-federal-election-2017-00-electoral-districts.geojson | 100 |
| berlin-election-results-federal-election-2021-00-city.geojson | 100 |
| berlin-election-results-federal-election-2021-00-districts.geojson | 100 |
| berlin-election-results-federal-election-2021-00-electoral-districts.geojson | 100 |
| berlin-election-results-federal-election-2025-00-city.geojson | 100 |
| berlin-election-results-federal-election-2025-00-districts.geojson | 100 |
| berlin-election-results-federal-election-2025-00-electoral-districts.geojson | 100 |
| berlin-election-results-european-election-2019-00-city.geojson | 100 |
| berlin-election-results-european-election-2019-00-districts.geojson | 100 |
| berlin-election-results-european-election-2019-00-electoral-districts.geojson | 100 |
| berlin-election-results-european-election-2024-00-city.geojson | 100 |
| berlin-election-results-european-election-2024-00-districts.geojson | 100 |
| berlin-election-results-european-election-2024-00-electoral-districts.geojson | 100 |
| berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-city.geojson | 100 |
| berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-districts.geojson | 100 |
| berlin-election-results-referendum-2008-tempelhof-bleibt-verkehrsflughafen-2008-00-electoral-districts.geojson | 100 |
| berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-2009-00-city.geojson | 100 |
| berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-2009-00-districts.geojson | 100 |
| berlin-election-results-referendum-2009-on-the-introduction-of-the-compulsory-elective-subject-ethics-religion-2009-00-electoral-districts.geojson | 100 |
| berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-2011-00-city.geojson | 100 |
| berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-2011-00-districts.geojson | 100 |
| berlin-election-results-referendum-2011-on-the-disclosure-of-the-partial-privatisation-contracts-at-berliner-wasserbetriebe-2011-00-electoral-districts.geojson | 100 |
| berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-2013-00-city.geojson | 100 |
| berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-2013-00-districts.geojson | 100 |
| berlin-election-results-referendum-2013-on-the-remunicipalisation-of-berlins-energy-supply-2013-00-electoral-districts.geojson | 100 |
| berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-2014-00-city.geojson | 100 |
| berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-2014-00-districts.geojson | 100 |
| berlin-election-results-referendum-2014-on-the-preservation-of-tempelhofer-feld-2014-00-electoral-districts.geojson | 100 |
| berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-2017-00-city.geojson | 100 |
| berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-2017-00-districts.geojson | 100 |
| berlin-election-results-referendum-2017-on-the-continued-operation-of-tegel-airport-2017-00-electoral-districts.geojson | 100 |
| berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-2021-00-city.geojson | 100 |
| berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-2021-00-districts.geojson | 100 |
| berlin-election-results-referendum-2021-deutsche-wohnen-und-co-enteignen-2021-00-electoral-districts.geojson | 100 |
| berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-city.geojson | 100 |
| berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-districts.geojson | 100 |
| berlin-election-results-referendum-2023-berlin-2030-klimaneutral-2023-00-electoral-districts.geojson | 100 |


## Classification

**The nature of the exposed data (source-aligned, aggregate, consumer-aligned)**

consumer-aligned


---
This data product canvas uses the template of [datamesh-architecture.com](https://www.datamesh-architecture.com/data-product-canvas).