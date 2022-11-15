import requests
import sys
import pandas as pd
from pandas import DataFrame

sys.path.append('/Users/aadhav/TradingHistoricalDataAnalysis/')

from Downloader.config.calender import calender
from datetime import datetime, timedelta
import csv
import os

class downloadArchiveStockData():

    nse_base_url = "https://archives.nseindia.com/products/content/"
    full_bhav_file_name = "sec_bhavdata_full_"
    download_csv = '/Users/aadhav/TradingHistoricalDataAnalysis/incoming'

    def __init__() -> None:
        pass


    @staticmethod
    def exception_handling(name: str, err: Exception) -> None:
        print(f'{name} : { err= } : {type(err)=}')



    @staticmethod
    def download_bhavcpy_name(date: datetime) -> str:
        """
        sample file name should be return - sec_bhavdata_full_11112022.csv
        """
        return f'{downloadArchiveStockData.full_bhav_file_name}{date.strftime("%d%m%Y")}.csv'


    @staticmethod
    def downloadUrlBuilder(date: datetime) -> str:
        """
        return the downloadable url
        """
        name = downloadArchiveStockData.download_bhavcpy_name(date)
        return f'{downloadArchiveStockData.nse_base_url}{name}'


    @staticmethod
    def write_csv(data: DataFrame, date: datetime) -> bool:
        try:
            file_name = f'{date.day}{date.month}{date.year}.csv'
            full_path = os.path.join(downloadArchiveStockData.download_csv, file_name)
            """
            Write the downloaded to csv file
            """
            data.to_csv(full_path)
            return True
        except Exception as err:
            downloadArchiveStockData.exception_handling(downloadArchiveStockData.write_csv.__name__, err)
            return False



    @classmethod
    def download_csv_bhavcopy(cls, date: datetime) -> bool :
        """
        download the csv from the url
        return : True or False , method will return whether download has been completed successfully
        """
        if not calender.is_weekend(date):
            try:
                data = pd.read_csv(cls.downloadUrlBuilder(date))
                is_writtentocsv = downloadArchiveStockData.write_csv(data, date)             
            except Exception as err:
                 downloadArchiveStockData.exception_handling(downloadArchiveStockData.download_csv_bhavcopy.__name__)
        else:
            print("Provided date is WeekEnd")



if __name__ == "__main__":   
    days=10
    while(days):
        date = datetime.now() - timedelta(days=days)
        downloadArchiveStockData.download_csv_bhavcopy(date)
        days = days - 1


    



