from mongoengine import Document
from mongoengine import DictField
from mongoengine import IntField
from mongoengine import DateTimeField

# --------------------- national indicators ----------------------------------

class PercentEvent(Document):
    class Meta:
        abstract = True

    _total_events = IntField(required=True)
    _create_date = DateTimeField(required=True)

    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, number):
        self._create_date = number


    @property
    def total_events(self):
        return self._total_events

    @total_events.setter
    def total_events(self, number):
        self._total_events = number

class PercentEventState(Document):
    class Meta:
        abstract = True
    _total_state_events = DictField(required=True)
    _create_date = DateTimeField(required=True)

    @property
    def total_state_events(self):
        return self._total_state_events

    @total_state_events.setter
    def total_state_events(self, number):
        self._total_state_events = number

    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, number):
        self._create_date = number


class PercentEventsPerLanguage(PercentEvent):
    _total_events_per_language = DictField(required=True)


    @property
    def total_events_per_language(self):
        return self._tota_events_per_language

    @total_events_per_language.setter
    def total_events_per_language(self, number):
        self._total_events_per_language = number


class PercentEventsPerAgeRange(PercentEvent):
    _total_events_per_age_range = DictField(required=True)

    @property
    def total_events_per_age_range(self):
        return self._total_events_per_age_range

    @total_events_per_age_range.setter
    def total_events_per_age_range(self, number):
        self._total_events_per_age_range = number



# -------------------- state indicators --------------------------------------


class PercentTypeEventsForState(PercentEvent):
    _type_state_events = DictField(required=True)


    @property
    def type_state_events(self):
        return self._type_state_events

    @type_state_events.setter
    def type_state_events(self, number):
        self._type_state_events = number




class PercentEventsPerLanguagePerState(Document):
    _totalEventsPerState = DictField(required=True)
    _totaEventsPerLanguagePerState = DictField(required=True)
    _createDate = DateTimeField(required=True)

    @property
    def total_events_per_state(self):
        return self._totalEventsPerState

    @total_events_per_state.setter
    def total_events_per_state(self, number):
        self._totalEvents = number

    @property
    def total_events_per_language_per_state(self):
        return self._totalEventsPerLanguage

    @total_events_per_language_per_state.setter
    def total_events_per_language_per_state(self, number):
        self._totalEventsPerLanguage = number

    @property
    def create_date(self):
        return self._createDate

    @create_date.setter
    def create_date(self, number):
        self._createDate = number


class PercentEventsPerAgeRangePerState(Document):
    _totalEventsPerAgeRangePerState = DictField(required=True)
    _totalEventsPerState = IntField(required=True)
    _createDate = DateTimeField(required=True)

    @property
    def total_events_per_state(self):
        return self._totalEventsPerState

    @total_events_per_state.setter
    def total_events_per_state(self, number):
        self._totalEventsPerState = number

    @property
    def total_events_per_age_range_per_state(self):
        return self._totalEventsPerAgeRangePerState

    @total_events_per_age_range_per_state.setter
    def total_events_per_age_range(self, number):
        self._totalEventsPerAgeRangePerState = number

    @property
    def create_date(self):
        return self._createDate

    @create_date.setter
    def create_date(self, number):
        self._createDate = number

# -------------------- Events Registered --------------------------------------


class QuantityOfRegisteredEvents(Document):
    _totalEventsRegisteredPerMounthPerYear = DictField(required=True)
    _totalEventsRegisteredPerYear = DictField(required=True)
    _totalEvents = IntField(required=True)
    _createDate = DateTimeField(required=True)

    @property
    def total_events_registered_per_mounth_per_year(self):
        return self._totalEventsRegisteredPerMounthPerYear

    @total_events_registered_per_mounth_per_year.setter
    def total_events_registered_per_mounth_per_year(self, number):
        self._totalEventsRegisteredPerMounthPerYear = number

    @property
    def total_events_registered_per_year(self):
        return self._totalEventsRegisteredPerYear

    @total_events_registered_per_year.setter
    def total_events_registered_per_year(self, number):
        self._totalEventsRegisteredPerYear = number

    @property
    def total_events(self):
        return self._totalEvents

    @total_events.setter
    def total_events(self, number):
        self._totalEvents = number

    @property
    def create_date(self):
        return self._createDate

    @create_date.setter
    def create_date(self, number):
        self._createDate = number
