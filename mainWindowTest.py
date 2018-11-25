import enum
import sys

from PySide2 import QtGui, QtWidgets, QtCore

def make_printer(num):

    def print_value(*args, **kwargs):
        print(num)
    return print_value

def print_button_state(signal):
    signal_text = 'on' if signal else 'off'
    print('Button is now ' + signal_text)


class InsuranceTypeEnum():
    LIFE_INSURANCE = 'Life Insurance'
    CRITICAL_SERIOUS = 'Critical / Serious'
    INCOME_PROTECTION = 'Income Protection'
    BUILDING = 'Building'
    BUSINESS = 'Business'
    SHOP = 'Shop'
    LIABILITY = 'Liability'
    PRIVATE_MEDICAL = 'Private Medical'

class PremiumTypeEnum():
    GUARANTEED = 'GUARANTEED'
    VARIABLE = 'VARIABLE'

class PlanTypeEnum():
    FIRST_DEATH = 'FIRST_DEATH'
    SEPERATE = 'SEPERATE'

class HeightUnitEnum():
    INCHES = 'inches'
    CENTIMETER = 'cm'
    METER = 'm'
    FEET = 'ft'

class WeightUnitEnum():
    KILOGRAM = 'kg'
    POUNDS = 'lbs'

class NewClientFormDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(NewClientFormDialog, self).__init__(parent)

        gridLayout = QtWidgets.QGridLayout()

        gridLayout.addWidget(self.createReference(), 0, 0)
        gridLayout.addWidget(self.createCustomerDetails(), 1, 0)
        gridLayout.addWidget(self.createInsuranceType(), 2, 0)
        gridLayout.addWidget(self.createLifeInsuranceCover(), 3, 0)

        gridLayout.setAlignment(QtCore.Qt.AlignLeft)

        self.setWindowTitle("New Client")

        self.setLayout(gridLayout)

    def createLifeInsuranceCover(self):

        planTypeLabel = QtWidgets.QLabel(self.tr("&Plan Type:"))
        planTypeLabel.setBuddy(QtWidgets.QComboBox())
        self.planType = QtWidgets.QComboBox()
        self.planType.addItem(PlanTypeEnum.FIRST_DEATH)
        self.planType.addItem(PlanTypeEnum.SEPERATE)

        termCoverLabel = QtWidgets.QLabel(self.tr("&Term Of Cover:"))
        termCoverLabel.setBuddy(QtWidgets.QLineEdit())
        self.termCover = QtWidgets.QLineEdit()

        occupationLabel = QtWidgets.QLabel(self.tr("&Occupation:"))
        occupationLabel.setBuddy(QtWidgets.QLineEdit())
        self.occupation = QtWidgets.QLineEdit()

        dutyLabel = QtWidgets.QLabel(self.tr("&Duty:"))
        dutyLabel.setBuddy(QtWidgets.QLineEdit())
        self.duty = QtWidgets.QLineEdit()

        residencyLabel = QtWidgets.QLabel(self.tr("&Residency:"))
        residencyLabel.setBuddy(QtWidgets.QLineEdit())
        self.residency = QtWidgets.QLineEdit()

        smokerLabel = QtWidgets.QLabel(self.tr("&Smoker:"))
        smokerLabel.setBuddy(QtWidgets.QRadioButton())
        self.smoker_yes = QtWidgets.QRadioButton("Yes")
        self.smoker_no = QtWidgets.QRadioButton("No")

        heightLabel = QtWidgets.QLabel(self.tr("&Height:"))
        heightLabel.setBuddy(QtWidgets.QLineEdit())
        self.height = QtWidgets.QLineEdit()
        self.heightUnits = QtWidgets.QComboBox()
        self.heightUnits.addItem(HeightUnitEnum.CENTIMETER)
        self.heightUnits.addItem(HeightUnitEnum.FEET)
        self.heightUnits.addItem(HeightUnitEnum.INCHES)
        self.heightUnits.addItem(HeightUnitEnum.METER)

        weightLabel = QtWidgets.QLabel(self.tr("&Weight:"))
        weightLabel.setBuddy(QtWidgets.QLineEdit())
        self.weight = QtWidgets.QLineEdit()
        self.weightUnits = QtWidgets.QComboBox()
        self.weightUnits.addItem(WeightUnitEnum.KILOGRAM)
        self.weightUnits.addItem(WeightUnitEnum.POUNDS)


        lifeCoverInsuranceGroupBox = QtWidgets.QGroupBox("Life Cover Insurance")
        lifeInsuranceCoverGridLayout = QtWidgets.QGridLayout()

        lifeInsuranceCoverGridLayout.addWidget(planTypeLabel, 0, 0)
        lifeInsuranceCoverGridLayout.addWidget(self.planType, 0, 1)
        lifeInsuranceCoverGridLayout.addWidget(termCoverLabel, 0, 2)
        lifeInsuranceCoverGridLayout.addWidget(self.termCover, 0, 3)
        lifeInsuranceCoverGridLayout.addWidget(occupationLabel, 0, 4)
        lifeInsuranceCoverGridLayout.addWidget(self.occupation, 0, 5)
        lifeInsuranceCoverGridLayout.addWidget(dutyLabel, 1, 0)
        lifeInsuranceCoverGridLayout.addWidget(self.duty, 1, 1)
        lifeInsuranceCoverGridLayout.addWidget(residencyLabel, 1, 2)
        lifeInsuranceCoverGridLayout.addWidget(self.residency, 1, 3)
        lifeInsuranceCoverGridLayout.addWidget(smokerLabel, 2, 0)
        lifeInsuranceCoverGridLayout.addWidget(self.smoker_yes, 2, 1)
        lifeInsuranceCoverGridLayout.addWidget(self.smoker_no, 2, 2)
        lifeInsuranceCoverGridLayout.addWidget(heightLabel, 2, 3)
        lifeInsuranceCoverGridLayout.addWidget(self.height, 2, 4)
        lifeInsuranceCoverGridLayout.addWidget(self.heightUnits, 2, 5)
        lifeInsuranceCoverGridLayout.addWidget(weightLabel, 3, 0)
        lifeInsuranceCoverGridLayout.addWidget(self.weight, 3, 1)
        lifeInsuranceCoverGridLayout.addWidget(self.weightUnits, 3, 2)

        lifeCoverInsuranceGroupBox.setLayout(lifeInsuranceCoverGridLayout)

        return lifeCoverInsuranceGroupBox

    def createInsuranceType(self):
        insuranceTypeGridLayout = QtWidgets.QGridLayout()

        insuranceTypeLabel = QtWidgets.QLabel(self.tr("&Insurance Type:"))
        insuranceTypeLabel.setBuddy(QtWidgets.QComboBox())
        self.insuranceType = QtWidgets.QComboBox()
        self.insuranceType.addItem(InsuranceTypeEnum.LIFE_INSURANCE)
        self.insuranceType.addItem(InsuranceTypeEnum.CRITICAL_SERIOUS)
        self.insuranceType.addItem(InsuranceTypeEnum.INCOME_PROTECTION)
        self.insuranceType.addItem(InsuranceTypeEnum.BUILDING)
        self.insuranceType.addItem(InsuranceTypeEnum.BUSINESS)
        self.insuranceType.addItem(InsuranceTypeEnum.SHOP)
        self.insuranceType.addItem(InsuranceTypeEnum.LIABILITY)
        self.insuranceType.addItem(InsuranceTypeEnum.PRIVATE_MEDICAL)

        coverAmountLabel = QtWidgets.QLabel(self.tr("&Cover Amount:"))
        coverAmountLabel.setBuddy(QtWidgets.QLineEdit())
        self.coverAmount = QtWidgets.QLineEdit("£")

        premiumLabel = QtWidgets.QLabel(self.tr("&Premium:"))
        premiumLabel.setBuddy(QtWidgets.QLineEdit())
        self.premium = QtWidgets.QLineEdit()

        premiumTypeLabel = QtWidgets.QLabel(self.tr("&Premium Type:"))
        premiumTypeLabel.setBuddy(QtWidgets.QLineEdit())
        self.premiumType = QtWidgets.QComboBox()
        self.premiumType.addItem(PremiumTypeEnum.GUARANTEED)
        self.premiumType.addItem(PremiumTypeEnum.VARIABLE)

        insuranceTypeGroupBox = QtWidgets.QGroupBox("Insurance Type")

        insuranceTypeGridLayout.addWidget(insuranceTypeLabel, 0, 0)
        insuranceTypeGridLayout.addWidget(self.insuranceType, 0, 1)
        insuranceTypeGridLayout.addWidget(coverAmountLabel, 0, 2)
        insuranceTypeGridLayout.addWidget(self.coverAmount, 0, 3)
        insuranceTypeGridLayout.addWidget(premiumLabel, 0, 4)
        insuranceTypeGridLayout.addWidget(self.premium, 0, 5)
        insuranceTypeGridLayout.addWidget(premiumTypeLabel, 0, 6)
        insuranceTypeGridLayout.addWidget(self.premiumType, 0, 7)

        insuranceTypeGroupBox.setLayout(insuranceTypeGridLayout)

        return insuranceTypeGroupBox

    def createCustomerDetails(self):

        customerGridLayout = QtWidgets.QGridLayout()

        nameLabel = QtWidgets.QLabel(self.tr("&First Name(s):"))
        nameLabel.setBuddy(QtWidgets.QLineEdit())

        lastNameLabel = QtWidgets.QLabel(self.tr("&Last Name:"))
        lastNameLabel.setBuddy(QtWidgets.QLineEdit())

        emailAddress = QtWidgets.QLabel(self.tr("&Email Address:"))
        emailAddress.setBuddy(QtWidgets.QLineEdit())

        dob = QtWidgets.QLabel(self.tr("&Date Of Birth:"))
        dob.setBuddy(QtWidgets.QLineEdit())

        calendarButton = QtWidgets.QPushButton()

        calendarButton.clicked.connect(self.openCalendar)
        icon = QtGui.QIcon()

        icon.addPixmap(QtGui.QPixmap("./images/calendar-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        calendarButton.setFixedHeight(26)
        calendarButton.setFixedWidth(28)
        calendarButton.setIcon(icon);

        houseNo = QtWidgets.QLabel(self.tr("&House No/ House Name:"))
        houseNo.setBuddy(QtWidgets.QLineEdit())

        streetName = QtWidgets.QLabel(self.tr("&Street Name:"))
        streetName.setBuddy(QtWidgets.QLineEdit())

        county = QtWidgets.QLabel(self.tr("&County:"))
        county.setBuddy(QtWidgets.QLineEdit())

        city = QtWidgets.QLabel(self.tr("&City:"))
        city.setBuddy(QtWidgets.QLineEdit())

        postcode = QtWidgets.QLabel(self.tr("&Postcode:"))
        postcode.setBuddy(QtWidgets.QLineEdit())

        country = QtWidgets.QLabel(self.tr("&Country:"))
        country.setBuddy(QtWidgets.QLineEdit())

        gender = QtWidgets.QLabel(self.tr("&Gender:"))
        gender.setBuddy(QtWidgets.QRadioButton())

        smoker = QtWidgets.QLabel(self.tr("&Smoker:"))
        smoker.setBuddy(QtWidgets.QRadioButton())

        employed = QtWidgets.QLabel(self.tr("&Employed:"))
        employed.setBuddy(QtWidgets.QRadioButton())

        policy_type = QtWidgets.QLabel(self.tr("&Policy Type:"))
        policy_type.setBuddy(QtWidgets.QRadioButton())

        customerGroupBox = QtWidgets.QGroupBox("Customer Details")

        customerGridLayout.addWidget(nameLabel, 0, 0)
        customerGridLayout.addWidget(QtWidgets.QLineEdit(), 0, 1)

        customerGridLayout.addWidget(lastNameLabel, 0, 2)
        customerGridLayout.addWidget(QtWidgets.QLineEdit(), 0, 3)

        customerGridLayout.addWidget(emailAddress, 0, 4)
        customerGridLayout.addWidget(QtWidgets.QLineEdit(), 0, 5)

        customerGridLayout.addWidget(dob, 0, 6)
        customerGridLayout.addWidget(QtWidgets.QLineEdit(), 0, 7)

        customerGridLayout.addWidget(calendarButton, 0, 8)

        customerGridLayout.addWidget(houseNo, 1, 0)
        customerGridLayout.addWidget(QtWidgets.QLineEdit(), 1, 1)

        customerGridLayout.addWidget(streetName, 1, 2)
        customerGridLayout.addWidget(QtWidgets.QLineEdit(), 1, 3)

        customerGridLayout.addWidget(county, 1, 4)
        customerGridLayout.addWidget(QtWidgets.QLineEdit(), 1, 5)

        customerGridLayout.addWidget(postcode, 1, 6)
        customerGridLayout.addWidget(QtWidgets.QLineEdit(), 1, 7)

        self.country = QtWidgets.QComboBox()
        self.country.addItem("United Kingdom")
        customerGridLayout.addWidget(country, 2, 0)
        customerGridLayout.addWidget(self.country, 2, 1)

        customerGridLayout.addWidget(gender, 3, 0)
        customerGridLayout.addWidget(QtWidgets.QRadioButton("Male"), 3, 1)
        customerGridLayout.addWidget(QtWidgets.QRadioButton("Female"), 3, 2)

        self.smoker_yes = QtWidgets.QRadioButton("Yes")
        self.smoker_no = QtWidgets.QRadioButton("No")
        self.smoker_no.setChecked(True)
        customerGridLayout.addWidget(smoker, 4, 0)
        customerGridLayout.addWidget(self.smoker_yes, 4, 1)
        customerGridLayout.addWidget(self.smoker_no, 4, 2)

        self.employed = QtWidgets.QComboBox()
        self.employed.addItem("Employed")
        self.employed.addItem("Self Employed")
        self.employed.addItem("UnEmployed")
        self.employed.addItem("House Person")

        customerGridLayout.addWidget(employed, 5, 0)
        customerGridLayout.addWidget(self.employed, 5, 1)

        self.policy_type_single = QtWidgets.QRadioButton("Single")
        self.policy_type_single.setChecked(True)
        self.policy_type_joined = QtWidgets.QRadioButton("Joined")
        customerGridLayout.addWidget(policy_type, 6, 0)
        customerGridLayout.addWidget(self.policy_type_single, 6, 1)
        customerGridLayout.addWidget(self.policy_type_joined, 6, 2)

        customerGroupBox.setLayout(customerGridLayout)

        return customerGroupBox

    def openCalendar(self):
        pass


    def createReference(self):

        referneceGridLayout = QtWidgets.QHBoxLayout()

        referneceGridLayout.addStretch()

        date = QtWidgets.QLabel(self.tr("&Date:"))
        date.setBuddy(QtWidgets.QLineEdit())

        reference = QtWidgets.QLabel(self.tr("&Reference:"))
        reference.setBuddy(QtWidgets.QLineEdit())

        referenceGroupBox = QtWidgets.QGroupBox("")

        referneceGridLayout.addWidget(date)
        referneceGridLayout.addWidget(QtWidgets.QLineEdit())
        referneceGridLayout.addWidget(reference)
        referneceGridLayout.addWidget(QtWidgets.QLineEdit())

        referneceGridLayout.setAlignment(QtCore.Qt.AlignLeft)

        referenceGroupBox.setLayout(referneceGridLayout)

        return referenceGroupBox


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("SafeLife Application")
        self.setFixedWidth(1000)

        layout = QtWidgets.QVBoxLayout()
        singleton_widget = QtWidgets.QWidget()
        singleton_widget.setLayout(layout)
        geometery = QtWidgets.QDesktopWidget().availableGeometry()
        self.setFixedSize(geometery.width(), geometery.height())

        self.setCentralWidget(singleton_widget)

        toolbar = QtWidgets.QToolBar('Main toolbar')
        self.addToolBar(toolbar)

        icon = QtGui.QIcon("./images/insert.png")
        new_advisor = QtWidgets.QAction(icon, "New Employee", self)
        new_advisor.setStatusTip('New Advisor')
        new_advisor.setCheckable(False)
        toolbar.addAction(new_advisor)

        icon = QtGui.QIcon("./images/update.png")
        update_advisor = QtWidgets.QAction(icon, "Update Employee", self)
        update_advisor.setStatusTip('Update Advisor')
        update_advisor.triggered.connect(print_button_state)
        update_advisor.setCheckable(False)
        toolbar.addAction(update_advisor)


        icon = QtGui.QIcon("./images/delete.png")
        archive_advisor = QtWidgets.QAction(icon, "Delete Employee", self)
        archive_advisor.setStatusTip('Archive Advisor')
        archive_advisor.triggered.connect(print_button_state)
        archive_advisor.setCheckable(False)
        toolbar.addAction(archive_advisor)
        toolbar.addSeparator()



        new_referral = QtWidgets.QAction('New Referral', self)
        new_referral.setStatusTip('New Referral')
        new_referral.triggered.connect(print_button_state)
        new_referral.setCheckable(False)
        toolbar.addAction(new_referral)


        update_referral = QtWidgets.QAction('Update Referral', self)
        update_referral.setStatusTip('Update Referral')
        update_referral.triggered.connect(print_button_state)
        update_referral.setCheckable(False)
        toolbar.addAction(update_referral)

        delete_referral = QtWidgets.QAction('Delete Referral', self)
        delete_referral.setStatusTip('Update Referral')
        delete_referral.triggered.connect(print_button_state)
        delete_referral.setCheckable(False)
        toolbar.addAction(delete_referral)

        toolbar.addSeparator()

        icon = QtGui.QIcon("./images/insert.png")
        new_client = QtWidgets.QAction(icon, 'New Client', self)
        new_client.setStatusTip('New Client')
        new_client.triggered.connect(self.newClient)
        new_client.setCheckable(False)
        toolbar.addAction(new_client)

        icon = QtGui.QIcon("./images/update.png")
        update_client = QtWidgets.QAction(icon, 'Update Client', self)
        update_client.setStatusTip('Update Client')
        update_client.triggered.connect(print_button_state)
        update_client.setCheckable(False)
        toolbar.addAction(update_client)

        icon = QtGui.QIcon("./images/delete.png")
        delete_client = QtWidgets.QAction(icon, 'Delete Client', self)
        delete_client.setStatusTip('Delete Client')
        delete_client.triggered.connect(print_button_state)
        delete_client.setCheckable(False)
        toolbar.addAction(delete_client)
        toolbar.setFloatable(True)
        toolbar.addSeparator()

    def newClient(self):
        NewClientFormDialog().exec_()

    def contextMenuEvent(self, event):
        print('Context menu event happened!')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    pixmap = QtGui.QPixmap(":/images/windows.png")
    splash = QtWidgets.QSplashScreen(pixmap)
    splash.show()
    splash.showMessage("Loaded modules")
    window = MainWindow()
    window.show()
    splash.showMessage("Established connections")

    splash.finish(window)

    # Start the event loop.
    app.exec_()
