#!/usr/bin/python3
# tests/test_models/__init__.py
from models.base_model import BaseModel
from models.engine import file_storage
# Import statements for the modules you want to test
from .test_base_model import *
from models import *
# Add more imports for other test modules if needed
