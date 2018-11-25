import sys

import pkg_resources

from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import (QAction, QGroupBox, QApplication, QDesktopWidget, QDialog, QFileDialog,
                             QHBoxLayout, QLabel, QMainWindow, QToolBar, QVBoxLayout, QMenuBar, QWidget,
                               QGridLayout, QVBoxLayout, QPushButton, QLineEdit, QTableWidget, QTableView,
                               QFormLayout, QCalendarWidget, QRadioButton, QComboBox)


class DateOfBirthWidget(QDialog):

    def __init__(self, parent=None):
        super(DateOfBirthWidget, self).__init__(parent)
        vlayout = QVBoxLayout()
        self.calendar = QCalendarWidget()
        vlayout.addWidget(self.calendar)

        self.setLayout(vlayout)

class DateOfBirthLineEdit(QLineEdit):

    def __init__(self, parent=None):
        super(DateOfBirthLineEdit, self).__init__(parent)

class NameLineEdit(QLineEdit):

    def __init__(self, parent=None):
        super(NameLineEdit, self).__init__(parent)

class LastNameLineEdit(QLineEdit):

    def __init__(self, parent=None):
        super(LastNameLineEdit, self).__init__(parent)

class EmailLineEdit(QLineEdit):

    def __init__(self, parent=None):
        super(EmailLineEdit, self).__init__(parent)


class NewInsuranceTypeDialog(QDialog):

    def __init__(self, parent=None):
        super(NewInsuranceTypeDialog, self).__init__(parent)

        insuranceNameLabel = QLabel(self.tr("&Insurance Name:"))
        insuranceNameLabel.setBuddy(QLineEdit())

        insuranceDetailLabel = QLabel(self.tr("&Insurance Detail:"))
        insuranceDetailLabel.setBuddy(LastNameLineEdit())

        gridLayout = QGridLayout()
        gridLayout.addWidget(insuranceNameLabel, 0, 0)
        gridLayout.addWidget(QLineEdit(), 0, 1)

        gridLayout.addWidget(insuranceDetailLabel, 1, 0)
        gridLayout.addWidget(QLineEdit(), 1, 1)

        saveButton = QPushButton("Save")
        saveButton.setStyleSheet("color: #fff; background-color: grey;");

        self.setLayout(gridLayout)


class EmployeeCommissionDialog(QDialog):

    def __init__(self, parent=None):
        super(EmployeeCommissionDialog, self).__init__(parent)


        amount_of_premium = QLabel(self.tr("&Amount Of Premium:"))
        amount_of_premium.setBuddy(QLineEdit())

        pay_commission_amount  = QLabel(self.tr("&Pay Commission:"))
        pay_commission_amount.setBuddy(LastNameLineEdit())

        how_many_times = QLabel(self.tr("&How many Times?:"))
        how_many_times.setBuddy(LastNameLineEdit())

        renew_date = QLabel(self.tr("&Renew Date?:"))
        renew_date.setBuddy(LastNameLineEdit())

        override_commissions = QLabel(self.tr("&Override Commission:"))
        override_commissions.setBuddy(LastNameLineEdit())

        calculateButton = QPushButton(self.tr("&Calculate"))

        total_payable_commission = QLabel(self.tr("&Total Payable Commission?:"))
        override_commissions.setBuddy(LastNameLineEdit())

        gridLayout = QGridLayout()
        gridLayout.addWidget(amount_of_premium, 0, 0)
        gridLayout.addWidget(QLineEdit(), 0, 1)

        gridLayout.addWidget(pay_commission_amount, 1, 0)
        gridLayout.addWidget(QLineEdit(), 1, 1)

        gridLayout.addWidget(how_many_times, 2, 0)
        gridLayout.addWidget(QLineEdit(), 2, 1)

        gridLayout.addWidget(renew_date, 3, 0)
        gridLayout.addWidget(QLineEdit(), 3, 1)

        gridLayout.addWidget(override_commissions, 4, 0)
        gridLayout.addWidget(QLineEdit(), 4, 1)

        gridLayout.addWidget(calculateButton, 5, 1)

        gridLayout.addWidget(total_payable_commission, 6, 0)
        gridLayout.addWidget(QLineEdit(), 6, 1)

        saveButton = QPushButton("Save")
        saveButton.setStyleSheet("color: #fff; background-color: grey;");

        self.setLayout(gridLayout)



