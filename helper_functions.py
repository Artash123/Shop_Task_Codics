class HelperFuncs:

    def __init__(self):
        self.errors = 0

    def input_int(self, massage, min_length, max_length):
        while True:
            self.check_errors()
            input_value = input(massage)
            if input_value.isdigit():
                input_value = int(input_value)
                if min_length <= input_value <= max_length:
                    return input_value
            self.errors += 1
            print("Please enter number between {} and {}".format(min, max))

    def check_string(self, massage, value, min_length, max_length):
        while True:
            self.check_errors()
            input_value = input(massage)
            if min_length <= len(input_value) <= max_length:
                input_value = input_value
                return input_value
            self.errors += 1
            print("{} must be no shorter {} letters and no longer {} letter".format(value, min, max))

    def check_errors(self):
        if self.errors == 3:
            print("you have 3 errors")
