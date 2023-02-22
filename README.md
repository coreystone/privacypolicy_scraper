# Privacy Policy Scraper


## DISCLAIMER
Most websites prohibit automatic collection/processing ("scraping") of their resources, and using this program on most sites will likely be in violation of the site's Terms of Service. This repository is provided strictly for *educational* purposes and I do not condone or encourage the use of this program on sites that do not belong to you, nor am I responsible for the consequences of what you choose to do with this code. Do not 


## About
**Privacy Policy Scraper** is a web-scraper designed to provide insight about a US-based company's privacy policy. It uses Python to fetch a company's privacy policy and tries to analyze the data rights the company affords to its customers, how to file a data request with the company, and also info about the request process itself. Most websites are *not* created equally and therefore the results for certain sites may vary as the program may not be able to read specific policy pages due to how they are configured. This means that results are not always reliable and manual review for each company is always recommended (and is actually intended by design). 


## What is collected?
Privacy Policy Scraper attempts to identify the following elements of a company's privacy policy:
* Contact email address of the company's privacy department/handler
* Web form where a user can exercise their data rights with company (if applicable)
* The web form solution used by company (if applicable): [OneTrust](https://www.onetrust.com/) or [Securiti.ai](https://securiti.ai/)
* The company's explicit acknowledgement of the following US legal privacy frameworks:
    * [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa)
    * [Colorado Privacy Act (CPA)](https://coag.gov/resources/colorado-privacy-act/)
    * [Connecticut Data Privacy Act (CTDPA)](https://portal.ct.gov/AG/Sections/Privacy/The-Connecticut-Data-Privacy-Act)
    * [Utah Consumer Privacy Act (UCPA)](https://wirewheel.io/blog/utah-consumer-privacy-act/)
    * [Virginia Consumer Data Protection Act (CDPA)](https://law.lis.virginia.gov/vacodefull/title59.1/chapter53/)
