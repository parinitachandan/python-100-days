from bs4 import BeautifulSoup
import requests
import smtplib
import lxml

EMAIL = "pcparinita@gmail.com"
PASSWORD = "xhgieuswlcylkacz"

url = "https://www.amazon.com/dp/B09SBRW3B9/ref=syn_sd"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find("span", "a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float < 100:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="me@parinita.me",
                            msg=f"Subject:Low price alert!\n\n"
                                f"Your pot is now available at the price of {price_as_float}\n"
                                f"Click the link below:\n"
                                f"{url}")


