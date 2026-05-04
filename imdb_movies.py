from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import os

driver = webdriver.Chrome()
driver.get("https://www.imdb.com/chart/top/")

time.sleep(5)  # wait page load

movies = []

# OLD IMDb table style (THIS WORKS BETTER)
rows = driver.find_elements(By.CSS_SELECTOR, "tbody.lister-list tr")

print("Rows found:", len(rows))

for row in rows[:20]:
    try:
        name = row.find_element(By.CSS_SELECTOR, ".titleColumn a").text
        rank = row.find_element(By.CSS_SELECTOR, ".titleColumn").text.split(".")[0].strip()
        year = row.find_element(By.CSS_SELECTOR, ".secondaryInfo").text.strip("()")
        rating = row.find_element(By.CSS_SELECTOR, ".imdbRating strong").text

        movies.append([rank, name, year, rating])

    except Exception as e:
        print("Skipping row:", e)

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = os.path.join(desktop, "imdb_movies.csv")

with open(file_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Rank", "Movie Name", "Year", "Rating"])
    writer.writerows(movies)

print("DONE 💛 CSV saved on Desktop!")

input("Press Enter to close...")
driver.quit()
