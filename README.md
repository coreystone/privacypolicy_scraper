# Privacy Policy Scraper


## ⚠️ DISCLAIMER
Most websites prohibit automatic collection/processing ("scraping") of their resources, and using this program on most sites will likely be in violation of some terms of service notices for respective sites. This repository is provided strictly for *educational* purposes and I do not condone or encourage the use of this program on sites that do not belong to you, nor am I responsible for the consequences of what you choose to do with this code. 


## 🔍 About
**Privacy Policy Scraper** is a web-scraper designed to provide insight about a US-based company's privacy policy. It uses Python to fetch a company's privacy policy and tries to analyze the data rights the company affords to its customers, how to file a data request with the company, and also info about the request process itself. Most websites are *not* created equally and therefore the results for certain sites may vary as the program may not be able to read specific policy pages due to how they are configured. This means that results are not always reliable and manual review for each company is always recommended (and is actually intended by design). 


## 📑 What is collected?
Privacy Policy Scraper attempts to identify the following elements of a company's privacy policy:
* Contact email address of the company's privacy department/officer
* Link to a web form where a user can exercise their data rights (if applicable)
* The web form solution used by company (if applicable): 
   * [LogicManager](https://www.logicmanager.com/)
   * [OneTrust](https://www.onetrust.com/)
   * [Securiti.ai](https://securiti.ai/)
   * [TrustArc](https://trustarc.com/)
   * [Truyo](https://truyo.com/)
* The company's explicit acknowledgement of the following US legal privacy frameworks:
    * [California Consumer Privacy Act (CCPA)](https://www.oag.ca.gov/privacy/ccpa)
    * [Colorado Privacy Act (CPA)](https://coag.gov/resources/colorado-privacy-act/)
    * [Connecticut Data Privacy Act (CTDPA)](https://portal.ct.gov/AG/Sections/Privacy/The-Connecticut-Data-Privacy-Act)
    * [Utah Consumer Privacy Act (UCPA)](https://wirewheel.io/blog/utah-consumer-privacy-act/)
    * [Virginia Consumer Data Protection Act (CDPA)](https://law.lis.virginia.gov/vacodefull/title59.1/chapter53/)
* Checks if a privacy policy includes a link to a CCPA metrics report. See [this relevant project](https://github.com/privacy-tech-lab/ccpa-metrics) by privacytechlab.org.


## ⚙️ How to run
1. Download the provided `.py` and `.csv` files and place them in the same directory
2. Configure the `input_file_path` variable in the program according to the location of your CSV file
3. Add entries to the CSV file to be parsed. For each entry, add a `Company` name and `Privacy Policy` URL as seen in the provided example file.
4. Run the program: `python3 main.py`
5. Review the generated results in `output_file.csv` and add and correct information where needed


## 📌 To-Do List
* Add search for [Nevada privacy law](https://termageddon.com/nevada-revised-statutes-chapter-603a/)
* Format console printing for resulting output rows
* Add Selenium to scrape the privacy policy automatically rather than manually linking it


## ❓ Potential features
Here are some things I'm considering adding but not sure if their usefulness would outweight the clutter/mess they would add to the resulting amount of fields/data across the directory.
* Collect phone number for contact
* Collect the date of the policy was posted/updated
* Identify if a site respects [Do Not Track requests](https://en.wikipedia.org/wiki/Do_Not_Track) per [California Business & Professions Code Section 22575](https://codes.findlaw.com/ca/business-and-professions-code/bpc-sect-22575/)