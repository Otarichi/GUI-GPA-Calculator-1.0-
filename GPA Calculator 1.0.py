from tkinter import *


class GPAApp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("GPA Calculator by Otarichi ver 1.0")
        self.create_widgets()

    def calculateGPA(self):

        try:
            def calculateSubjGPA(subjectPoint):
                GPA = 0
                if 51 <= subjectPoint <= 60:
                    GPA = 0.5
                    return GPA
                elif 61 <= subjectPoint <= 70:
                    GPA = 1
                    return GPA
                elif 71 <= subjectPoint <= 80:
                    GPA = 2
                    return GPA
                elif 81 <= subjectPoint <= 90:
                    GPA = 3
                    return GPA
                elif 91 <= subjectPoint <= 100:
                    GPA = 4
                    return GPA
                else:
                    return None


            subCounter = 0
            GpaSum = 0
            creditsSum = 0
            if calculateSubjGPA(int(self.subject_1_point_Entry.get())) is not None:
                self.subject_1_GPA = calculateSubjGPA(int(self.subject_1_point_Entry.get())) * int(self.subject_1_credit_Entry.get())
                subCounter += 1
                GpaSum += self.subject_1_GPA
                creditsSum += int(self.subject_1_credit_Entry.get())
            if calculateSubjGPA(int(self.subject_2_point_Entry.get())) is not None:
                self.subject_2_GPA = calculateSubjGPA(int(self.subject_2_point_Entry.get())) * int(self.subject_2_credit_Entry.get())
                subCounter += 1
                GpaSum += self.subject_2_GPA
                creditsSum += int(self.subject_2_credit_Entry.get())
            if calculateSubjGPA(int(self.subject_3_point_Entry.get())) is not None:
                self.subject_3_GPA = calculateSubjGPA(int(self.subject_3_point_Entry.get())) * int(self.subject_3_credit_Entry.get())
                subCounter += 1
                GpaSum += self.subject_3_GPA
                creditsSum += int(self.subject_3_credit_Entry.get())
            if calculateSubjGPA(int(self.subject_4_point_Entry.get())) is not None:
                self.subject_4_GPA = calculateSubjGPA(int(self.subject_4_point_Entry.get())) * int(self.subject_4_credit_Entry.get())
                subCounter += 1
                GpaSum += self.subject_4_GPA
                creditsSum += int(self.subject_4_credit_Entry.get())
            if calculateSubjGPA(int(self.subject_5_point_Entry.get())) is not None:
                self.subject_5_GPA = calculateSubjGPA(int(self.subject_5_point_Entry.get())) * int(self.subject_5_credit_Entry.get())
                subCounter += 1
                GpaSum += self.subject_5_GPA
                creditsSum += int(self.subject_5_credit_Entry.get())
            if calculateSubjGPA(int(self.subject_1_point_Entry.get())) is not None:
                self.subject_6_GPA = calculateSubjGPA(int(self.subject_6_point_Entry.get())) * int(self.subject_6_credit_Entry.get())
                subCounter += 1
                GpaSum += self.subject_6_GPA
                creditsSum += int(self.subject_6_credit_Entry.get())

            if subCounter > 0:
                self.GPA = GpaSum/creditsSum
                self.messageLabel["text"] = "your GPA is {}".format(self.GPA)
            else:
                self.messageLabel["text"] = "you failed all subjects, your GPA is 0"
        except:
            self.messageLabel["text"] = "oops, something is wrong\n" \
                                        "Please fill in all fields!\n " \
                                        "Enter the numbers in credits and points fields!"


    def create_widgets(self):
        self.subject_Names_Label = Label(self.master)
        self.subject_Names_Label["text"] = "Subject name"
        self.subject_Names_Label.grid(row=0, column=1)
        self.subject_credit_Label = Label(self.master)
        self.subject_credit_Label["text"] = "Credits"
        self.subject_credit_Label.grid(row=0, column=2)
        self.subject_point_Label = Label(self.master)
        self.subject_point_Label["text"] = "Point"
        self.subject_point_Label.grid(row=0, column=3)

        self.subject_1_name_Entry = Entry(self.master)
        self.subject_1_name_Entry.grid(row=1, column=1)
        self.subject_1_credit_Entry = Entry(self.master)
        self.subject_1_credit_Entry.grid(row=1, column=2)
        self.subject_1_point_Entry = Entry(self.master)
        self.subject_1_point_Entry.grid(row=1, column=3)

        self.subject_2_name_Entry = Entry(self.master)
        self.subject_2_name_Entry.grid(row=2, column=1)
        self.subject_2_credit_Entry = Entry(self.master)
        self.subject_2_credit_Entry.grid(row=2, column=2)
        self.subject_2_point_Entry = Entry(self.master)
        self.subject_2_point_Entry.grid(row=2, column=3)

        self.subject_3_name_Entry = Entry(self.master)
        self.subject_3_name_Entry.grid(row=3, column=1)
        self.subject_3_credit_Entry = Entry(self.master)
        self.subject_3_credit_Entry.grid(row=3, column=2)
        self.subject_3_point_Entry = Entry(self.master)
        self.subject_3_point_Entry.grid(row=3, column=3)

        self.subject_4_name_Entry = Entry(self.master)
        self.subject_4_name_Entry.grid(row=4, column=1)
        self.subject_4_credit_Entry = Entry(self.master)
        self.subject_4_credit_Entry.grid(row=4, column=2)
        self.subject_4_point_Entry = Entry(self.master)
        self.subject_4_point_Entry.grid(row=4, column=3)

        self.subject_5_name_Entry = Entry(self.master)
        self.subject_5_name_Entry.grid(row=5, column=1)
        self.subject_5_credit_Entry = Entry(self.master)
        self.subject_5_credit_Entry.grid(row=5, column=2)
        self.subject_5_point_Entry = Entry(self.master)
        self.subject_5_point_Entry.grid(row=5, column=3)

        self.subject_6_name_Entry = Entry(self.master)
        self.subject_6_name_Entry.grid(row=6, column=1)
        self.subject_6_credit_Entry = Entry(self.master)
        self.subject_6_credit_Entry.grid(row=6, column=2)
        self.subject_6_point_Entry = Entry(self.master)
        self.subject_6_point_Entry.grid(row=6, column=3)


        self.gpa_calculate_Button = Button(self.master)
        self.gpa_calculate_Button.grid(row=7, column=2)
        self.gpa_calculate_Button["text"] = "Calculate GPA"
        self.gpa_calculate_Button["command"] = self.calculateGPA


        self.messageLabel = Label(self.master)
        self.messageLabel.grid(row=8, column=2)
        self.messageLabel["text"] = "Please fill in all fields!\n " \
                                    "Enter the numbers in credits and points fields!"


root = Tk()
root.geometry("500x220")
App_01 = GPAApp(root)
App_01.mainloop()