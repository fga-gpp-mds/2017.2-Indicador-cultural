from django.db import models
from mongoengine import *

# -------------------- state indicators --------------------------------

class PercentThematicsMuseumsForState:
    __thematicsMuseumsForState = MapField(required = True)
    __totalMuseumsForState = MapField(required = True)

    @property
    def thmeaticsMuseumsForState(self):
        return self._thematicsMuseumsForState

    @thmeaticsMuseumsForState.setter
    def thmeaticsMuseumsForState(self,number):
        self._thematicsMuseumsForState = number

    @property
    def totalMuseumsForState(self):
        return self._totalMuseumsForState

    @totalMuseumsForState.setter
    def totalMuseumsForState(self,number):
        self._totalMuseumsForState = number

class PercentTypeMuseumsForState:
    __typeMuseumsForState = MapField(required = True)
    __totalMuseumsForState = MapField(required = True)

    @property
    def typeMuseumsForState(self):
        return self._typeMuseumsForState

    @typeMuseumsForState.setter
    def typeMuseumsForState(self,number):
        self._typeMuseumsForState = number

    @property
    def totalMuseumsForState(self):
        return self._totalMuseumsForState

    @totalMuseumsForState.setter
    def totalMuseumsForState(self,number):
        self._totalMuseumsForState = number


class PercentPublicOrPrivateMuseumsForState:
    _totalPublicMuseumsForState = mapField(required = True)
    _totalPrivateMuseumsForState = mapField(required = True)
    _totalMuseumsForState = mapField(required = True)

    @property
    def totalPublicMuseumsForState(self):
        return self._totalPublicMuseumsForState

    @totalPublicMuseumsForState.setter
    def totalPublicMuseumsForState(self,number):
        self._totalPublicMuseumsForState = number

    @property
    def totalPrivateMuseumsForState(self):
        return self._totalPrivateMuseumsForState

    @totalPrivateMuseumsForState.setter
    def totalPrivateMuseumsForState(self,number):
        self._totalPrivateMuseumsForState = number

    @property
    def totalMuseumsForState(self):
        return self._totalMuseumsForState

    @totalMuseumsForState.setter
    def totalMuseumsForState(self, number):
        self._totalMuseumsForState = number

class PercentMuseumsHistoricalArchivePublicAccessForState:
    _totalMuseumsHistoricalArchivePublicAccessForState = mapField(required = True)
    _totalMuseumsForState = mapField(required = True)

    @property
    def totalMuseumsHistoricalArchivePublicAccessForState(self):
        return self._totalMuseumsHistoricalArchivePublicAccessForState

    @totalMuseumsHistoricalArchivePublicAccessForState.setter
    def totalMuseumsHistoricalArchivePublicAccessForState(self, number):
        self._totalMuseumsHistoricalArchivePublicAccessForState = number

    @property
    def totalMuseumsForState(self):
        return self._totalMuseumsForState

    @totalMuseumsForState.setter
    def totalMuseumsForState(self, number):
        self._totalMuseumsForState = number

class PercentMuseumsPromoteGuidedTourForState:
    _totalMuseumsPromoteGuidedTourForState = mapField(required = True)
    _totalMuseumsForState = mapField(required = True)

    @property
    def totalMuseumsPromoteGuidedTourForState(self):
        return self._totalMuseumsPromoteGuidedTourForState

    @totalMuseumsPromoteGuidedTourForState.setter
    def totalMuseumsPromoteGuidedTourForState(self, number):
        self._totalMuseumsPromoteGuidedTourForState = number

    @property
    def totalMuseumsForState(self):
        return self._totalMuseumsForState

    @totalMuseumsForState.setter
    def totalMuseumsForState(self, number):
        self._totalMuseumsForState = number

# --------------------- national indicators ----------------------------------

class PercentThematicsMuseums:
    __thematicsMuseums = intField(required = True)
    __totalMuseums = intField(required = True)

    @property
    def thmeaticsMuseums(self):
        return self._thematicsMuseums

    @thmeaticsMuseums.setter
    def thmeaticsMuseums(self,number):
        self._thematicsMuseums = number

    @property
    def totalMuseums(self):
        return self._totalMuseums

    @totalMuseums.setter
    def totalMuseums(self,number):
        self._totalMuseums = number

