from django.contrib.auth.mixins import UserPassesTestMixin


class StaffTest(UserPassesTestMixin):
    """Lo scopo di questo mixin è fare in modo che solo uno staff
    possa creare nuove sezioni.
    """

    def test_func(self):
        return self.request.user.is_staff
