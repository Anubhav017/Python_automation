import softest


# The Util function takes the list iterate over it and match the expected value
class Utils(softest.TestCase):
    # Method for soft assertion on a list
    def assert_list_items(self, clist, value):
        for val in clist:
            print("Value is " + val.text)
            self.soft_assert(self.assertEqual, val.text, value)
            print("Assertion passed")

        self.assert_all()
