# CoinMarketCap Scraper With MongoDB
A simple scraper for exchanges' information on CoinMarketCap.com. All data can be saved into a remote MongoDB. For example,

![cmc-exchanges-mongodb](https://i.imgur.com/Vtxx1Oo.png)

## Set Up MongoDB Over DigitalOcean Droplet
The installation shell script can be found in this [repo](https://github.com/0xboz/mongodb_installation_script).

## How-to
* Clone this repo
```
git clone https://github.com/0xboz/coinmarketcap_scraper.git
cd coinmarketcap_scraper
```
* Create virtual environment (optional but recommended)
```
python3 -m venv venv
```
* Activate virtual environment (optional but recommended)
```
source venv/source/activate
```
* Install required packages
```
pip install -r requirements.txt
```
* Create a ***config.ini*** in the root directory
> username = *USERNAME*  
> password = *PASSWORD*  
> ip = *SERVER_IP*  
> database_name = CoinMarketCap  
> collection_name = exchanges  
* Run
```
python exchanges.py
```
![terminal-resp](https://i.imgur.com/6oxf4ft.png)
* Update the database  
Re-run the program whenever you would like to update the database.
