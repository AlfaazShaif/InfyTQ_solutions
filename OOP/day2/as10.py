class CallDetail:
    def __init__(self, phoneno, called_no, duration, call_type):
        self.phoneno = phoneno
        self.called_no = called_no
        self.duration = duration
        self.call_type = call_type

    # def __str__(self):
    #     return self.phoneno + " " + self.called_no + " " + self.duration + " " + self.call_type

class Util:
    def __init__(self):
        self.list_of_call_objects = None

    def parse_customer(self, list_of_call_string):
        self.list_of_call_objects = []
        for call_log in list_of_call_string:
            call_detail = call_log.split(',')
            call_object = CallDetail(call_detail[0], call_detail[1], call_detail[2], call_detail[3])
            self.list_of_call_objects.append(call_object)
        
        # print(self.list_of_call_objects)
            

call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string = [call,call2,call3]
Util().parse_customer(list_of_call_string)


