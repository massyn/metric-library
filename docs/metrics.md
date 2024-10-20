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
|`ISO27001:2022-A.8.13`|ISO27001:2022|8 Technological controls|Information backup|
|`NIST CSF v2.0-PR.DS-11`|NIST CSF v2.0|PROTECT (PR)|Data Security (PR.DS)|















## Vulnerability Management




### VM01 - Systems without critical vulnerabilities

> This metric measures the number of systems that do not have any critically rated vulnerabilities


#### Scoring

* SLO : 85.00% - 95.00%
* Weight : 0.6

#### Calculation

(`All production systems without any critical vulnerabilities`) / (`All systems in the asset inventory flagged as production`)

#### References

|**Ref**|**Framework**|**Domain**|**Sub Domain**|
|--|--|--|--|
|`ISO27001:2013-A.12.6.1`|ISO27001:2013|12 Operations security|A.12.6 Technical vulnerability management|
|`NIST CSF v2.0-ID.RA-08`|NIST CSF v2.0|IDENTIFY (ID)|Risk Assessment (ID.RA)|
|`ISO27001:2022-A.8.8`|ISO27001:2022|8 Technological controls|Management of technical vulnerabilities|




### VM02 - Systems without a vulnerability management agent

> This metric measures the number of systems that do not have a vulnerability management agent installed.


#### Scoring

* SLO : 90.00% - 95.00%
* Weight : 0.2

#### Calculation

(`All production systems with a vulnerability management agent installed`) / (`All systems in the asset inventory flagged as production`)

#### References

|**Ref**|**Framework**|**Domain**|**Sub Domain**|
|--|--|--|--|
|`ISO27001:2013-A.12.6.1`|ISO27001:2013|12 Operations security|A.12.6 Technical vulnerability management|
|`NIST CSF v2.0-ID.RA-08`|NIST CSF v2.0|IDENTIFY (ID)|Risk Assessment (ID.RA)|
|`ISO27001:2022-A.8.8`|ISO27001:2022|8 Technological controls|Management of technical vulnerabilities|




### VM03 - Time to remediate critical vulnerabilities

> This metric tracks the average time taken to remediate critically rated vulnerabilities from discovery to remediation.


#### Scoring

* SLO : 70.00% - 90.00%
* Weight : 0.4

#### Calculation

(`Total number of days to remediate critical vulnerabilities`) / (`Total number of critical vulnerabilities remediated`)

#### References

|**Ref**|**Framework**|**Domain**|**Sub Domain**|
|--|--|--|--|
|`ISO27001:2013-A.12.6.1`|ISO27001:2013|12 Operations security|A.12.6 Technical vulnerability management|
|`NIST CSF v2.0-ID.RA-08`|NIST CSF v2.0|IDENTIFY (ID)|Risk Assessment (ID.RA)|
|`ISO27001:2022-A.8.8`|ISO27001:2022|8 Technological controls|Management of technical vulnerabilities|




### VM04 - Percentage of vulnerabilities patched within SLA

> This metric measures the percentage of vulnerabilities that are patched within the defined Service Level Agreement (SLA) for the organization.


#### Scoring

* SLO : 80.00% - 95.00%
* Weight : 0.5

#### Calculation

(`Number of vulnerabilities patched within SLA`) / (`Total number of vulnerabilities detected`)

#### References

|**Ref**|**Framework**|**Domain**|**Sub Domain**|
|--|--|--|--|
|`ISO27001:2013-A.12.6.1`|ISO27001:2013|12 Operations security|A.12.6 Technical vulnerability management|
|`NIST CSF v2.0-ID.RA-08`|NIST CSF v2.0|IDENTIFY (ID)|Risk Assessment (ID.RA)|
|`ISO27001:2022-A.8.8`|ISO27001:2022|8 Technological controls|Management of technical vulnerabilities|




### VM05 - Systems with known exploitable vulnerabilities

> This metric tracks the number of systems with known exploitable vulnerabilities as identified in public databases like CVE or vendor advisories.


#### Scoring

* SLO : 75.00% - 90.00%
* Weight : 0.3

#### Calculation

(`All systems with known exploitable vulnerabilities`) / (`All systems in the asset inventory`)

#### References

|**Ref**|**Framework**|**Domain**|**Sub Domain**|
|--|--|--|--|
|`ISO27001:2013-A.12.6.1`|ISO27001:2013|12 Operations security|A.12.6 Technical vulnerability management|
|`NIST CSF v2.0-ID.RA-08`|NIST CSF v2.0|IDENTIFY (ID)|Risk Assessment (ID.RA)|
|`ISO27001:2022-A.8.8`|ISO27001:2022|8 Technological controls|Management of technical vulnerabilities|




