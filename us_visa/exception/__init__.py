import os
import sys

def error_msg_details(error, error_details:sys):
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_msg = f"Error occured python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"
 
    return error_msg

class USvisaException(Exception):
    def __init__(self, error_msg, error_details):
        """
        :param error_message: error message in string format
        """
        super().__init__(error_msg)
        self.error_msg = error_msg_details(
            error_msg, error_details=error_details
        )

    def __str__(self):
        return self.error_msg