class PercentTypeMuseums:
    __typeMuseums = intField(required = True)
    __totalMuseums = intField(required = True)

    @property
    def typeMuseums(self):
        return self._typeMuseums

    @typeMuseums.setter
    def typeMuseums(self,number):
        self._typeMuseums = number

    @property
    def totalMuseums(self):
        return self._totalMuseums

    @totalMuseums.setter
    def totalMuseums(self,number):
        self._totalMuseums = number

class PercentPublicOrPrivateMuseums:
    _totalPublicMuseums = intField(required = True)
    _totalPrivateMuseums = intField(required = True)
    _totalMuseums = intField(required = True)

    @property
    def totalPublicMuseums(self):
        return self._totalPublicMuseums

    @totalPublicMuseums.setter
    def totalPublicMuseums(self,number):
        self._totalPublicMuseums = number

    @property
    def totalPrivateMuseums(self):
        return self._totalPrivateMuseums

    @totalPrivateMuseums.setter
    def totalPrivateMuseums(self,number):
        self._totalPrivateMuseums = number

    @property
    def totalMuseums(self):
        return self._totalMuseums

    @totalMuseums.setter
    def totalMuseums(self, number):
        self._totalMuseums = number

class PercentMuseumsHistoricalArchivePublicAccess:
    _totalMuseumsHistoricalArchivePublicAccess = intField(required = True)
    _totalMuseums = intField(required = True)

    @property
    def totalMuseumsHistoricalArchivePublicAccess(self):
        return self._totalMuseumsHistoricalArchivePublicAccess

    @totalMuseumsHistoricalArchivePublicAccess.setter
    def totalMuseumsHistoricalArchivePublicAccess(self, number):
        self._totalMuseumsHistoricalArchivePublicAccess = number

    @property
    def totalMuseums(self):
        return self._totalMuseums

    @totalMuseums.setter
    def totalMuseums(self, number):
        self._totalMuseums = number

class PercentMuseumsPromoteGuidedTour:
    _totalMuseumsPromoteGuidedTour = intField(required = True)
    _totalMuseums = intField(required = True)

    @property
    def totalMuseumsPromoteGuidedTour(self):
        return self._totalMuseumsPromoteGuidedTour

    @totalMuseumsPromoteGuidedTour.setter
    def totalMuseumsPromoteGuidedTour(self, number):
        self._totalMuseumsPromoteGuidedTour = number

    @property
    def totalMuseums(self):
        return self._totalMuseums

    @totalMuseums.setter
    def totalMuseums(self, number):
        self._totalMuseums = number

# Amount of Museums registered per year on the platform throughout its existence
class AmountMuseumsRegisteredYear:
    _totalMuseumsRegisteredYear = mapField(required = True)

    @property
    def totalMuseumsRegisteredYear(self):
        return self._totalMuseumsRegisteredYear

    @totalMuseumsRegisteredYear.setter
    def totalMuseumsRegisteredYear(self, number):
        self._totalMuseumsRegisteredYear = number

# Amount of Museums registered per month on the platform throughout its existence
class AmountMuseumsRegisteredMonth:
    _totalMuseumsRegisteredMonth = mapField(required = True)

    @property
    def totalMuseumsRegisteredMonth(self):
        return self._totalMuseumsRegisteredMonth

    @totalMuseumsRegisteredMonth.setter
    def totalMuseumsRegisteredMonth(self, number):
        self._totalMuseumsRegisteredMonth = number

# Percentage of museums by states
class PercentMuseumsForState:
    _totalMuseumsForState = mapField(required = True)
    _totalMuseums = intField(required = True)

    @property
    def totalMuseumsForState(self):
        return self._totalMuseumsForState

    @totalMuseumsForState.setter
    def totalMuseumsForState(self, number):
        self._totalMuseumsForState = number

    @property
    def totalMuseums(self):
        return self._totalMuseums

    @totalMuseums.setter
    def totalMuseums(self, number):
        self._totalMuseums = number
