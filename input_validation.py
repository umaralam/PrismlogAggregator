"""
input data validation module
"""
from datetime import datetime, timedelta
import logging


class InputValidation:
    """
    input data validation class
    """
    
    def __init__(self, msisdn, input_date):
        self.msisdn = msisdn
        self.input_date = input_date
        self.is_input_valid = False
        self.f_cur_date_time = ""
        self.f_diff_date_time = ""
        self.is_tlog = False

    def validate_msisdn(self):
        """
        Validate msisdn.
        """
        try:
            msisdn = self.msisdn
            special_characters = ['/', '#', '$', '*', '&', '@']
            mdn = "".join(filter(lambda char: char not in special_characters , msisdn))
            logging.info('msisdn:%s and formatted msisdn after removal of special character just for creating out file:%s', self.msisdn, mdn)
            return mdn
        except Exception as error:
            logging.error('Invalid msisdn')
            raise

    def validate_date(self):
        """
        Validate date.
        """
        try:
            datetime.strptime(self.input_date, "%Y%m%d")
            self.is_input_valid = True
            logging.debug('Transaction date entered is valid : %s', self.input_date)
            return self.input_date
        except Exception as error:
            logging.error('Transaction date %s entered is of invalid format. The format should be "yyyymmdd".', self.input_date)
            self.is_input_valid = False
            raise
        
    def validate_timedtdata(self, timedtdata):
        """
        Validate tdata time.
        """
        try:
            tdata, stDelta = timedtdata.split("=")
            dt = int(stDelta)
            logging.info('tdata param: %s and time delta: %s', tdata, stDelta)
            cur_date_time = datetime.now() 
            diff_date_time = cur_date_time - timedelta(minutes=dt)
    
            self.f_cur_date_time = datetime.strftime(cur_date_time, "%Y-%m-%d %H:%M:%S")
            self.f_diff_date_time = datetime.strftime(diff_date_time, "%Y-%m-%d %H:%M:%S")
            logging.info('formatted current datetime %s - time delta %s = formatted diff datetime %s ', self.f_cur_date_time, dt, self.f_diff_date_time)
            self.is_tlog = True
        except Exception as error:
            logging.error('Invalid argument: %s".', timedtdata)
            self.is_input_valid = False
            raise
