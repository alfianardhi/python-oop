class Employee: #class

    """attributes"""
    name = "jon"
    job = "Sales"
    salesWeek = 6

    def hasAchievedTarget(self):
        if self.salesWeek > 5:
            print("target has been achieved")
        else:
            print("target hasn't been achieved")

    @staticmethod
    def getMessage():
        print("Hello message static")
