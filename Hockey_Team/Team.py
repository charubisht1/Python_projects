# create team class
class Team:
    # defining initialisation method
    def __init__(self, t_id, r_date, name, t_type, fee_paid, fee_amount, cancellation_date):
        self.__t_id = t_id
        self.__r_date = r_date
        self.__name = name
        self.__t_type = t_type
        self.__fee_paid = fee_paid
        self.__fee_amount = fee_amount
        self.__cancellation_date = cancellation_date

    # creating mutator methods
    def set_cancellation_date(self, cancellation_date):
        self.__cancellation_date = cancellation_date

    def set_t_id(self, t_id):
        self.__t_id = t_id

    def set_r_date(self, r_date):
        self.__r_date = r_date

    def set_name(self, name):
        self.__name = name

    def set_t_type(self, t_type):
        self.__t_type = t_type

    def set_fee_paid(self, fee_paid):
        self.__fee_paid = fee_paid

    def set_fee_amount(self, fee_amount):
        self.__fee_amount = fee_amount

    # creating accessor methods
    def get_t_id(self):
        return self.__t_id

    def get_r_date(self):
        return self.__r_date

    def get_name(self):
        return self.__name

    def get_t_type(self):
        return self.__t_type

    def get_fee_paid(self):
        return self.__fee_paid

    def get_fee_amount(self):
        return self.__fee_amount

    def get_cancellation_date(self):
        return self.__cancellation_date

    #
    def __str__(self):
        return 'ID: ' + str(self.__t_id) + '\n' + 'REGISTRATION DATE: ' + str(self.__r_date) + '\n' + 'NAME: ' + \
               self.__name + '\n' + 'TYPE: ' + self.__t_type + '\n' + 'FEE STATUS: ' + str(self.__fee_paid) + '\n' \
               + 'FEE AMOUNT: ' + str(self.__fee_amount) + '\n' + 'CANCELLATION DATE :' + str(self.__cancellation_date)
