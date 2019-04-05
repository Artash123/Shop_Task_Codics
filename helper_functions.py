class HelperFuncs:

    def input_int(self, massage, min_length, max_length):
        while True:
            input_value = input(massage)
            if input_value.isdigit():
                input_value = int(input_value)
                if min_length <= input_value <= max_length:
                    return input_value
            print("Please enter number between {} and {}".format(min_length, max_length))

    def input_float(self, massage, min_length, max_length):
        while True:
            input_value = input(massage)
            if len(input_value) > 5:
                print('Maximum 5 digit')
                continue
            try:
                float(input_value)
                input_value = float(input_value)
                if min_length <= input_value <= max_length:
                    return input_value
                print("Please enter number between {} and {} g".format(min_length, max_length))
            except ValueError:
                print("Please enter number between {} and {}".format(min_length, max_length))

    def check_string(self, massage, value, min_length, max_length):
        while True:
            input_value = input(massage)
            if min_length <= len(input_value) <= max_length:
                input_value = input_value
                return input_value
            print("{} must be no shorter {} letters and no longer {} letter".format(value, min_length, max_length))

