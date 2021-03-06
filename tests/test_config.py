import json
import logging
import os
import joblib
import pytest
from prediction_service.prediction import form_response, ap_response

class NotInRange(Exception):
    def __init__(self, message='Value Not In Range'):
        self.message = message
        super().__init__(self.message)

def test_generic():
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange

