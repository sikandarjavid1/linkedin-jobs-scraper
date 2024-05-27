# LinkedIn Job Scraper

## Overview

This repository contains Python scripts to scrape job information from LinkedIn based on specified keywords and location.

Firstly, on the basis of keyword and location, a list of jobs along with apply urls will be saved to a csv file. Afterwards, this csv file will be traversed to get text description of each job.



## Usage
Modify the variables in main.py (line 6 and 7 in main.py)to set the desired keywords and location.

Run main.py to initiate the job scraping process and everything else will be catered by the script.

## Requirements

- Python
- Pandas
- Selenium
- BeautifulSoup
- Lxml
- ChromeDriver (ensure it is in the system PATH or provide the path in the script i.e. line 15 in job_scrapper.py and line 19 in helper.py)

**Note:** Don't forget to add credentials in line 16 and 17 in job_scrapper.py.


After configuration, run the `main.py` script:

```bash
python main.py
```

## Contributing

Feel free to contribute by opening issues or submitting pull requests. Your feedback and enhancements are welcome!

