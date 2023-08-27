import csv
import nltk
from colorama import Fore, Style

nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

# Creating an instance of the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Function to classify the review into 5-star categories
def classify_review(review):
    # Analyzing the sentiment of the review
    sentiment_score = sia.polarity_scores(review)['compound']
    # Classifying the review based on the sentiment score
    if sentiment_score >= 0.8:
        return 5
    elif sentiment_score >= 0.6:
        return 4
    elif sentiment_score >= 0.4:
        return 3
    elif sentiment_score >= 0.2:
        return 2
    else:
        return 1

while True:
    print(Fore.BLUE + "\n====== Sentiment Analysis Tool ======\n" + Style.RESET_ALL)
    print(Fore.GREEN + "Select an option:" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Enter a review manually" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Stop" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Read reviews from a CSV file\n" + Style.RESET_ALL)
    option = input(Fore.GREEN + "Enter your option: " + Style.RESET_ALL)

    if option == '1':
        print(Fore.BLUE + "\n====== Manual Review Entry ======\n" + Style.RESET_ALL)
        review = input(Fore.GREEN + "Enter your review: " + Style.RESET_ALL)
        rating = classify_review(review)
        print(Fore.YELLOW + "\nYour review is rated as:", rating, "stars\n" + Style.RESET_ALL)
    elif option == '2':
        print(Fore.RED + "\nExiting the program...\n" + Style.RESET_ALL)
        break
    elif option == '3':
        print(Fore.BLUE + "\n====== CSV Review Entry ======\n" + Style.RESET_ALL)
        file_name = input(Fore.GREEN + "Enter the CSV file name (with extension): " + Style.RESET_ALL)
        show_reviews = input(Fore.GREEN + "Do you want to show the output review star for each review in the file? (y/n): " + Style.RESET_ALL)
        reviews = []
        with open(file_name, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                review = row[0]
                rating = classify_review(review)
                if show_reviews.lower() == 'y':
                    print(Fore.YELLOW + "\nReview:", review)
                    print("Rating:", rating, "stars\n" + Style.RESET_ALL)
                reviews.append(rating)
        print(Fore.GREEN + "\nThe reviews from the file have been added.")
        avg_rating = sum(reviews) / len(reviews)
        print("The average star rating of all reviews in the file is:", avg_rating, "stars\n" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\nInvalid option. Please enter 1, 2, or 3.\n" + Style.RESET_ALL)

print(Fore.BLUE + "\n====== Program Ended ======\n" + Style.RESET_ALL)
