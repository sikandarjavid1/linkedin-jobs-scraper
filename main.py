from helper import *
from job_scrapper import *


#Use these variables to d change city or role accordingly
keywords='Marketing Data Analyst'
location='Berlin, Berlin, Germany'


keywords_encoded=quote(keywords)
location_encoded=quote(location)

url1=f'https://www.linkedin.com/jobs/search?keywords={keywords_encoded}&location={location_encoded}&geoId=106967730&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'

# job_info=find_profiles(url1)
# job_info.to_csv('sample_testing.csv')

driver=login()
extract_jd('sample.csv',driver)