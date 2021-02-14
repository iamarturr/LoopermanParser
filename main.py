from bs4 import BeautifulSoup
import requests


def main(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.text, features="html.parser")

    r = soup.find_all("div", class_="player-wrapper")[0]
    r = str(r).split("\n")[0]

    print(r.split("rel")[1].replace('=', "").replace('"', "").replace(" >", ""))


if __name__ == "__main__":
    url = "https://www.looperman.com/loops/detail/209709/nick-mira-x-foreigngotem-type-melody-150bpm-hip-hop-electric-guitar-loop"
    main(url)
