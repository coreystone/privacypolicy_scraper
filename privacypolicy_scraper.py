import pandas as pd
import re
import requests
from bs4 import BeautifulSoup


def get_potential_emails(soup_string):
    """
    Find any email addresses within the page
    """
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", soup_string)
    emails = set(emails)
    print("Unique emails found:", emails) if(len(emails) > 0) else print("Email address not found.")

    if len(emails) == 1:
        return emails.pop()
    elif len(emails) == 0:
        return ""
    else:
        return emails


def get_potential_web_form_vendor(soup_string) -> str:
    """
    Returns the name of the web form vendor a site is using, if it can be found. Compare to the set of URLs fetched.
    """
    if "logicmanager" in soup_string:
        print("Web form vendor found: Logic Manager")
        return "Logic Manager"
    elif "onetrust" in soup_string:
        print("Web form vendor found: OneTrust")
        return "OneTrust"
    elif "securiti" in soup_string:
        print("Web form vendor found: Securiti")
        return "Securiti"
    elif "trustarc" in soup_string:
        print("Web form vendor found: TrustArc")
        return "TrustArc"
    elif "truyo" in soup_string:
        print("Web form vendor found: Truyo")
        return "Truyo"
    elif "zendesk" in soup_string:
        print("Web form vendor found: Zendesk")
        return "Zendesk"
    else:
        print("Web form vendor not found.")
        return ""


def get_potential_web_form(soup):
    """
    Attempts to scrape URL of a web form to exercise privacy rights (such as a OneTrust web form).
    Uses a regex pattern to search for known web form provider domains. Saves a set of unique links that match the pattern.
    """
    links = []
    pattern = "(.logicmanager.com)|(.onetrust.com)|(.securiti.ai)|(.trustarc.com)|(.truyo.com)|(.zendesk.com)"
    for link in soup.findAll('a', attrs={'href': re.compile(pattern)}):
        links.append(link.get('href'))

    links = set(links)
    print("Unique web forms found:", links) if (len(links) > 0) else print("Web form not found.")
    if len(links) == 1:
        return links.pop()
    elif len(links) == 0:
        return ""
    else:
        return links


def check_ccpa(page_text) -> bool:
    """
    returns True or False depending on result of California Consumer Privacy Act (CCPA) regular expression
    The CPRA is now part of the CCPA, but it may still appear in privacy policies that haven't been updated recently.
    """
    regex_ccpa = re.compile(r'(California( Consumer Privacy Act)?)|(\(?C\.?C\.?P\.?A\.?\)?)')
    regex_cpra = re.compile(r'(California( Privacy Rights Act)?)|(\(?C\.?P\.?R\.?A\.?\)?)')
    if bool(regex_ccpa.search(page_text)) or bool(regex_cpra.search(page_text)): print("--- CCPA mentioned")
    return bool(regex_ccpa.search(page_text)) or bool(regex_cpra.search(page_text))


def check_cpa(page_text) -> bool:
    """
    returns True or False depending on result of Colorado Privacy Act (CPA) regular expression
    """
    regex = re.compile(r'(Colorado( Privacy Act)?)|(\b\(?C\.?P\.?A\.?\)?)')
    if bool(regex.search(page_text)): print("--- CPA mentioned")
    return bool(regex.search(page_text))


def check_ctdpa(page_text) -> bool:
    """
    returns True or False depending on result of Connecticut Data Privacy Act (CTDPA) regular expression
    """
    regex = re.compile(r'(Connecticut( Data Privacy Act)?)|(\(?C\.?T\.?D\.?P\.?A\.?\)?)')
    if bool(regex.search(page_text)): print("--- CTDPA mentioned")
    return bool(regex.search(page_text))


def check_cdpa(page_text) -> bool:
    """
    returns True or False depending on result of Viriginia Consumer Data Protection Act ((V)CDPA) regular expression
    """
    regex = re.compile(r'(Virginia( Consumer Data Protection Act)?)|(\(?V?\.?C\.?D\.?P\.?A\.?\)?)')
    if bool(regex.search(page_text)): print("--- CDPA mentioned")
    return bool(regex.search(page_text))


def check_ucpa(page_text) -> bool:
    """
    returns True or False depending on result of Utah Consumer Privacy Act (UCPA) regular expression
    """
    regex = re.compile(r'(Utah( Consumer Privacy Act)?)|(\(?U\.?C\.?P\.?A\.?\)?)')
    if bool(regex.search(page_text)): print("--- UCPA mentioned")
    return bool(regex.search(page_text))


if __name__ == '__main__':
    # To test an HTML file "offline", first fetch the .html file:
    # page = requests.get('https://www.url/privacy-policy')

    # with open('privacy_policy_name.html', 'rb') as f:
    #    soup = BeautifulSoup(f.read(), features="html.parser")

    input_file_path  = 'input_file.csv'
    output_file_path = 'output_file.csv'

    print("Beginning Privacy Policy Scraper...")

    try:
        df = pd.read_csv(input_file_path)
        df.fillna('', inplace=True)  # Replaces all NaN values with empty string for adding values
    except:
        print("Couldn't read .CSV file. Check formatting and try again.")

    print("File opened:", input_file_path, "|", "Writing to:", output_file_path)
    print("---------------------------------------------------------------------------")

    for row in df.itertuples():
        # row[0]=company, row[1]=pp, row[2]=email, row[3]=webform, row[4]=webform_vendor,
        # row[5]=ccpa, row[6]=cpa, row[7]=ctdpa, row[8]=cdpa, row[9]=ucpa, row[10]=notes

        company_name       = row.Company
        privacy_policy_url = row.PrivacyPolicy

        print("[#{index}] Attempting request:".format(row.Index), company_name, "|", privacy_policy_url)

        try:
            page = requests.get(privacy_policy_url)

        except:
            print("(EXCEPTION) Error: moving to next company.")
            print("---------------------------------------------------------------------------")
            continue

        if page.status_code == 200:
            print("Connection successful (HTTP 200 OK). Begin parsing.")
            soup = BeautifulSoup(page.content, features="html.parser")
            soup_string = str(soup)

            page_text = soup.get_text()

            df.at[row.Index, "Company"] = company_name
            df.at[row.Index, "PrivacyPolicy"] = privacy_policy_url
            df.at[row.Index, "Contact"] = get_potential_emails(soup_string)
            df.at[row.Index, "WebForm"] = get_potential_web_form(soup)
            df.at[row.Index, "WebFormVendor"] = get_potential_web_form_vendor(soup_string)
            df.at[row.Index, "CCPA"] = check_ccpa(page_text)
            df.at[row.Index, "CPA"] = check_cpa(page_text)
            df.at[row.Index, "CTDPA"] = check_ctdpa(page_text)
            df.at[row.Index, "CDPA"] = check_cdpa(page_text)
            df.at[row.Index, "UCPA"] = check_ucpa(page_text)

        elif page.status_code == 403:  # Read: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
            print("Connection refused (HTTP 403 FORBIDDEN). Continuing to next company.")

        elif page.status_code == 406:  # Read: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/406
            print("Connection refused (HTTP 406 NOT ACCEPTED). Continuing to next company.")

        else:
            print("Unexpected behavior; connection failed: HTTP", page.status_code,". Continuing to next company.")

        print("Output row:", row)
        print("---------------------------------------------------------------------------")

    df.to_csv(output_file_path, index=False) # Saves the result to CSV in output path