import requests
import bs4
import re

list_url = [
    "https://www.chittorgarh.com/ipo/vedant-fashions-ipo/1217/",
    "https://www.chittorgarh.com/ipo/uma-exports-ipo/1235/",
    "https://www.chittorgarh.com/ipo/ruchi-soya-fpo/1118/",
    "https://www.chittorgarh.com/ipo/veranda-learning-ipo/1236/",
    "https://www.chittorgarh.com/ipo/campus-activewear-ipo/1249/",
    "https://www.chittorgarh.com/ipo/rainbow-children-medicare-ipo/1250/",
]


def remove_rupee_sign(issue_price):
    """Removes the Rupee sign from the issue price."""
    return issue_price.replace("₹", "")


def remove_per_share(issue_price):
    """Removes the 'per share' text from the issue price."""
    return issue_price.split(" ")[0]


def formate_date(user_date):
    match = re.match(r"(\w+), (.+)", user_date)

    if match:
        day_of_week = match.group(1)
        date = match.group(2)

        # Combine the extracted parts
        combined_date = f"{date}"

    else:
        print("String format doesn't match expected pattern.")
    return combined_date


def request_page(url):
    response = requests.get(url)
    page = bs4.BeautifulSoup(response.content, "html.parser")
    # print(page.encode("utf-8"))
    return page


def get_date(page):
    # for date
    date = page.select(
        "#main > div.row.pt-2.mt-2 > div:nth-child(4) > div > div:nth-child(2) > div:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(2)"
    )
    if date:
        date = formate_date(date[0].text)
        print(date)
    return date


def get_listing_price(page):
    listing_price = page.select(
        "#main > div.row.pt-2.mt-2 > div:nth-child(12) > div:nth-child(2) > div:nth-child(2) > div > div.card-body > div > div:nth-child(2) > table > tbody > tr:nth-child(2) > td"
    )
    # print(str(listing_price))
    if listing_price:
        listing_price = listing_price[0].text
        print(listing_price)
    return listing_price


def get_subscription(page):
    subscription = page.select(
        "#main > div:nth-child(2) > div > div:nth-child(4) > div > table > tbody > tr:nth-child(6) > td:nth-child(2) > b"
    )
    if not subscription:
        subscription = page.select(
            "#main > div:nth-child(2) > div > div:nth-child(4) > div > table > tbody > tr:nth-child(8) > td:nth-child(2) > b"
        )
    if not subscription:
        subscription = page.select(
            "#main > div:nth-child(2) > div > div:nth-child(4) > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > b"
        )
    if subscription:
        subscription = subscription[0].text
        print(subscription)
    return subscription


def get_type(page):
    ipo_type = page.select("#faq_ipo_detail_1 > div > p:nth-child(1) > b")
    # print(ipo_type)
    if ipo_type:
        ipo_type = ipo_type[0].text
        if "main-board" in ipo_type:
            ipo_type = "MAINBOARD IPO"
        elif "SME" in ipo_type:
            ipo_type = "SME IPO"
    print(ipo_type)
    return ipo_type


def get_issue_price(page):
    issue_price = page.select(
        "#main > div.row.pt-2.mt-2 > div:nth-child(12) > div:nth-child(2) > div:nth-child(1) > div > div.card-body > table > tbody > tr:nth-child(5) > td:nth-child(2)"
    )
    # print(issue_price.encode("utf-8"))
    if issue_price:
        issue_price = issue_price[0].text
        issue_price = remove_per_share(remove_rupee_sign(issue_price))
        print(issue_price)
    return issue_price


def get_data(url):
    page = request_page(url)
    result = get_issue_price(page)
    # result = get_listing_price(page)
    # result = get_date(page)
    # result = get_type(page)
    # result = get_subscription(page)
    if not result:
        result = ""
        print(url)
        return url
    return result


def main():
    """Writes the final issue price to a text file."""
    with open("issue_price.txt", "w", encoding="utf-8") as f:
        for url in list_url:
            result = get_data(url)
            f.write(str(result) + "\n")


if __name__ == "__main__":
    main()
    # issue_price = get_issue_price()
    # write_to_file(issue_price)
