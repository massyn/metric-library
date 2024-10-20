# Metric Library


## Disaster Recovery


### DR01 - Servers backed up in the last 24 hours

> This metric measures the number of systems that have actually been backed up.


#### Scoring

* SLO : 80.00% - 90.00%
* Weight : 0.5

#### Calculation

(`All production servers with a successful backup reported in the last 24 hours`) / (`All servers in the asset inventory flagged as production`)

#### References

|**Ref**|**Framework**|**Domain**|**Sub Domain**|
|--|--|--|--|
|`ISO27001:2013-A.17.2.1`|ISO27001:2013|17 Information security aspects of business continuity management|A.17.2 Redundancies|







## Vulnerability Management




### VM01 - Servers without critical vulnerabilities

> This metric measures the number of systems that do not have any critically rated vulnerabilities


#### Scoring

* SLO : 85.00% - 95.00%
* Weight : 0.6

#### Calculation

(`All production servers without any`) / (`All servers in the asset inventory flagged as production`)

#### References

|**Ref**|**Framework**|**Domain**|**Sub Domain**|
|--|--|--|--|
|`ISO27001:2013-A.12.6.1`|ISO27001:2013|12 Operations security|A.12.6 Technical vulnerability management|
|`NIST CSF v2.0-ID.RA-08`|NIST CSF v2.0|IDENTIFY (ID)|Risk Assessment (ID.RA)|
|`ISO27001:2022-A.8.8`|ISO27001:2022|8 Technological controls|Management of technical vulnerabilities|




