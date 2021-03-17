# A student has a student number, name, grades assignments in a course and percentage allocation for the course.
# Display the students first initial and last name with their course grade. To calculate the course grade you
# total each assignment mark times the assignment percentage allocation.

class St():
    n = None
    fn = None
    g = None
    p = None

    def __init__(self,d, n, g, p ):
        self.n = d
        self.fn = n
        self.g = g
        self.p = p

    def cg(self):
        g = 1.0
        c = 0
        for m in self.g:
            g = g + (m * self.p[c]/100)
            c = c + 1

        if (22 - g) < 5 :
            sg = "A" + str(int((22 - g) + 1))
        elif ((22 - g) < 7):
            sg = "B" + str(int((22 - g) -4))
        elif ((22 - g) < 10):
            sg = "C" + str(int((22 - g) -7))
        else:
            sg = "H"

        print(g)
        print(self.fn[0:1] + " " + self.fn.split(" ")[1] + " got " + sg)


    def main():
        a = [15,19,18]
        b = [25,25,50]
        st =  St(20012, "Derek Somerville",a,b )
        st.cg();

St.main()