class EmployeeFormDialog(QDialog):

    def __init__(self, parent=None):
        super(EmployeeFormDialog, self).__init__(parent)

        nameLabel = QLabel(self.tr("&First Name(s):"))
        nameLabel.setBuddy(NameLineEdit())

        lastNameLabel = QLabel(self.tr("&Last Name:"))
        lastNameLabel.setBuddy(LastNameLineEdit())

        dateOfBirthLabel = QLabel(self.tr("&Date of Birth:"))
        dateOfBirthLabel.setBuddy(DateOfBirthLineEdit())

        calendarButton = QPushButton()
        calendarButton.clicked.connect(self.openCalendar)
        icon = QIcon()
        icon.addPixmap(QPixmap("./images/calendar-icon.png"), QIcon.Normal, QIcon.Off)
        calendarButton.setIcon(icon);

        emailLabel = QLabel(self.tr("&Email:"))
        emailLabel.setBuddy(EmailLineEdit())

        genderLabel = QLabel(self.tr("&Gender:"))
        male = QRadioButton("Male")
        female = QRadioButton("Female")
        genderLabel.setBuddy(male)
        genderLabel.setBuddy(female)

        house_no = QLabel(self.tr("&House No/House Name:"))
        house_no.setBuddy(QLineEdit())
        stree_name = QLabel(self.tr("&Street Name:"))
        stree_name.setBuddy(QLineEdit())
        town_name = QLabel(self.tr("&Town Name:"))
        town_name.setBuddy(QLineEdit())
        county = QLabel(self.tr("&County:"))
        county.setBuddy(QLineEdit())
        country = QLabel(self.tr("&Country:"))
        country.setBuddy(QComboBox())

        phone_no = QLabel(self.tr("&Phone Number:"))
        phone_no.setBuddy(QLineEdit())

        saveButton = QPushButton("Save")
        saveButton.setStyleSheet("color: #fff; background-color: grey;");

        gridLayout = QGridLayout()
        gridLayout.addWidget(nameLabel, 0, 0)
        gridLayout.addWidget(NameLineEdit(), 0, 1)
        gridLayout.addWidget(lastNameLabel, 1, 0)
        gridLayout.addWidget(LastNameLineEdit(), 1, 1)
        gridLayout.addWidget(dateOfBirthLabel, 2, 0)
        gridLayout.addWidget(DateOfBirthLineEdit(), 2, 1)
        gridLayout.addWidget(calendarButton, 2, 2)
        gridLayout.addWidget(emailLabel, 3, 0)
        gridLayout.addWidget(EmailLineEdit(), 3, 1)
        gridLayout.addWidget(genderLabel, 4, 0)
        gridLayout.addWidget(male, 4, 1)
        gridLayout.addWidget(female, 4, 2)

        #Address
        gridLayout.addWidget(house_no, 5, 0)
        gridLayout.addWidget(QLineEdit(), 5, 1)

        #Address
        gridLayout.addWidget(stree_name, 6, 0)
        gridLayout.addWidget(QLineEdit(), 6, 1)

        #Address
        gridLayout.addWidget(town_name, 7, 0)
        gridLayout.addWidget(QLineEdit(), 7, 1)

        #Address
        gridLayout.addWidget(county, 8, 0)
        gridLayout.addWidget(QLineEdit(), 8, 1)

        #Address
        gridLayout.addWidget(country, 9, 0)
        gridLayout.addWidget(QComboBox(), 9, 1)

        # Address
        gridLayout.addWidget(phone_no, 10, 0)
        gridLayout.addWidget(QLineEdit(), 10, 1)

        gridLayout.addWidget(saveButton, 11, 1)

        self.setLayout(gridLayout)

    def openCalendar(self):
        dob = DateOfBirthWidget()
        dob.exec_()


