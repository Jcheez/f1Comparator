from predictions import Prediction
from scrapper import Scrapper

### Statistics class ###
class Statistics:
    def __init__(self):
        self.has_scrapper_links = False
        self.has_valid_predictions = False
        self.driver_standings = []
        self.team_standings = []
        self.predictions = {}

    def check_stats(self):
        try:
            open("links.txt")
            open("predictions.txt")
            self.has_scrapper_links = True
            self.has_valid_predictions = True
        except FileNotFoundError:
            print("Statistics cannot be initialised, predictions and links not properly configured")
        return self

    def initialise_stats(self):
        if self.has_scrapper_links and self.has_valid_predictions:
            self.predictions = Prediction().initialise_prediction().get_all_prediction()
            self.driver_standings = Scrapper().initialise_links().scrape_driver()
            self.team_standings = Scrapper().initialise_links().scrape_constructor()
            return self
        else:
            print("Links and predictions not initialised properly")
            return self

    def count_driver_zeros(self):
        counter = 0
        for info in self.driver_standings:
            formatted_info = info.split(" ")
            if formatted_info[3] == "0":
                counter += 1
        return counter

    def min_driver_zero(self):
        counter = 1
        for info in self.driver_standings:
            formatted_info = info.split(" ")
            if formatted_info[3] == "0":
                break
            counter += 1
        return counter

    def count_team_zeros(self):
        counter = 0
        for info in self.team_standings:
            formatted_info = info.split(" ")
            if formatted_info[-1] == "0":
                counter += 1
        return counter

    def min_team_zero(self):
        counter = 1
        for info in self.team_standings:
            formatted_info = info.split(" ")
            if formatted_info[-1] == "0":
                break
            counter += 1
        return counter

    def calculate_deviation(self, name, who):
        if who == "driver":
            driver_prediction = self.predictions[name]["drivers"]
            inaccuracy_score = 0
            current_predicted_position = 1
            current_actual_position = 1
            for cd in driver_prediction:
                for ranking in self.driver_standings:
                    if cd.lower() in ranking.lower():
                        if ranking.split(" ")[3] == "0":
                            if current_predicted_position < self.min_driver_zero():
                                score = abs(self.min_driver_zero() - current_predicted_position)
                                inaccuracy_score += score
                                current_actual_position = 1
                            else:
                                inaccuracy_score += 0
                                current_actual_position = 1
                        else:
                            score = abs(current_actual_position - current_predicted_position)
                            inaccuracy_score += score
                            current_actual_position = 1
                        break
                    current_actual_position += 1
                current_predicted_position += 1
            return inaccuracy_score
        elif who == "team":
            driver_prediction = self.predictions[name]["teams"]
            inaccuracy_score = 0
            current_predicted_position = 1
            current_actual_position = 1
            for cd in driver_prediction:
                for ranking in self.team_standings:
                    if cd.lower() in ranking.lower():
                        if ranking.split(" ")[2] == "0":
                            if current_predicted_position < self.min_team_zero():
                                score = abs(self.min_team_zero() - current_predicted_position)
                                inaccuracy_score += score
                                current_actual_position = 1
                            else:
                                inaccuracy_score += 0
                                current_actual_position = 1
                        else:
                            score = abs(current_actual_position - current_predicted_position)
                            inaccuracy_score += score
                            current_actual_position = 1
                        break
                    current_actual_position += 1
                current_predicted_position += 1
            return inaccuracy_score

    def calculate_all_deviation(self, who):
        for person in self.predictions.keys():
            print(person)
            print(self.calculate_deviation(person, who))
