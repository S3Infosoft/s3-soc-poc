# s3-soc-poc
SOC POC


## Populating an Application insights instance

```python3 sen-python-demo.py INSTRUMENTATION-KEY```

When an application insights instance is setup (Assuming instructions have been followed from Azure_POC>CEF data connector>Application insights), use this script to generate sample logs & populate the sentinel dashboard/log analytics logspace.

## Populating from existing CEF log file

```chmod +x populateSampleFromCEF.sh
./populateSampleFromCEF.sh logfile.txt
```

After setting up the OMS agent pass a text file containing CEF formatted logs. Sample CEF logs can be downlaod from https://logs.to/

OR

Run this script to populate sentinel with a small number of logs.

```chmod +x populateSample.sh
./populateSample.sh
```
