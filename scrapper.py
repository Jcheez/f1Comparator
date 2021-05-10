# Importing libraries
import requests
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self):
        self.driver = ""
        self.constructor = ""

    def scrape_driver(self):
        page = requests.get(self.driver)  # Sends a get request to the site
        soup = BeautifulSoup(page.content, 'html.parser')  # formatting HTML content
        result = soup.find('tbody').find_all(class_='dark')  # finding the table in HTML
        counter = 1
        formatted_result = []  # formatted table after cleaning
        string_placeholder = ""  # Holds the current tag in the for loop
        for tag in result:
            if counter % 4 == 0:
                string_placeholder += f" {tag.get_text()}"
                formatted_result.append(string_placeholder)
                string_placeholder = ""
            elif counter % 2 == 0:
                name = tag.find(class_="hide-for-mobile")
                string_placeholder += f" {name.get_text()}"
            else:
                t = tag.get_text()
                if string_placeholder == "":
                    string_placeholder = t
                else:
                    string_placeholder += f" {t}"
            counter += 1
        return formatted_result

    def scrape_constructor(self):
        page = requests.get(self.constructor)  # Sends a get request to the site
        soup = BeautifulSoup(page.content, 'html.parser')  # formatting HTML content
        result = soup.find('tbody').find_all(class_='dark')  # finding the table in HTML
        counter = 1
        formatted_result = []  # formatted table after cleaning
        string_placeholder = ""  # Holds the current tag in the for loop
        for tag in result:
            if counter % 3 == 0:
                string_placeholder += f" {tag.get_text()}"
                formatted_result.append(string_placeholder)
                string_placeholder = ""
            else:
                t = tag.get_text()
                if string_placeholder == "":
                    string_placeholder = t
                else:
                    string_placeholder += f" {t}"
            counter += 1
        return formatted_result

    def initialise_links(self):
        try:
            file = open("links.txt")
            lines = file.readlines()
            self.driver = lines[0].replace("\n", "")
            self.constructor = lines[1]
            file.close()
        except FileNotFoundError:
            print("Please create the links first")

    @staticmethod
    def create_links():
        new_file = open("links.txt", "w+")
        print("Your links should be from the following site: https://www.formula1.com/en/results.html/2020/drivers.html")
        driver_link = input("Driver's Championship Link: ")
        constructor_link = input("Constructor Championship Link: ")
        new_file.write(driver_link + "\n")
        new_file.write(constructor_link)
        new_file.close()

    @staticmethod
    def edit_links():
        try:
            open("links.txt")
        except FileNotFoundError:
            print("Please create the links first")
            return
        file = open("links.txt", "w+")
        driver_link = input("Driver's Championship Link: ")
        constructor_link = input("Constructor Championship Link: ")
        file.write(driver_link + "\n")
        file.write(constructor_link)
        file.close()
