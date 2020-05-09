class Employee:

    def __init__(self, first_name, last_name, rate_per_hour):
        self.registered_time = 0
        self.first_name = first_name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour

    def register_time(self, hours):
        self.registered_time = hours

    def pay_salary(self):
        if self.registered_time <= 8:
            to_pay = self.registered_time * self.rate_per_hour
        else:
            to_pay = 8 * self.rate_per_hour + (self.registered_time - 8) * self.rate_per_hour * 2
        self.registered_time = 0
        return to_pay



class TestEmployee:

    def test_init(self):
        employee = Employee("Jan", "Nowak", 100.0)
        assert employee
        assert employee.first_name == "Jan"
        assert employee.last_name == "Nowak"
        assert employee.rate_per_hour == 100.0

    def test_register_time(self):
        employee = Employee("Jan", "Nowak", 100.0)
        employee.register_time(5)
        assert employee.registered_time == 5

    def test_pay_salary(self):
        employee = Employee("Jan", "Nowak", 100.0)
        assert employee.pay_salary() == 0
        employee.register_time(5)
        assert employee.pay_salary() == 500
        assert employee.pay_salary() == 0

    def test_pay_salary_overhours(self):
        employee = Employee("Jan", "Nowak", 100.0)
        employee.register_time(10)
        assert employee.pay_salary() == 1200
        assert employee.pay_salary() == 0