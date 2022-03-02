"""Class Time with read-write properties."""

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    @property
    def hour(self):
        """Return the value for hour"""
        return self._hour

    @hour.setter
    def hour(self, hour):
        """Set the value for hour"""
        if not (0 <= hour < 24):
            raise ValueError('Hour should be between 0-23')
        self._hour = hour
    
    @property
    def minute(self):
        """Return value for minute"""
        return self._minute

    @minute.setter
    def minute(self, minute):
        """Set the value for minute"""
        if not (0 <= minute < 60):
            raise ValueError('Minute should be between 0-59') 
        self._minute = minute

    @property
    def second(self):
        """Return value for second"""
        return self._second

    @second.setter
    def second(self, second):
        """Set the value for second"""
        if not (0 <= second < 60):
            raise ValueError('Second should be between 0-59') 
        self._second = second

    @property
    def time(self):
        """Return the value for time"""
        return (self.hour, self.minute, self.second)

    @time.setter
    def time(self, time_tuple):
        """Access tuple and set value for hour, minute and second"""
        if not len(time_tuple) == 3:
            raise ValueError('Time tuple should have three arguments')
        self.set_time(*time_tuple)

    def set_time(self, hour=0, minute=0, second=0):
        """Sets the time in hour, minute and second"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        """Return Time string for repr()."""
        return (f'Time(hour={self.hour}, minute={self.minute}, ' + 
                f'second={self.second})')

    def __str__(self):
        """Return Time string in 12-hour clock format."""
        return (('12' if self.hour in (0, 12) else str(self.hour % 12)) + 
                f':{self.minute:0>2}:{self.second:0>2}' + 
                (' AM' if self.hour < 12 else ' PM'))