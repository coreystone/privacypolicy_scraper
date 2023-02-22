# Privacy Policy Scraper


## ⚠️ DISCLAIMER
Most websites prohibit automatic collection/processing ("scraping") of their resources, and using this program on most sites will likely be in violation of the site's Terms of Service. This repository is provided strictly for *educational* purposes and I do not condone or encourage the use of this program on sites that do not belong to you, nor am I responsible for the consequences of what you choose to do with this code.


## 🔍 About
**Privacy Policy Scraper** is a web-scraper designed to provide insight about a US-based company's privacy policy. It uses Python to fetch a company's privacy policy and tries to analyze the data rights the company affords to its customers, how to file a data request with the company, and also info about the request process itself. Most websites are *not* created equally and therefore the results for certain sites may vary as the program may not be able to read specific policy pages due to how they are configured. This means that results are not always reliable and manual review for each company is always recommended (and is actually intended by design). 


## 📑 What is collected?
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


## ⚙️ How to run
1. Download the provided `.py` and `.csv` files and place them in the same directory
2. Configure the `input_file_path` variable in the program according to the location of your CSV file
3. Add entries to the CSV file to be parsed. For each entry, add a `Company` name and `Privacy Policy` URL as seen in the provided example file.
4. Run the program: `python3 main.py`
5. Review the generated results in `output_file.csv` and add and correct information where needed


## 📌 To-Do List
* Scrape the link to web form(s) if it exists
* Format console output for improved visibility of events
* Documentation/comments
* Convert resulting .csv into Markdown (.md) table 
