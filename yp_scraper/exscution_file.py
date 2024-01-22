import yp_scraper.spiders.electrtion
import yp_scraper.spiders.plumber_scraper 
import yp_scraper.spiders.restruant_spider 
from scrapy.crawler import CrawlerProcess
import random
import csv
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                              QComboBox, QPushButton, QGridLayout, QVBoxLayout)



def main(user_input, choice):
    run_project(choice)
    
    with open("items.csv", newline = "") as file:
        jsonData = csv.DictReader(file)
        plumber_data = [row for row in jsonData]

    if user_input == "get highest rated business":
        name = find_email_of_best_plumber(plumber_data)
        return f'The highest rated {choice} is {name}'
    elif user_input == "get random business":
        name = get_rand_bis(plumber_data)
        return f'The random {choice} is {name}'
    elif user_input == "get business with no website":
        name = get_bis_no_email(plumber_data)
        return f'The {choice} with no website is {name}'

def find_email_of_best_plumber(plumber_data):
    best = 0
    x = 0
    for row in plumber_data:
        stars = row['stars_out_of_five']
        num_of_reviews = row['number_of_riews']
        if stars == 'rating-stars five' and plumber_data[best]['stars_out_of_five'] != 'rating-stars five' and num_of_reviews < plumber_data[best]['number_of_riews']:
            best = x
        x += 1
    return plumber_data[best]['name']
def get_bis_no_email(plumber_data):
    x = 0
    for row in plumber_data:
        if row['website'] == None:
            return plumber_data[row]['name']
        x += 1
def get_rand_bis(plumber_data):
    highe = len(plumber_data)
    random_integer = random.randrange(highe+1)
    return plumber_data[random_integer]['name']


def run_project(choice):
    if choice == 'plumbers':
        process = CrawlerProcess( settings={"FEEDS": {"items.csv": {"format": "csv"},},})
        process.crawl(yp_scraper.spiders.plumber_scraper.PlumberScraperSpider)
        process.start()
    elif choice =='restruants':
        process = CrawlerProcess( settings={"FEEDS": {"items.csv": {"format": "csv"},},})
        process.crawl(yp_scraper.spiders.restruant_spider.RestruantSpiderSpider)
        process.start()
    elif choice == 'electrtions':
        process = CrawlerProcess( settings={"FEEDS": {"items.csv": {"format": "csv"},},})
        process.crawl(yp_scraper.spiders.electrtion.ElectrtionSpider)
        process.start()



class NumberApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # First page widgets
        self.first_labe = QLabel("What business would you like to serch for?", self)
        self.first_box = QComboBox(self)
        self.first_box.addItems(['plumbers', 'restruants', 'electrtions'])
        self.sup_label = QLabel("Waht data would you like to find", self)
        self.number_combo = QComboBox(self)
        self.number_combo.addItems(["get highest rated business", "get business with no website", "get random business",])
        submit_button = QPushButton("Submit", self)

        # Layout for first page
        layout = QGridLayout()
        layout.addWidget(self.first_labe, 0, 0)
        layout.addWidget(self.first_box, 1, 0)
        layout.addWidget(self.sup_label, 2, 0)
        layout.addWidget(self.number_combo, 3, 0)
        layout.addWidget(submit_button, 4, 0)
        self.setLayout(layout)

        # Second page widgets
        self.second_page = QWidget()
        self.number_display = QLabel("", self.second_page)
        self.back_button = QPushButton("Back", self.second_page)

        # Layout for second page
        second_layout = QVBoxLayout()
        second_layout.addWidget(self.number_display)
        second_layout.addWidget(self.back_button)
        self.second_page.setLayout(second_layout)

        # Button actions
        submit_button.clicked.connect(self.show_second_page)
        self.back_button.clicked.connect(self.show_first_page)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Number App')
        self.show()


    def show_second_page(self):
        selected_data = self.number_combo.currentText()
        users_data = main(selected_data, self.first_box.currentText())
        self.number_display.setText(f"{users_data}")
        self.second_page.show()
        self.hide()

    def show_first_page(self):
        self.show()
        self.second_page.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NumberApp()
    sys.exit(app.exec_())