import datetime
import sys
sys.path.append('/Users/aadhav/TradingHistoricalDataAnalysis/')
from defaults.dates import weekday
from enum import IntFlag, Flag


class calender():

    weekend = {weekday.SATURDAY, weekday.SUNDAY}


    def __init__(self) -> None:
        pass


    @staticmethod
    def is_weekend(date: datetime) -> bool:
        '''
        params:
        date: get the date to verfiy

        return: True | False
                return true if the date is Saturday or Sunday else Return False     
        '''
        return weekday(date.weekday()) in calender.weekend

        


if __name__ == "__main__":
    """
    block is to test the functionality of each module
    """
    is_weekend = calender.is_weekend(datetime.datetime.now() + datetime.timedelta(days=1))
    print(is_weekend)


    