class ApplicationWindow(QWidget):
    """Create the main window that stores all of the widgets necessary for the application."""

    def __init__(self, parent=None):
        """Initialize the components of the main window."""
        super(ApplicationWindow, self).__init__()

        menuBar = QMenuBar()
        act = menuBar.addAction("File")

        gridLayout = QGridLayout()

        gridLayout.addWidget(self.create_first_box(), 0, 0)
        gridLayout.addWidget(self.create_search_box(), 1, 0)

        self.setFixedWidth(1000)
        self.setLayout(gridLayout)


    def create_first_box(self):
        hlayout = QHBoxLayout()

        # New Employee
        employee = QPushButton("New Employee", self)
        employee.setStyleSheet("color: #fff; background-color: grey;");
        employee.clicked.connect(lambda: self.newEmployeeForm())
        hlayout.addWidget(employee)

        # New Insurance Type
        new_insurance_type = QPushButton("New Insurance Type", self)
        new_insurance_type.setStyleSheet("color: #fff; background-color: grey;");
        new_insurance_type.clicked.connect(lambda: self.newInsuranceType())
        hlayout.addWidget(new_insurance_type)

        # Reports
        reports = QPushButton("Reports", self)
        reports.setStyleSheet("color: #fff; background-color: grey;");
        reports.clicked.connect(lambda: self.newEmployeeForm())
        hlayout.addWidget(reports)

        group_box = QGroupBox("New")
        group_box.setLayout(hlayout)
        hlayout.addStretch(1)

        hlayout.setAlignment(Qt.AlignTop)
        return group_box

    def create_search_box(self):
        gridLayout = QGridLayout()

        hlayout = QHBoxLayout()

        searchTextBox = QLineEdit()
        hlayout.addWidget(searchTextBox)

        # Search Employee
        search = QPushButton("Search")
        search.clicked.connect(lambda: self.newEmployeeForm())
        hlayout.addWidget(search)

        employee_commission = QPushButton("Add Employee commission")
        employee_commission.setEnabled(True)
        employee_commission.clicked.connect(lambda: self.addEmployeeCommission())
        hlayout.addWidget(employee_commission)

        name = QLabel("Abraham - ")
        hlayout.addWidget(name)

        name = QLabel("SAFELIFE8765")
        hlayout.addWidget(name)

        tableWidget = QTableWidget()
        tableWidget.setRowCount(20)
        self.horizontal_header = ["Id", "Insurance Type", "Customer", "Start Date", "End Date", "Payable Commission", "Override Commission",
                                  "Month Left to Pay"]
        tableWidget.setColumnCount(len(self.horizontal_header))
        tableWidget.setHorizontalHeaderLabels(self.horizontal_header)
        tableWidget.setColumnWidth(1, 100)

        gridLayout.addLayout(hlayout, 0, 0)
        gridLayout.addWidget(tableWidget, 1, 0)

        new_group_box = QGroupBox("Search Commission Statements")
        new_group_box.setLayout(gridLayout)

        return new_group_box

    def newEmployeeForm(self):
        EmployeeFormDialog().exec_()

    def newInsuranceType(self):
        NewInsuranceTypeDialog().exec_()

    def addEmployeeCommission(self):
        EmployeeCommissionDialog().exec_()



def main():
    application = QApplication(sys.argv)
    window = ApplicationWindow()
    desktop = QDesktopWidget().availableGeometry()
    width = desktop.width()
    height = desktop.height()
    window.show()
    sys.exit(application.exec_())

if __name__ == "__main__":
    main()