import csv
import re
import requests
from bs4 import BeautifulSoup


def get_potential_emails(soup_string):
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", soup_string)
    emails = set(emails)
    print("Unique emails found:", emails)

    if len(emails) == 1:
        return emails.pop()
    elif len(emails) == 0:
        return ""
    else:
        return str(emails)


def get_potential_web_form_vendor(soup_string):
    # check if ".securiti." or ".onetrust." are in the HTML page
    if "securiti" in soup_string:
        print("Web form vendor found: Securiti")
        return "Securiti"
    elif "onetrust" in soup_string:
        print("Web form vendor found: OneTrust")
        return "OneTrust"
    else:
        print("Web form vendor not found.")
        return ""


def check_ccpa(page_text):
    regex_ccpa = re.compile(r'(California( Consumer Privacy Act)?)|(\(?C\.?C\.?P\.?A\.?\)?)')
    regex_cpra = re.compile(r'(California( Privacy Rights Act)?)|(\(?C\.?P\.?R\.?A\.?\)?)')
    return bool(regex_ccpa.search(page_text)) or bool(regex_cpra.search(page_text))  # checks for mention of either the CCPA or CPRA (which is now just the CCPA)


def check_cpa(page_text):
    regex = re.compile(r'(Colorado( Privacy Act)?)|(\b\(?C\.?P\.?A\.?\)?)')
    return bool(regex.search(page_text))


def check_ctdpa(page_text):
    regex = re.compile(r'(Connecticut( Data Privacy Act)?)|(\(?C\.?T\.?D\.?P\.?A\.?\)?)')
    return bool(regex.search(page_text))


def check_cdpa(page_text):
    regex = re.compile(r'(Virginia( Consumer Data Protection Act)?)|(\(?V\.?C\.?D\.?P\.?A\.?\)?)')
    return bool(regex.search(page_text))


def check_ucpa(page_text):
    regex = re.compile(r'(Utah( Consumer Privacy Act)?)|(\(?U\.?C\.?P\.?A\.?\)?)')
    return bool(regex.search(page_text))  # returns T or F


if __name__ == '__main__':
    # To test an HTML file "offline", first fetch the .html file:
    # page = requests.get('https://www.url/privacy-policy')

    # with open('privacy_policy_name.html', 'rb') as f:
    #    soup = BeautifulSoup(f.read(), features="html.parser")

    input_file_path = 'input_file.csv'
    output_file_path = 'output_file.csv'

    print("Beginning program.")

    # Thanks to https://stackoverflow.com/a/57518881
    with open(input_file_path, 'r', newline='') as inputFile, open(output_file_path, 'w', newline='') as writerFile:
        read_file = csv.reader(inputFile)
        write_file = csv.writer(writerFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        print("File opened:", input_file_path, "|", "Writing to:", output_file_path)
        print("---------------------------------------------------------------------------")
        r = 0
        for row in read_file:
            # row[0]=company, row[1]=pp, row[2]=email, row[3]=webform, row[4]=webform_vendor,
            # row[5]=ccpa, row[6]=cpa, row[7]=ctdpa, row[8]=cdpa, row[9]=ucpa, row[10]=notes

            if r == 0:  # for the first row in the CSV, just copy the column headers
                write_file.writerow(row)
                r += 1
                continue

            else:
                company_name = row[0]
                privacy_policy_url = row[1]

                print("Attempting request:", company_name, "|", privacy_policy_url)

                page = requests.get(privacy_policy_url)

                if page.status_code == 200:
                    print("Connection successful (HTTP 200 OK). Now scraping:", company_name)
                    soup = BeautifulSoup(page.content, features="html.parser")
                    soup_string = str(soup)

                    page_text = soup.get_text()

                    page_output_row = (row[0],
                                       row[1],
                                       get_potential_emails(soup_string),
                                       "",  # to do: link to web form(s)
                                       get_potential_web_form_vendor(soup_string),
                                       check_ccpa(page_text),
                                       check_cpa(page_text),
                                       check_ctdpa(page_text),
                                       check_cdpa(page_text),
                                       check_ucpa(page_text),
                                       "")

                else:
                    print("Connection failed. Continuing to next company.")

                print("Output row:", page_output_row)
                write_file.writerow(page_output_row)
                print("---------------------------------------------------------------------------")