## PersonalRecordsTable

||Key |val
|---|---|---|
|Hash|Name|S|
|Range|Year or Profile?|S|
||Team|S|
|||(Records)|...|

- Year（GSI1Hash）に対してName（GSI1Range）をscan
- Name(Hash)に対してYear or Profile（Range）をscan
- Year（GSI2Hash）に対してTeam(GSI2Range)でquery


## TeamRecprdsTable