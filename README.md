# organization-catalog-etl
ETL for organization-catalogue

Need to have: 
- admin auth token for environment to be worked on (in a file; token.txt)
- port-forwarded elasticsearch pod for two of the environments

See makefile for commands

Run order:

1. post_loop.py
This forces organization-catalogue to update prefLabels for all organizations
   
2. get_elastic.py
This fetches data from elastic. Staging and demo does not have a running fdk-dataset-api, so you'll have to utilize 
   a port-forwarded elastic-pod.
   Production can simply fetch this data via /publisher endpoint. (this will be removed soon)
   
3. put_loop.py
Updates organization-catalogue with prefLabels from elastic