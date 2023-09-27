def get_issue_price2(url):
    # url = "https://www.chittorgarh.com/ipo/ruchi-soya-fpo/1118/"

    # print(page.encode("utf-8"))
    page = request_page(url)
    # for issue price
    # issue_price_tag = page.select(
    #     "#main > div.row.pt-2.mt-2 > div:nth-child(11) > div:nth-child(2) > div:nth-child(1) > div > div.card-body > table > tbody > tr:nth-child(5) > td:nth-child(2)"
    #     or "#main > div.row.pt-2.mt-2 > div:nth-child(12) > div:nth-child(2) > div:nth-child(1) > div > div.card-body > table > tbody > tr:nth-child(5) > td:nth-child(2)"
    # )
    # for date
    # issue_price_tag = page.select(
    #     "#main > div.row.pt-2.mt-2 > div:nth-child(4) > div > div:nth-child(2) > div:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(2)"
    # )
    # for listing price
    # issue_price_tag = page.select(
    #     "#main > div.row.pt-2.mt-2 > div:nth-child(11) > div:nth-child(2) > div:nth-child(2) > div > div.card-body > div > div:nth-child(2) > table > tbody > tr:nth-child(2) > td"
    # )
    # for subscription
    # issue_price_tag = page.select(
    #     "#main > div:nth-child(2) > div > div:nth-child(4) > div > table > tbody > tr:nth-child(6) > td:nth-child(2) > b"
    # )
    # if not issue_price_tag:
    #     issue_price_tag = page.select(
    #         "#main > div:nth-child(2) > div > div:nth-child(4) > div > table > tbody > tr:nth-child(8) > td:nth-child(2) > b"
    #     )
    # if not issue_price_tag:
    #     issue_price_tag = page.select(
    #         "#main > div:nth-child(2) > div > div:nth-child(4) > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > b"
    #     )

    # for type
    issue_price_tag = page.select("#faq_ipo_detail_1 > div > p:nth-child(1) > b")

    # print(issue_price_tag)
    if issue_price_tag:
        issue_price = issue_price_tag[0].text
        # if "main-board" in issue_price:
        #     issue_price = "MAINBOARD IPO"
        # elif "SME" in issue_price:
        #     issue_price = "SME IPO"
    else:
        issue_price = ""
        print(url)
        return url
    # issue_price = remove_per_share(remove_rupee_sign(issue_price))
    # issue_price = for_date(issue_price)
    print(issue_price)
    return issue_price
