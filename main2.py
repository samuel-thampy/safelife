import sys

from PySide2 import QtGui, QtWidgets, QtCore
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker, backref
from sqlalchemy import create_engine
# from sqlalchemy_imageattach.entity import Image, image_attachment


username = 'safelife'
password = 'safelife'
hostname = 'localhost'
database_name = 'safelife_db'
engine = create_engine('postgresql+psycopg2://{}:{}@{}/{}'.format(username, password, hostname, database_name),
                       convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base = declarative_base()
Base.query = db_session.query_property()


class _GCProtector(object):
    widgets = []


class Referee(Base):
    __tablename__ = 'referee'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email_address = Column(String(250), nullable=False)
    dob = Column(DateTime, nullable=False)

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    county = Column(String(250))
    post_code = Column(String(250), nullable=False)
    country = Column(String(250), nullable=False)
    client_id = Column(Integer, ForeignKey('client.id'))

class Provider(Base):
    __tablename__ = 'provider'

    id = Column(Integer, primary_key=True)
    provider_name = Column(String(250), nullable=False)
    insuranceTypes = relationship("insuranceTypes")

class PremiumInsuranceType(Base):
    __tablename__ = 'premium_insurance_type'

    id = Column(Integer, primary_key=True)

class Employee(Base):
    __tablename__ = 'employee'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    employee_no = Column(String(250), nullable=False)
    employee_type = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    dob = Column(DateTime, nullable=False)
    mobile_number = Column(String(250), nullable=False)
    # employee_picture = image_attachment('EmployeePicture')
    commission = relationship("CommissionTable")


class EmployeeRefereeQuery():
    pass

class CommissionTable(Base):
    __tablename__ = 'commission_table'
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employee.id'))


# class EmployeePicture(Base, Image):
#     """User picture model."""
#
#     employee_id = Column(Integer, ForeignKey('employee.id'), primary_key=True)
#     employee = relationship('Employee')
#     __tablename__ = 'employee_picture'


class Client(Base):
    __tablename__ = 'client'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email_address = Column(String(250), nullable=False, unique=True, index=True)
    dob = Column(DateTime, nullable=False)
    gender = Column(String(250), nullable=False)
    smoker = Column(String(250), nullable=False)
    employed = Column(String(250), nullable=False)
    policy_type = Column(String(250), nullable=False)
    addresses = relationship("Address", backref="client")

    client = relationship(Address)


    def save(self):
        s = db_session()
        s.add(self)
        return s.commit()


class JoinClient(Base):
    __tablename__ = 'joinclient'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship(Client)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email_address = Column(String(250), nullable=False)
    dob = Column(DateTime, nullable=False)
    gender = Column(String(250), nullable=False)
    smoker = Column(String(250), nullable=False)
    employed = Column(String(250), nullable=False)
    policy_type = Column(String(250), nullable=False)


class ClientInsuranceDetails(Base):
    __tablename__ = 'clientinsurnacedetails'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship(Client)
    date_started = Column(DateTime, nullable=False)
    reference = Column(DateTime, nullable=False)
    renewal_date = Column(DateTime, nullable=False)


class InsuranceType(Base):
    __tablename__ = 'insurancetype'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship(Client)
    cover_amount = Column(Integer)
    premium_amount =  Column(Integer)
    premium_type = Column(String(250), nullable=False)


class LifeCoverInsurance(Base):
    __tablename__ = 'lifecoverinsurance'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship(Client)
    plan_type = Column(String(250))
    life_cover = Column(String(250))
    term_of_cover = Column(String(250))
    occupation = Column(String(250))
    duty = Column(String(250))
    residency = Column(String(250))
    smoker = Column(String(250))
    height = Column(String(250))
    height_unit = Column(String(250))
    weight = Column(String(250))
    weight_unit = Column(String(250))
    family_health = Column(Text)
    health_details = Column(Text)
    renewal = Column(String)

class CriticalSeriousInsurance(Base):
    __tablename__ = 'criticalseriousinsurance'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship(Client)
    plan_type = Column(String(250))
    life_cover = Column(String(250))
    term_of_cover = Column(String(250))
    occupation = Column(String(250))
    duty = Column(String(250))
    residency = Column(String(250))
    smoker = Column(String(250))
    height = Column(String(250))
    height_unit = Column(String(250))
    weight = Column(String(250))
    weight_unit = Column(String(250))
    family_health = Column(Text)
    health_details = Column(Text)
    renewal = Column(String)


class IncomeProtection(Base):
    __tablename__ = 'incomeprotection'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship(Client)
    provider = Column(String(250))
    type_of_industry = Column(String(250))
    employement_type = Column(String(250))
    type_of_job = Column(String(250))
    any_second_job = Column(String(250))
    policy_for = Column(String(250))
    policy_type = Column(String(250))
    policy_start = Column(String(250))
    premium_date = Column(String(250))
    benefit_amount = Column(String(250))
    premium = Column(String(250))
    deferred_period = Column(String(250))
    smoker = Column(String(250))
    height = Column(String(250))
    height_unit = Column(String(250))
    weight = Column(String(250))
    weight_unit = Column(String(250))
    notes = Column(Text)
    renewal = Column(String)


class BuildProtectionCover(Base):
    __tablename__ = 'buildingcoverprotection'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship(Client)
    provider = Column(String(250))
    no_of_bedrooms = Column(String(250))
    claims_any = Column(String(250))
    accident_buildings = Column(String(250))
    buildings = Column(String(250))
    contents = Column(String(250))
    accident_contents = Column(Text)
    emergency = Column(Text)
    legal_cover = Column(String(250))
    personal_possession = Column(String(250))
    start_date = Column(Text)
    flood_risk = Column(String)
    notes = Column(String)
    renewal = Column(String)


class BuildProtectionShopCover(Base):
    __tablename__ = 'buildingcovershopprotection'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship(Client)
    provider = Column(String(250))
    no_of_bedrooms = Column(String(250))
    claims_any = Column(String(250))
    accident_buildings = Column(String(250))
    buildings = Column(String(250))
    contents = Column(String(250))
    accident_contents = Column(Text)
    emergency = Column(Text)
    legal_cover = Column(String(250))
    personal_possession = Column(String(250))
    start_date = Column(Text)
    flood_risk = Column(String)
    notes = Column(String)
    renewal = Column(String)


class BuildProtectionLiabilityCover(Base):
    __tablename__ = 'buildingcoverliabilityprotection'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship(Client)
    provider = Column(String(250))
    no_of_bedrooms = Column(String(250))
    claims_any = Column(String(250))
    accident_buildings = Column(String(250))
    buildings = Column(String(250))
    contents = Column(String(250))
    accident_contents = Column(Text)
    emergency = Column(Text)
    legal_cover = Column(String(250))
    personal_possession = Column(String(250))
    start_date = Column(Text)
    flood_risk = Column(String)
    notes = Column(String)
    renewal = Column(String)


class BuildProtectionBusinessCover(Base):
    __tablename__ = 'buildingcoverbusinessprotection'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship(Client)
    provider = Column(String(250))
    no_of_bedrooms = Column(String(250))
    claims_any = Column(String(250))
    accident_buildings = Column(String(250))
    buildings = Column(String(250))
    contents = Column(String(250))
    accident_contents = Column(Text)
    emergency = Column(Text)
    legal_cover = Column(String(250))
    personal_possession = Column(String(250))
    start_date = Column(Text)
    flood_risk = Column(String)
    notes = Column(String)
    renewal = Column(String)


class GPDetails(Base):
    __tablename__ = 'gpdetails'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship(Client)
    surgery_name =  Column(String)
    surgery_house_no =  Column(String)
    street_name = Column(String(250))
    street_number = Column(String(250))
    county = Column(String(250))
    post_code = Column(String(250), nullable=False)
    country = Column(String(250), nullable=False)

class ClientGPDetails(Base):
    __tablename__ = 'clientgpdetails'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship(Client)
    gp_details_id = Column(Integer, ForeignKey('gpdetails.id'))
    gp_details = relationship(GPDetails)
    health_details = Column(Text)
    family_history = Column(Text)
    sports_hobbies = Column(Text)


class BankDetails(Base):
    __tablename__ = 'bankdetails'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship(Client)
    bank_name = Column(String(250))
    bank_address = Column(Text)
    bank_sort_code = Column(String(250))
    bank_account = Column(String(250))


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
    GUARANTEED = 'Guaranteed'
    VARIABLE = 'Variable'

class LifeCoverEnum():
    FIRST_DEATH = 'First Death'
    SEPARATE = 'Separate'

class PlanTypeEnum():
    INDEXED = 'Index'
    LEVEL = 'Level'
    DECREASE = 'Decrease'
    INCREASE = 'Increase'


class HeightUnitEnum():
    INCHES = 'inches'
    CENTIMETER = 'cm'
    METER = 'm'
    FEET = 'ft'

class WeightUnitEnum():
    KILOGRAM = 'kg'
    POUNDS = 'lbs'

class ProviderEnum():
    SUNLIFE = 'Sunlife'
    AVIVA = 'Aviva'

class PolicyNumberEnum():
    SUNLIFE = 'a12333'
    SIS = '1123'



class NewClientFormDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(NewClientFormDialog, self).__init__(parent)

        self.customerDetails = {}

        self.gridLayout = QtWidgets.QGridLayout()

        self.gridLayout.addWidget(self.createReference(), 0, 0)
        self.gridLayout.addWidget(self.createCustomerDetails(), 1, 0)
        self.gridLayout.addWidget(self.createInsuranceType(), 3, 0)

        self.gridLayout.addWidget(self.createLifeInsuranceCover(), 4, 0)

        self.gridLayout.addWidget(self.createGPDetails(), 5, 0)
        self.gridLayout.addWidget(self.createBankDetails(), 6, 0)
        self.gridLayout.addLayout(self.create_save_buttons(), 7, 0)

        self.gridLayout.setAlignment(QtCore.Qt.AlignLeft)

        self.setWindowTitle("New Client")
        self.setWindowIcon(QtGui.QIcon("./images/safelifeLogo.png"))

        self.setLayout(self.gridLayout)

    def current_index_change(self, i):
        item = self.gridLayout.itemAtPosition(4, 0)
        if item is not None:
            item.widget().deleteLater()
            self.gridLayout.removeItem(item)

        if i == 0:
            self.gridLayout.addWidget(self.createLifeInsuranceCover(), 4, 0)
        elif i == 1:
            self.gridLayout.addWidget(self.createCriticalIlnessCover(), 4, 0)
        elif i == 2:
            self.gridLayout.addWidget(self.createIncomeProtectionCover(), 4, 0)
        elif i == 3:
            self.gridLayout.addWidget(self.createBuildingInsurance(), 4, 0)
        elif i == 4:
            self.gridLayout.addWidget(self.createBuildingInsurance(), 4, 0)
        elif i == 5:
            self.gridLayout.addWidget(self.createBuildingInsurance(), 4, 0)
        elif i == 6:
            self.gridLayout.addWidget(self.createBuildingInsurance(), 4, 0)
        elif i == 7:
            self.gridLayout.addWidget(self.createBuildingInsurance(), 4, 0)

        self.setLayout(self.gridLayout)

    def createCustomerDetails(self):
        customerGridLayout = QtWidgets.QGridLayout()

        nameLabel = QtWidgets.QLabel(self.tr("First Name(s):"))
        self.first_name_client_one = QtWidgets.QLineEdit()

        lastNameLabel = QtWidgets.QLabel("Last Name:")
        self.last_name_client_one = QtWidgets.QLineEdit()

        emailAddress = QtWidgets.QLabel("Email Address:")
        self.email_address_client_one = QtWidgets.QLineEdit()

        dob = QtWidgets.QLabel(self.tr("Date Of Birth:"))
        self.dob_client_one = QtWidgets.QDateEdit()

        houseNo = QtWidgets.QLabel(self.tr("House No/ House Name:"))
        self.house_no_client_one = QtWidgets.QLineEdit()

        streetName = QtWidgets.QLabel(self.tr("Street Name:"))
        self.street_name_client_one = QtWidgets.QLineEdit()

        county = QtWidgets.QLabel(self.tr("County:"))
        self.county_client_one = QtWidgets.QLineEdit()

        city = QtWidgets.QLabel(self.tr("City:"))
        self.city_client_one = QtWidgets.QLineEdit()

        postcode = QtWidgets.QLabel(self.tr("Postcode:"))
        self.post_code_client_one = QtWidgets.QLineEdit()

        countryLabel = QtWidgets.QLabel(self.tr("Country:"))
        self.country_client_one = QtWidgets.QComboBox()
        self.country_client_one.addItem("United Kingdom")

        gender = QtWidgets.QLabel(self.tr("Gender:"))
        genderGroupBox = QtWidgets.QGroupBox()
        genderHBoxLayout = QtWidgets.QHBoxLayout()
        genderHBoxLayout.addWidget(gender)
        self.gender_male_client_one = QtWidgets.QRadioButton("Male")
        self.gender_female_client_one = QtWidgets.QRadioButton("Female")
        self.gender_male_client_one.setChecked(True)
        genderHBoxLayout.addWidget(self.gender_male_client_one)
        genderHBoxLayout.addWidget(self.gender_female_client_one)
        genderGroupBox.setLayout(genderHBoxLayout)

        smoker = QtWidgets.QLabel(self.tr("Smoker:"))
        smokerGroupBox = QtWidgets.QGroupBox()
        smokerHBoxLayout = QtWidgets.QHBoxLayout()
        self.smoker_yes_client_one = QtWidgets.QRadioButton("Yes")
        self.smoker_no_client_one = QtWidgets.QRadioButton("No")
        self.smoker_no_client_one.setChecked(True)
        smokerHBoxLayout.addWidget(smoker)
        smokerHBoxLayout.addWidget(self.smoker_yes_client_one)
        smokerHBoxLayout.addWidget(self.smoker_no_client_one)
        smokerGroupBox.setLayout(smokerHBoxLayout)

        employedLabel = QtWidgets.QLabel(self.tr("Employed:"))
        self.employed_client_one = QtWidgets.QComboBox()
        self.employed_client_one.addItem("Employed")
        self.employed_client_one.addItem("Self Employed")
        self.employed_client_one.addItem("UnEmployed")
        self.employed_client_one.addItem("House Person")

        policyTypeLabel = QtWidgets.QLabel(self.tr("Policy Type:"))
        policyTypeGroupBox = QtWidgets.QGroupBox()
        policyTypeHBoxLayout = QtWidgets.QHBoxLayout()
        self.policy_type_single = QtWidgets.QRadioButton("Single")
        self.policy_type_joined = QtWidgets.QRadioButton("Joint")
        self.policy_type_single.setChecked(True)
        policyTypeHBoxLayout.addWidget(policyTypeLabel)
        policyTypeHBoxLayout.addWidget(self.policy_type_single)
        policyTypeHBoxLayout.addWidget(self.policy_type_joined)
        policyTypeGroupBox.setLayout(policyTypeHBoxLayout)
        self.policy_type_joined.toggled.connect(self.joined_person)

        customerGroupBox = QtWidgets.QGroupBox("Customer Details")
        customerGridLayout.addWidget(nameLabel, 0, 0)
        customerGridLayout.addWidget(self.first_name_client_one, 0, 1)
        customerGridLayout.addWidget(lastNameLabel, 0, 2)
        customerGridLayout.addWidget(self.last_name_client_one, 0, 3)
        customerGridLayout.addWidget(emailAddress, 0, 4)
        customerGridLayout.addWidget(self.email_address_client_one, 0, 5)
        customerGridLayout.addWidget(dob, 0, 6)
        customerGridLayout.addWidget(self.dob_client_one, 0, 7)
        customerGridLayout.addWidget(houseNo, 1, 0)
        customerGridLayout.addWidget(self.house_no_client_one, 1, 1)
        customerGridLayout.addWidget(streetName, 1, 2)
        customerGridLayout.addWidget(self.street_name_client_one, 1, 3)
        customerGridLayout.addWidget(county, 1, 4)
        customerGridLayout.addWidget(self.county_client_one, 1, 5)
        customerGridLayout.addWidget(postcode, 1, 6)
        customerGridLayout.addWidget(self.post_code_client_one, 1, 7)
        customerGridLayout.addWidget(city, 2, 0)
        customerGridLayout.addWidget(self.city_client_one, 2, 1)
        customerGridLayout.addWidget(countryLabel, 2, 2)
        customerGridLayout.addWidget(self.country_client_one, 2, 3)
        customerGridLayout.addWidget(genderGroupBox, 2, 4)
        customerGridLayout.addWidget(smokerGroupBox, 2, 5)
        customerGridLayout.addWidget(employedLabel, 2, 6)
        customerGridLayout.addWidget(self.employed_client_one, 2, 7)
        customerGridLayout.addWidget(policyTypeGroupBox, 3, 0)

        customerGroupBox.setLayout(customerGridLayout)

        return customerGroupBox

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
        self.insuranceType.currentIndexChanged.connect(self.current_index_change)

        coverAmountLabel = QtWidgets.QLabel(self.tr("&Cover Amount: £"))
        coverAmountLabel.setBuddy(QtWidgets.QLineEdit())
        self.coverAmount = QtWidgets.QLineEdit()

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

    def create_save_buttons(self):
        buttonsLayout = QtWidgets.QHBoxLayout()
        buttonsLayout.addStretch(3)
        saveButton = QtWidgets.QPushButton("Save")
        saveButton.clicked.connect(self.save_client_details)
        cancelButton = QtWidgets.QPushButton("Cancel")

        buttonsLayout.addWidget(saveButton)
        buttonsLayout.addWidget(cancelButton)

        return buttonsLayout

    def save_client_details(self):
        client = Client()
        client.first_name = self.first_name_client_one.text()
        client.last_name = self.last_name_client_one.text()
        client.email_address = self.email_address_client_one.text()
        client.dob = self.dob_client_one.text()
        client.gender = self.gender_male_client_one.text()
        client.smoker = self.smoker_no_client_one.text()
        client.employed = self.employed_client_one.currentText()
        client.policy_type = self.policy_type_single.text()

        return client.save()

    def joined_person(self):
        item = self.gridLayout.itemAtPosition(2, 0)
        if item is not None:
            item.widget().deleteLater()
            self.gridLayout.removeItem(item)
        else:
            self.gridLayout.addWidget(self.createJoinedPerson(), 2, 0)

        self.setLayout(self.gridLayout)

    def createJoinedPerson(self):
        customerGridLayout = QtWidgets.QGridLayout()

        nameLabel = QtWidgets.QLabel(self.tr("First Name(s):"))
        self.first_name_client_two = QtWidgets.QLineEdit()

        lastNameLabel = QtWidgets.QLabel("Last Name:")
        self.last_name_client_two = QtWidgets.QLineEdit()

        emailAddress = QtWidgets.QLabel("Email Address:")
        self.email_address_client_two = QtWidgets.QLineEdit()

        dob = QtWidgets.QLabel(self.tr("Date Of Birth:"))

        self.dob_client_two = QtWidgets.QDateEdit()

        houseNo = QtWidgets.QLabel(self.tr("House No/ House Name:"))
        self.house_no_client_two = QtWidgets.QLineEdit()

        streetName = QtWidgets.QLabel(self.tr("Street Name:"))
        self.street_name_client_two = QtWidgets.QLineEdit()

        county = QtWidgets.QLabel(self.tr("County:"))
        self.county_client_two = QtWidgets.QLineEdit()

        city = QtWidgets.QLabel(self.tr("City:"))
        self.city_client_two = QtWidgets.QLineEdit()

        postcode = QtWidgets.QLabel(self.tr("Postcode:"))
        self.post_code_client_two = QtWidgets.QLineEdit()

        countryLabel = QtWidgets.QLabel(self.tr("Country:"))
        self.country_client_two = QtWidgets.QComboBox()
        self.country_client_two.addItem("United Kingdom")

        gender = QtWidgets.QLabel("Gender:")
        genderGroupBox = QtWidgets.QGroupBox()
        genderHBoxLayout = QtWidgets.QHBoxLayout()
        genderHBoxLayout.addWidget(gender)
        self.gender_male_client_two = QtWidgets.QRadioButton("Male")
        self.gender_female_client_two = QtWidgets.QRadioButton("Female")
        self.gender_female_client_two.setChecked(True)
        genderHBoxLayout.addWidget(self.gender_male_client_two)
        genderHBoxLayout.addWidget(self.gender_female_client_two)
        genderGroupBox.setLayout(genderHBoxLayout)

        smoker = QtWidgets.QLabel(self.tr("Smoker:"))
        smokerGroupBox = QtWidgets.QGroupBox()
        smokerHBoxLayout = QtWidgets.QHBoxLayout()
        self.smoker_yes_client_two = QtWidgets.QRadioButton("Yes")
        self.smoker_no_client_two = QtWidgets.QRadioButton("No")
        self.smoker_no_client_two.setChecked(True)
        smokerHBoxLayout.addWidget(smoker)
        smokerHBoxLayout.addWidget(self.smoker_yes_client_two)
        smokerHBoxLayout.addWidget(self.smoker_no_client_two)
        smokerGroupBox.setLayout(smokerHBoxLayout)

        employedLabel = QtWidgets.QLabel("Employed:")
        self.employed_client_two = QtWidgets.QComboBox()
        self.employed_client_two.addItem("Employed")
        self.employed_client_two.addItem("Self Employed")
        self.employed_client_two.addItem("UnEmployed")
        self.employed_client_two.addItem("House Person")

        customerGroupBox = QtWidgets.QGroupBox("Joint Customer")
        customerGridLayout.addWidget(nameLabel, 0, 0)
        customerGridLayout.addWidget(self.first_name_client_two, 0, 1)
        customerGridLayout.addWidget(lastNameLabel, 0, 2)
        customerGridLayout.addWidget(self.last_name_client_two, 0, 3)
        customerGridLayout.addWidget(emailAddress, 0, 4)
        customerGridLayout.addWidget(self.email_address_client_two, 0, 5)
        customerGridLayout.addWidget(dob, 0, 6)
        customerGridLayout.addWidget(self.dob_client_two, 0, 7)
        customerGridLayout.addWidget(houseNo, 1, 0)
        customerGridLayout.addWidget(self.house_no_client_two, 1, 1)
        customerGridLayout.addWidget(streetName, 1, 2)
        customerGridLayout.addWidget(self.street_name_client_two, 1, 3)
        customerGridLayout.addWidget(county, 1, 4)
        customerGridLayout.addWidget(self.county_client_two, 1, 5)
        customerGridLayout.addWidget(postcode, 1, 6)
        customerGridLayout.addWidget(self.post_code_client_two, 1, 7)
        customerGridLayout.addWidget(city, 2, 0)
        customerGridLayout.addWidget(self.city_client_two, 2, 1)
        customerGridLayout.addWidget(countryLabel, 2, 2)
        customerGridLayout.addWidget(self.country_client_two, 2, 3)
        customerGridLayout.addWidget(genderGroupBox, 2, 4)
        customerGridLayout.addWidget(smokerGroupBox, 2, 5)
        customerGridLayout.addWidget(employedLabel, 2, 6)
        customerGridLayout.addWidget(self.employed_client_two, 2, 7)

        customerGroupBox.setLayout(customerGridLayout)

        return customerGroupBox

    def createBuildingInsurance(self):
        BuildingInsuranceGroupBox = QtWidgets.QGroupBox("Building Insurance Cover")
        BuildingInsuranceGridLayout = QtWidgets.QGridLayout()

        providerLabel = QtWidgets.QLabel("Provider:")
        providerLabel.setBuddy(QtWidgets.QLineEdit())
        self.provider = QtWidgets.QComboBox()
        self.provider.addItem(ProviderEnum.AVIVA)
        self.provider.addItem(ProviderEnum.SUNLIFE)

        policyNumberLabel = QtWidgets.QLabel("Policy Number:")
        self.policyNumber = QtWidgets.QComboBox()
        self.policyNumber.addItem(PolicyNumberEnum.SUNLIFE)
        self.policyNumber.addItem(PolicyNumberEnum.SIS)

        builtYearLabel = QtWidgets.QLabel("Built Year:")
        builtYearLabel.setBuddy(QtWidgets.QLineEdit())
        self.built_year = QtWidgets.QLineEdit()

        noOfBedroomsLabel = QtWidgets.QLabel("No of Bedrooms:")
        noOfBedroomsLabel.setBuddy(QtWidgets.QLineEdit())
        self.no_of_bedrooms = QtWidgets.QLineEdit()
        self.no_of_bedrooms.setFixedWidth(50)


        claimsAnyLabel = QtWidgets.QLabel("Claims Any:")
        self.claims_any = QtWidgets.QLineEdit()
        self.claims_any.setFixedWidth(300)
        self.claims_any.setFixedHeight(50)

        accidentBuildingGroupBox = QtWidgets.QGroupBox()
        accidentBuildingLabel = QtWidgets.QLabel("Accident Buildings:")
        self.accident_building_yes = QtWidgets.QRadioButton("Yes")
        self.accident_building_no = QtWidgets.QRadioButton("No")
        self.accident_building_yes.setChecked(True)
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(accidentBuildingLabel)
        hbox.addWidget(self.accident_building_yes)
        hbox.addWidget(self.accident_building_no)
        accidentBuildingGroupBox.setLayout(hbox)

        buildingGroupBox = QtWidgets.QGroupBox()
        BuildingLabel = QtWidgets.QLabel("Building:")
        self.building_yes = QtWidgets.QRadioButton("Yes")
        self.building_no = QtWidgets.QRadioButton("No")
        self.building_yes.setChecked(True)
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(BuildingLabel)
        hbox.addWidget(self.building_yes)
        hbox.addWidget(self.building_no)
        buildingGroupBox.setLayout(hbox)

        contentsGroupBox = QtWidgets.QGroupBox()
        contentsLabel = QtWidgets.QLabel("Contents:")
        self.contents_yes = QtWidgets.QRadioButton("Yes")
        self.contents_no = QtWidgets.QRadioButton("No")
        self.contents_yes.setChecked(True)
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(contentsLabel)
        hbox.addWidget(self.contents_yes)
        hbox.addWidget(self.contents_no)
        contentsGroupBox.setLayout(hbox)

        accidentsContentsLabel = QtWidgets.QLabel("Accident Contents:")
        accidentsContentsLabel.setBuddy(QtWidgets.QLineEdit())
        self.accident_contents = QtWidgets.QLineEdit()
        self.accident_contents.setFixedWidth(300)
        self.accident_contents.setFixedHeight(50)

        emergencyGroupBox = QtWidgets.QGroupBox()
        emergencyLabel = QtWidgets.QLabel("Emergency:")
        self.emergency_yes = QtWidgets.QRadioButton("Yes")
        self.emergency_no = QtWidgets.QRadioButton("No")
        self.emergency_yes.setChecked(True)
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(emergencyLabel)
        hbox.addWidget(self.emergency_yes)
        hbox.addWidget(self.emergency_no)
        emergencyGroupBox.setLayout(hbox)

        legalCoverGroupBox = QtWidgets.QGroupBox()
        legalCoverLabel = QtWidgets.QLabel("Legal Cover:")
        self.legalCover_yes = QtWidgets.QRadioButton("Yes")
        self.legalCover_no = QtWidgets.QRadioButton("No")
        self.legalCover_yes.setChecked(True)
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(legalCoverLabel)
        hbox.addWidget(self.legalCover_yes)
        hbox.addWidget(self.legalCover_no)
        legalCoverGroupBox.setLayout(hbox)

        personalPossessionGroupBox = QtWidgets.QGroupBox()
        self.personal_possession_yes = QtWidgets.QRadioButton("Yes")
        self.personal_possession_no = QtWidgets.QRadioButton("No")
        self.personal_possession_yes.setChecked(True)
        self.personal_possession = QtWidgets.QLineEdit()
        self.personal_possession.setFixedWidth(300)
        self.personal_possession.setFixedHeight(50)
        personalPossessionLabel = QtWidgets.QLabel("Personal Possession:")
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(personalPossessionLabel)
        hbox.addWidget(self.personal_possession_yes)
        hbox.addWidget(self.personal_possession_no)
        hbox.addWidget(self.personal_possession)
        personalPossessionGroupBox.setLayout(hbox)

        startDateLabel = QtWidgets.QLabel("Start Date:")
        self.building_cover_start_date = QtWidgets.QDateEdit()
        self.building_cover_start_date.setDate(QtCore.QDate.currentDate())

        floodRiskLabel = QtWidgets.QLabel("Flood Risk:")
        floodRiskGroupBox = QtWidgets.QGroupBox()
        self.flood_risk_yes = QtWidgets.QRadioButton("Yes")
        self.flood_risk_no = QtWidgets.QRadioButton("No")
        self.flood_risk_yes.setChecked(True)
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(floodRiskLabel)
        hbox.addWidget(self.flood_risk_yes)
        hbox.addWidget(self.flood_risk_no)
        floodRiskGroupBox.setLayout(hbox)

        notesLabel = QtWidgets.QLabel("Notes:")
        notesLabel.setBuddy(QtWidgets.QLineEdit())
        self.buildingCoverNotes = QtWidgets.QLineEdit()
        self.buildingCoverNotes.setFixedWidth(300)
        self.buildingCoverNotes.setFixedHeight(50)

        renewalLabel = QtWidgets.QLabel("Renewal:")
        self.renewal_building_insurance_date = QtWidgets.QDateEdit()
        self.renewal_building_insurance_date.setDate(QtCore.QDate.currentDate().addDays(365))

        BuildingInsuranceGridLayout.addWidget(providerLabel, 0, 0)
        BuildingInsuranceGridLayout.addWidget(self.provider, 0, 1)
        BuildingInsuranceGridLayout.addWidget(policyNumberLabel, 0, 2)
        BuildingInsuranceGridLayout.addWidget(self.policyNumber, 0, 3)
        BuildingInsuranceGridLayout.addWidget(noOfBedroomsLabel, 0, 4)
        BuildingInsuranceGridLayout.addWidget(self.no_of_bedrooms, 0, 5)
        BuildingInsuranceGridLayout.addWidget(claimsAnyLabel, 1, 0)
        BuildingInsuranceGridLayout.addWidget(self.claims_any, 1, 1)
        BuildingInsuranceGridLayout.addWidget(accidentBuildingGroupBox, 1, 2)
        BuildingInsuranceGridLayout.addWidget(buildingGroupBox, 1, 3)
        BuildingInsuranceGridLayout.addWidget(contentsGroupBox, 1, 4)
        BuildingInsuranceGridLayout.addWidget(accidentsContentsLabel, 1, 5)
        BuildingInsuranceGridLayout.addWidget(self.accident_contents, 1, 6)
        BuildingInsuranceGridLayout.addWidget(emergencyGroupBox, 2, 0)
        BuildingInsuranceGridLayout.addWidget(legalCoverGroupBox, 2, 1)
        BuildingInsuranceGridLayout.addWidget(personalPossessionGroupBox, 2, 2)
        BuildingInsuranceGridLayout.addWidget(floodRiskGroupBox, 2, 3)
        BuildingInsuranceGridLayout.addWidget(startDateLabel, 2, 4)
        BuildingInsuranceGridLayout.addWidget(self.building_cover_start_date, 2, 5)
        BuildingInsuranceGridLayout.addWidget(notesLabel, 3, 0)
        BuildingInsuranceGridLayout.addWidget(self.buildingCoverNotes, 3, 1)
        BuildingInsuranceGridLayout.addWidget(renewalLabel, 3, 2)
        BuildingInsuranceGridLayout.addWidget(self.renewal_building_insurance_date, 3, 3)

        BuildingInsuranceGroupBox.setLayout(BuildingInsuranceGridLayout)

        return BuildingInsuranceGroupBox

    def createIncomeProtectionCover(self):

        providerLabel = QtWidgets.QLabel("Provider:")
        providerLabel.setBuddy(QtWidgets.QLineEdit())
        self.provider = QtWidgets.QComboBox()
        self.provider.addItem(ProviderEnum.AVIVA)
        self.provider.addItem(ProviderEnum.SUNLIFE)

        policyNumberLabel = QtWidgets.QLabel("Policy Number:")
        self.policyNumber = QtWidgets.QComboBox()
        self.policyNumber.addItem(PolicyNumberEnum.SUNLIFE)
        self.policyNumber.addItem(PolicyNumberEnum.SIS)


        occupationLabel = QtWidgets.QLabel(self.tr("&Occupation:"))
        occupationLabel.setBuddy(QtWidgets.QLineEdit())
        self.occupation = QtWidgets.QLineEdit()

        industryTypeLabel = QtWidgets.QLabel(self.tr("&Type Of Industry:"))
        industryTypeLabel.setBuddy(QtWidgets.QLineEdit())
        self.industryType = QtWidgets.QLineEdit()

        employedLabel = QtWidgets.QLabel(self.tr("&Employed:"))
        employedLabel.setBuddy(QtWidgets.QLineEdit())
        self.employed = QtWidgets.QComboBox()
        self.employed.addItem("Employed")
        self.employed.addItem("Self Employed")
        self.employed.addItem("UnEmployed")
        self.employed.addItem("House Person")

        jobTypeLabel = QtWidgets.QLabel(self.tr("&Type Of Job:"))
        jobTypeLabel.setBuddy(QtWidgets.QLineEdit())
        self.jobType = QtWidgets.QLineEdit()
        self.jobType.setFixedWidth(300)
        self.jobType.setFixedHeight(50)

        secondJobLabel = QtWidgets.QLabel(self.tr("&Type Of Second Job:"))
        secondJobLabel.setBuddy(QtWidgets.QLineEdit())
        self.secondJob = QtWidgets.QLineEdit()
        self.secondJob.setFixedWidth(300)
        self.secondJob.setFixedHeight(50)

        policyForLabel = QtWidgets.QLabel(self.tr("&Policy For:"))
        policyForLabel.setBuddy(QtWidgets.QComboBox())
        self.policyFor = QtWidgets.QComboBox()
        self.policyFor.addItem("New")
        self.policyFor.addItem("Increase")
        self.policyFor.addItem("Replace")

        policyStartLabel = QtWidgets.QLabel(self.tr("&Policy Type:"))
        policyStartLabel.setBuddy(QtWidgets.QLineEdit())
        self.policyStart = QtWidgets.QLineEdit()

        paymentDatetLabel = QtWidgets.QLabel(self.tr("&Payment Date:"))
        paymentDatetLabel.setBuddy(QtWidgets.QLineEdit())
        self.paymentDate = QtWidgets.QLineEdit()

        benefitAmountLabel = QtWidgets.QLabel(self.tr("&Benefit Amount:"))
        benefitAmountLabel.setBuddy(QtWidgets.QLineEdit())

        self.benefitAmount = QtWidgets.QLineEdit()

        deferredPeriodLabel = QtWidgets.QLabel(self.tr("&Deferred Period:"))
        deferredPeriodLabel.setBuddy(QtWidgets.QLineEdit())
        self.deferredPeriod = QtWidgets.QLineEdit()

        IncomeProtectionGroupBox = QtWidgets.QGroupBox("Income Protection Cover")
        IncomeProtectionGridLayout = QtWidgets.QGridLayout()

        IncomeProtectionGridLayout.addWidget(occupationLabel, 0, 0)
        IncomeProtectionGridLayout.addWidget(self.occupation, 0, 1)
        IncomeProtectionGridLayout.addWidget(industryTypeLabel, 0, 2)
        IncomeProtectionGridLayout.addWidget(self.industryType, 0, 3)
        IncomeProtectionGridLayout.addWidget(employedLabel, 0, 4)
        IncomeProtectionGridLayout.addWidget(self.employed, 0, 5)
        IncomeProtectionGridLayout.addWidget(jobTypeLabel, 0, 6)
        IncomeProtectionGridLayout.addWidget(self.jobType, 0, 7)
        IncomeProtectionGridLayout.addWidget(secondJobLabel, 0, 8)
        IncomeProtectionGridLayout.addWidget(self.secondJob, 0, 9)
        IncomeProtectionGridLayout.addWidget(policyForLabel, 0, 10)
        IncomeProtectionGridLayout.addWidget(self.policyFor, 0, 11)
        IncomeProtectionGridLayout.addWidget(policyStartLabel, 0, 12)
        IncomeProtectionGridLayout.addWidget(self.policyStart, 0, 13)
        IncomeProtectionGridLayout.addWidget(policyStartLabel, 0, 12)
        IncomeProtectionGridLayout.addWidget(self.policyStart, 0, 13)
        IncomeProtectionGridLayout.addWidget(policyStartLabel, 0, 12)
        IncomeProtectionGridLayout.addWidget(self.policyStart, 0, 13)

        IncomeProtectionGroupBox.setLayout(IncomeProtectionGridLayout)

        return IncomeProtectionGroupBox

    def createGPDetails(self):
        gpNameSurgeryNameLabel = QtWidgets.QLabel(self.tr("&GP Name/Surgery Name:"))
        gpNameSurgeryNameLabel.setBuddy(QtWidgets.QLineEdit())
        self.gpName = QtWidgets.QLineEdit()

        gpHouseNoLabel = QtWidgets.QLabel(self.tr("&House No/ House Name:"))
        gpHouseNoLabel.setBuddy(QtWidgets.QLineEdit())
        self.gpHouseNo = QtWidgets.QLineEdit()

        gpStreetNameLabel = QtWidgets.QLabel(self.tr("&Street Name:"))
        gpStreetNameLabel.setBuddy(QtWidgets.QLineEdit())
        self.gpStreetName = QtWidgets.QLineEdit()

        gpCountyLabel = QtWidgets.QLabel(self.tr("&County:"))
        gpCountyLabel.setBuddy(QtWidgets.QLineEdit())
        self.gpCounty = QtWidgets.QLineEdit()

        gpCityLabel = QtWidgets.QLabel(self.tr("&City:"))
        gpCityLabel.setBuddy(QtWidgets.QLineEdit())
        self.gpCity = QtWidgets.QLineEdit()

        gpPostcodeLabel = QtWidgets.QLabel(self.tr("&Postcode:"))
        gpPostcodeLabel.setBuddy(QtWidgets.QLineEdit())
        self.gpPostCode = QtWidgets.QLineEdit()

        gpCountryLabel = QtWidgets.QLabel(self.tr("&Country:"))
        gpCountryLabel.setBuddy(QtWidgets.QLineEdit())
        self.gpCountry = QtWidgets.QComboBox()

        GPGroupBox = QtWidgets.QGroupBox("GP Details")
        gpDetailsGridLayout = QtWidgets.QGridLayout()

        gpDetailsGridLayout.addWidget(gpNameSurgeryNameLabel, 0, 0)
        gpDetailsGridLayout.addWidget(self.gpName, 0, 1)
        gpDetailsGridLayout.addWidget(gpHouseNoLabel, 1, 0)
        gpDetailsGridLayout.addWidget(self.gpHouseNo, 1, 1)
        gpDetailsGridLayout.addWidget(gpStreetNameLabel, 1, 2)
        gpDetailsGridLayout.addWidget(self.gpStreetName, 1, 3)
        gpDetailsGridLayout.addWidget(gpCountyLabel, 1, 4)
        gpDetailsGridLayout.addWidget(self.gpCounty, 1, 5)
        gpDetailsGridLayout.addWidget(gpCityLabel, 1, 6)
        gpDetailsGridLayout.addWidget(self.gpCity, 1, 7)
        gpDetailsGridLayout.addWidget(gpPostcodeLabel, 1, 8)
        gpDetailsGridLayout.addWidget(self.gpPostCode, 1, 9)
        gpDetailsGridLayout.addWidget(gpCountryLabel, 1, 10)
        gpDetailsGridLayout.addWidget(self.gpCountry, 1, 11)

        GPGroupBox.setLayout(gpDetailsGridLayout)

        return GPGroupBox

    def createBankDetails(self):
        bankNameLabel = QtWidgets.QLabel(self.tr("&Bank Name:"))
        bankNameLabel.setBuddy(QtWidgets.QLineEdit())
        self.bankName = QtWidgets.QLineEdit()

        sortCodeLabel = QtWidgets.QLabel(self.tr("&Sort Code:"))
        sortCodeLabel.setBuddy(QtWidgets.QLineEdit())
        self.sortCode = QtWidgets.QLineEdit()

        accountLabel = QtWidgets.QLabel(self.tr("&Account:"))
        accountLabel.setBuddy(QtWidgets.QLineEdit())
        self.account = QtWidgets.QLineEdit()

        ddDateLabel = QtWidgets.QLabel(self.tr("&DD Date:"))
        ddDateLabel.setBuddy(QtWidgets.QLineEdit())
        self.ddDate = QtWidgets.QDateEdit()
        self.ddDate.setDate(QtCore.QDate.currentDate())

        bankDetailsGroupBox = QtWidgets.QGroupBox("Bank Details")
        bankdetailsGridLayout = QtWidgets.QGridLayout()

        bankdetailsGridLayout.addWidget(bankNameLabel, 0, 0)
        bankdetailsGridLayout.addWidget(self.bankName, 0, 1)
        bankdetailsGridLayout.addWidget(sortCodeLabel, 0, 2)
        bankdetailsGridLayout.addWidget(self.sortCode, 0, 3)
        bankdetailsGridLayout.addWidget(self.sortCode, 0, 3)
        bankdetailsGridLayout.addWidget(accountLabel, 0, 4)
        bankdetailsGridLayout.addWidget(self.account, 0, 5)
        bankdetailsGridLayout.addWidget(ddDateLabel, 0, 6)
        bankdetailsGridLayout.addWidget(self.ddDate, 0, 7)

        bankDetailsGroupBox.setLayout(bankdetailsGridLayout)

        return bankDetailsGroupBox

    def createCriticalIlnessCover(self):

        providerLabel = QtWidgets.QLabel("Provider:")
        providerLabel.setBuddy(QtWidgets.QLineEdit())
        self.provider = QtWidgets.QComboBox()
        self.provider.addItem(ProviderEnum.AVIVA)
        self.provider.addItem(ProviderEnum.SUNLIFE)

        policyNumberLabel = QtWidgets.QLabel("Policy Number:")
        self.policyNumber = QtWidgets.QComboBox()
        self.policyNumber.addItem(PolicyNumberEnum.SUNLIFE)
        self.policyNumber.addItem(PolicyNumberEnum.SIS)


        planTypeLabel = QtWidgets.QLabel(self.tr("&Plan Type:"))
        planTypeLabel.setBuddy(QtWidgets.QComboBox())
        self.planType = QtWidgets.QComboBox()
        self.planType.addItem(PlanTypeEnum.INDEXED)
        self.planType.addItem(PlanTypeEnum.DECREASE)
        self.planType.addItem(PlanTypeEnum.LEVEL)

        lifeCoverLabel = QtWidgets.QLabel(self.tr("&Life Cover:"))
        lifeCoverLabel.setBuddy(QtWidgets.QComboBox())
        self.lifeCover = QtWidgets.QComboBox()
        self.lifeCover.addItem(LifeCoverEnum.FIRST_DEATH)
        self.lifeCover.addItem(LifeCoverEnum.SEPARATE)

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
        smoker = QtWidgets.QLabel(self.tr("Smoker:"))
        smokerGroupBox = QtWidgets.QGroupBox()
        smokerHBoxLayout = QtWidgets.QHBoxLayout()
        self.smoker_yes_life_cover_insurance = QtWidgets.QRadioButton("Yes")
        self.smoker_no_life_cover_insurance = QtWidgets.QRadioButton("No")
        self.smoker_no_life_cover_insurance.setChecked(True)
        smokerHBoxLayout.addWidget(smoker)
        smokerHBoxLayout.addWidget(self.smoker_yes_life_cover_insurance)
        smokerHBoxLayout.addWidget(self.smoker_no_life_cover_insurance)
        smokerGroupBox.setLayout(smokerHBoxLayout)

        heightGroupBox = QtWidgets.QGroupBox()
        heightHBoxLayout = QtWidgets.QHBoxLayout()
        heightLabel = QtWidgets.QLabel(self.tr("&Height:"))
        heightLabel.setBuddy(QtWidgets.QLineEdit())
        self.heightLifeInsurance = QtWidgets.QLineEdit()
        self.heightUnitsLifeInsurance = QtWidgets.QComboBox()
        self.heightUnitsLifeInsurance.addItem(HeightUnitEnum.CENTIMETER)
        self.heightUnitsLifeInsurance.addItem(HeightUnitEnum.FEET)
        self.heightUnitsLifeInsurance.addItem(HeightUnitEnum.INCHES)
        self.heightUnitsLifeInsurance.addItem(HeightUnitEnum.METER)
        heightHBoxLayout.addWidget(heightLabel)
        heightHBoxLayout.addWidget(self.heightLifeInsurance)
        heightHBoxLayout.addWidget(self.heightUnitsLifeInsurance)
        heightGroupBox.setLayout(heightHBoxLayout)

        weightGroupBox = QtWidgets.QGroupBox()
        weightHBoxLayout = QtWidgets.QHBoxLayout()
        weightLabel = QtWidgets.QLabel(self.tr("&Weight:"))
        weightLabel.setBuddy(QtWidgets.QLineEdit())
        self.weightLifeInsurance = QtWidgets.QLineEdit()
        self.weightUnitsLifeInsurance = QtWidgets.QComboBox()
        self.weightUnitsLifeInsurance.addItem(WeightUnitEnum.KILOGRAM)
        self.weightUnitsLifeInsurance.addItem(WeightUnitEnum.POUNDS)
        weightHBoxLayout.addWidget(weightLabel)
        weightHBoxLayout.addWidget(self.weightLifeInsurance)
        weightHBoxLayout.addWidget(self.weightUnitsLifeInsurance)
        weightGroupBox.setLayout(weightHBoxLayout)

        familyHealthLabel = QtWidgets.QLabel("Family Health:")
        self.familyHealth = QtWidgets.QLineEdit()
        self.familyHealth.setFixedWidth(300)
        self.familyHealth.setFixedHeight(50)

        healthDetailsLabel = QtWidgets.QLabel("Health Details:")
        self.healthDetails = QtWidgets.QLineEdit()
        self.healthDetails.setFixedWidth(300)
        self.healthDetails.setFixedHeight(50)

        lifeCoverInsuranceGroupBox = QtWidgets.QGroupBox("Critical Serious Insurance")
        lifeInsuranceCoverGridLayout = QtWidgets.QGridLayout()

        lifeInsuranceCoverGridLayout.addWidget(planTypeLabel, 0, 0)
        lifeInsuranceCoverGridLayout.addWidget(self.planType, 0, 1)
        lifeInsuranceCoverGridLayout.addWidget(lifeCoverLabel, 0, 2)
        lifeInsuranceCoverGridLayout.addWidget(self.lifeCover, 0, 3)
        lifeInsuranceCoverGridLayout.addWidget(termCoverLabel, 0, 4)
        lifeInsuranceCoverGridLayout.addWidget(self.termCover, 0, 5)
        lifeInsuranceCoverGridLayout.addWidget(occupationLabel, 0, 6)
        lifeInsuranceCoverGridLayout.addWidget(self.occupation, 0, 7)
        lifeInsuranceCoverGridLayout.addWidget(dutyLabel, 1, 0)
        lifeInsuranceCoverGridLayout.addWidget(self.duty, 1, 1)
        lifeInsuranceCoverGridLayout.addWidget(residencyLabel, 1, 2)
        lifeInsuranceCoverGridLayout.addWidget(self.residency, 1, 3)
        lifeInsuranceCoverGridLayout.addWidget(smokerGroupBox, 1, 4)
        lifeInsuranceCoverGridLayout.addWidget(heightGroupBox, 1, 5)
        lifeInsuranceCoverGridLayout.addWidget(weightGroupBox, 1, 6)
        lifeInsuranceCoverGridLayout.addWidget(familyHealthLabel, 2, 0)
        lifeInsuranceCoverGridLayout.addWidget(self.familyHealth, 2, 1)
        lifeInsuranceCoverGridLayout.addWidget(healthDetailsLabel, 2, 2)
        lifeInsuranceCoverGridLayout.addWidget(self.healthDetails, 2, 3)

        lifeCoverInsuranceGroupBox.setLayout(lifeInsuranceCoverGridLayout)

        return lifeCoverInsuranceGroupBox

    def createLifeInsuranceCover(self):

        providerLabel = QtWidgets.QLabel("Provider:")
        providerLabel.setBuddy(QtWidgets.QLineEdit())
        self.provider = QtWidgets.QComboBox()
        self.provider.addItem(ProviderEnum.AVIVA)
        self.provider.addItem(ProviderEnum.SUNLIFE)

        policyNumberLabel = QtWidgets.QLabel("Policy Number:")
        self.policyNumber = QtWidgets.QComboBox()
        self.policyNumber.addItem(PolicyNumberEnum.SUNLIFE)
        self.policyNumber.addItem(PolicyNumberEnum.SIS)



        planTypeLabel = QtWidgets.QLabel(self.tr("Plan Type:"))
        planTypeLabel.setBuddy(QtWidgets.QComboBox())
        self.planTypeLifeInsurance = QtWidgets.QComboBox()
        self.planTypeLifeInsurance.addItem(PlanTypeEnum.INDEXED)
        self.planTypeLifeInsurance.addItem(PlanTypeEnum.DECREASE)
        self.planTypeLifeInsurance.addItem(PlanTypeEnum.LEVEL)

        lifeCoverLabel = QtWidgets.QLabel(self.tr("&Life Cover:"))
        lifeCoverLabel.setBuddy(QtWidgets.QComboBox())
        self.lifeCoverLifeInsurance = QtWidgets.QComboBox()
        self.lifeCoverLifeInsurance.addItem(LifeCoverEnum.FIRST_DEATH)
        self.lifeCoverLifeInsurance.addItem(LifeCoverEnum.SEPARATE)

        termCoverLabel = QtWidgets.QLabel("Term Of Cover:")
        self.termCoverLifeInsurance = QtWidgets.QLineEdit()

        occupationLabel = QtWidgets.QLabel(self.tr("&Occupation:"))
        occupationLabel.setBuddy(QtWidgets.QLineEdit())
        self.occupationLifeInsurance = QtWidgets.QLineEdit()

        dutyLabel = QtWidgets.QLabel(self.tr("&Duty:"))
        dutyLabel.setBuddy(QtWidgets.QLineEdit())
        self.dutyLifeInsurance = QtWidgets.QLineEdit()

        residencyLabel = QtWidgets.QLabel(self.tr("&Residency:"))
        residencyLabel.setBuddy(QtWidgets.QLineEdit())
        self.residencyLifeInsurance = QtWidgets.QLineEdit()

        smoker = QtWidgets.QLabel(self.tr("Smoker:"))
        smokerGroupBox = QtWidgets.QGroupBox()
        smokerHBoxLayout = QtWidgets.QHBoxLayout()
        self.smoker_yes_life_cover_insurance = QtWidgets.QRadioButton("Yes")
        self.smoker_no_life_cover_insurance = QtWidgets.QRadioButton("No")
        self.smoker_no_life_cover_insurance.setChecked(True)
        smokerHBoxLayout.addWidget(smoker)
        smokerHBoxLayout.addWidget(self.smoker_yes_life_cover_insurance)
        smokerHBoxLayout.addWidget(self.smoker_no_life_cover_insurance)
        smokerGroupBox.setLayout(smokerHBoxLayout)

        heightGroupBox = QtWidgets.QGroupBox()
        heightHBoxLayout = QtWidgets.QHBoxLayout()
        heightLabel = QtWidgets.QLabel(self.tr("&Height:"))
        heightLabel.setBuddy(QtWidgets.QLineEdit())
        self.heightLifeInsurance = QtWidgets.QLineEdit()
        self.heightUnitsLifeInsurance = QtWidgets.QComboBox()
        self.heightUnitsLifeInsurance.addItem(HeightUnitEnum.CENTIMETER)
        self.heightUnitsLifeInsurance.addItem(HeightUnitEnum.FEET)
        self.heightUnitsLifeInsurance.addItem(HeightUnitEnum.INCHES)
        self.heightUnitsLifeInsurance.addItem(HeightUnitEnum.METER)
        heightHBoxLayout.addWidget(heightLabel)
        heightHBoxLayout.addWidget(self.heightLifeInsurance)
        heightHBoxLayout.addWidget(self.heightUnitsLifeInsurance)
        heightGroupBox.setLayout(heightHBoxLayout)

        weightGroupBox = QtWidgets.QGroupBox()
        weightHBoxLayout = QtWidgets.QHBoxLayout()
        weightLabel = QtWidgets.QLabel(self.tr("&Weight:"))
        weightLabel.setBuddy(QtWidgets.QLineEdit())
        self.weightLifeInsurance = QtWidgets.QLineEdit()
        self.weightUnitsLifeInsurance = QtWidgets.QComboBox()
        self.weightUnitsLifeInsurance.addItem(WeightUnitEnum.KILOGRAM)
        self.weightUnitsLifeInsurance.addItem(WeightUnitEnum.POUNDS)
        weightHBoxLayout.addWidget(weightLabel)
        weightHBoxLayout.addWidget(self.weightLifeInsurance)
        weightHBoxLayout.addWidget(self.weightUnitsLifeInsurance)
        weightGroupBox.setLayout(weightHBoxLayout)

        familyHealthLabel = QtWidgets.QLabel("Family Health:")
        self.familyHealthLifeInsurance = QtWidgets.QLineEdit()
        self.familyHealthLifeInsurance.setFixedWidth(300)
        self.familyHealthLifeInsurance.setFixedHeight(50)

        healthDetailsLabel = QtWidgets.QLabel("Health Details:")
        self.healthDetailsLifeInsurance = QtWidgets.QLineEdit()
        self.healthDetailsLifeInsurance.setFixedWidth(300)
        self.healthDetailsLifeInsurance.setFixedHeight(50)

        lifeCoverInsuranceGroupBox = QtWidgets.QGroupBox("Life Cover Insurance")
        lifeInsuranceCoverGridLayout = QtWidgets.QGridLayout()

        lifeInsuranceCoverGridLayout.addWidget(providerLabel, 0, 0)
        lifeInsuranceCoverGridLayout.addWidget(self.provider, 0, 1)
        lifeInsuranceCoverGridLayout.addWidget(policyNumberLabel, 0, 2)
        lifeInsuranceCoverGridLayout.addWidget(self.policyNumber, 0, 3)

        lifeInsuranceCoverGridLayout.addWidget(planTypeLabel, 0, 4)
        lifeInsuranceCoverGridLayout.addWidget(self.planTypeLifeInsurance, 0, 5)
        lifeInsuranceCoverGridLayout.addWidget(lifeCoverLabel, 1, 0)
        lifeInsuranceCoverGridLayout.addWidget(self.lifeCoverLifeInsurance, 1, 1)
        lifeInsuranceCoverGridLayout.addWidget(termCoverLabel, 1, 2)
        lifeInsuranceCoverGridLayout.addWidget(self.termCoverLifeInsurance, 1, 3)
        lifeInsuranceCoverGridLayout.addWidget(occupationLabel, 1, 4)
        lifeInsuranceCoverGridLayout.addWidget(self.occupationLifeInsurance, 1, 5)
        lifeInsuranceCoverGridLayout.addWidget(dutyLabel, 1, 6)
        lifeInsuranceCoverGridLayout.addWidget(self.dutyLifeInsurance, 2, 0)
        lifeInsuranceCoverGridLayout.addWidget(residencyLabel, 2, 1)
        lifeInsuranceCoverGridLayout.addWidget(self.residencyLifeInsurance, 2, 2)
        lifeInsuranceCoverGridLayout.addWidget(smokerGroupBox, 2, 4)
        lifeInsuranceCoverGridLayout.addWidget(heightGroupBox, 2, 5)
        lifeInsuranceCoverGridLayout.addWidget(weightGroupBox, 2, 6)
        lifeInsuranceCoverGridLayout.addWidget(familyHealthLabel, 3, 0)
        lifeInsuranceCoverGridLayout.addWidget(self.familyHealthLifeInsurance, 3, 1)
        lifeInsuranceCoverGridLayout.addWidget(healthDetailsLabel, 3, 2)
        lifeInsuranceCoverGridLayout.addWidget(self.healthDetailsLifeInsurance, 3, 3)

        lifeCoverInsuranceGroupBox.setLayout(lifeInsuranceCoverGridLayout)

        return lifeCoverInsuranceGroupBox

    def createReference(self):
        referneceGridLayout = QtWidgets.QHBoxLayout()
        referneceGridLayout.addStretch(2)

        date = QtWidgets.QLabel("Date:")
        self.reference_date = QtWidgets.QDateEdit()
        self.reference_date.setDate(QtCore.QDate.currentDate())

        reference = QtWidgets.QLabel("Reference:")
        self.reference_id = QtWidgets.QComboBox()


        referenceGroupBox = QtWidgets.QGroupBox("")

        referneceGridLayout.addWidget(date)
        referneceGridLayout.addWidget(self.reference_date)
        referneceGridLayout.addWidget(reference)
        referneceGridLayout.addWidget(self.reference_id)

        referneceGridLayout.setAlignment(QtCore.Qt.AlignLeft)

        referenceGroupBox.setLayout(referneceGridLayout)

        return referenceGroupBox

class FormWidget(QtWidgets.QWidget):

    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout(self)

        button_width = 150
        button_height = 150

        self.payment_every_15_days_btn = QtWidgets.QPushButton("Report Every Payment 15 days")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.payment_every_15_days_btn.setIcon(icon)
        self.layout.addWidget(self.payment_every_15_days_btn)

        self.pushButton = QtWidgets.QPushButton("Report List of Client for Insurance Due")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/report2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.layout.addWidget(self.pushButton)

        self.button2 = QtWidgets.QPushButton("Report List of Client for Insurance Due")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/report3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button2.setIcon(icon)
        self.layout.addWidget(self.button2)

        self.button3 = QtWidgets.QPushButton("Payment to an employee/referee on a payment date")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/report4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button3.setIcon(icon)
        self.layout.addWidget(self.button3)

        self.setLayout(self.layout)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("SafeLife Insurance Ltd.")
        self.setFixedWidth(1000)
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")

        quit = QtWidgets.QAction("Quit", self)
        file.addAction(quit)

        tools = bar.addMenu("Tools")
        tools.addAction("Search Client")

        layout = QtWidgets.QVBoxLayout()
        singleton_widget = QtWidgets.QWidget()
        singleton_widget.setLayout(layout)
        geometery = QtWidgets.QDesktopWidget().availableGeometry()
        self.setFixedSize(geometery.width(), geometery.height())
        self.setWindowIcon(QtGui.QIcon("./images/safelifeLogo.png"));
        self.setCentralWidget(singleton_widget)

        toolbar = QtWidgets.QToolBar('Main toolbar')
        self.addToolBar(toolbar)

        icon = QtGui.QIcon("./images/employee.png")
        new_advisor = QtWidgets.QAction(icon, "New Employee", self)
        new_advisor.setStatusTip('New Advisor')
        new_advisor.setCheckable(False)
        toolbar.addAction(new_advisor)

        icon = QtGui.QIcon("./images/employee.png")
        update_advisor = QtWidgets.QAction(icon, "Update Employee", self)
        update_advisor.setStatusTip('Update Advisor')
        update_advisor.setCheckable(False)
        toolbar.addAction(update_advisor)

        icon = QtGui.QIcon("./images/employee.png")
        archive_advisor = QtWidgets.QAction(icon, "Delete Employee", self)
        archive_advisor.setStatusTip('Archive Advisor')
        archive_advisor.setCheckable(False)
        toolbar.addAction(archive_advisor)
        toolbar.addSeparator()

        icon = QtGui.QIcon("./images/girl.png")
        new_referral = QtWidgets.QAction(icon, "New Referral", self)
        new_referral.setStatusTip('New Referral')
        new_referral.setCheckable(False)
        toolbar.addAction(new_referral)

        icon = QtGui.QIcon("./images/girl.png")
        update_referral = QtWidgets.QAction(icon, "Update Referral", self)
        update_referral.setStatusTip('Update Referral')
        update_referral.setCheckable(False)
        toolbar.addAction(update_referral)

        icon = QtGui.QIcon("./images/girl.png")
        delete_referral = QtWidgets.QAction(icon, "Delete Referral", self)
        delete_referral.setStatusTip('Delete Referral')
        delete_referral.setCheckable(False)
        toolbar.addAction(delete_referral)

        toolbar.addSeparator()

        icon = QtGui.QIcon("./images/multiple-users.png")
        new_client = QtWidgets.QAction(icon, 'New Client', self)
        new_client.setStatusTip('New Client')
        new_client.triggered.connect(self.newClient)
        new_client.setCheckable(False)
        toolbar.addAction(new_client)

        icon = QtGui.QIcon("./images/multiple-users.png")
        update_client = QtWidgets.QAction(icon, 'Update Client', self)
        update_client.setStatusTip('Update Client')
        update_client.setCheckable(False)
        toolbar.addAction(update_client)

        icon = QtGui.QIcon("./images/multiple-users.png")
        delete_client = QtWidgets.QAction(icon, 'Delete Client', self)
        delete_client.setStatusTip('Delete Client')
        delete_client.setCheckable(False)
        toolbar.addAction(delete_client)
        toolbar.setFloatable(True)
        toolbar.addSeparator()

        self.form_widget = FormWidget(self)
        self.setCentralWidget(self.form_widget)

        self.statusBar().showMessage("Ready", 5000)

    def newClient(self):
        NewClientFormDialog().exec_()

    def contextMenuEvent(self, event):
        print('Context menu event happened!')


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

    app = QtWidgets.QApplication(sys.argv)
    pixmap = QtGui.QPixmap("./images/safelifeLogo.png")
    splash = QtWidgets.QSplashScreen(pixmap)
    splash.show()
    splash.showMessage("<p style='color: red;'>Loaded modules</p>")
    splash.showMessage("Starting Safelife Insurance Ltd.")

    window = MainWindow()
    window.show()

    splash.finish(window)

    # Start the event loop.
    app.exec_()
