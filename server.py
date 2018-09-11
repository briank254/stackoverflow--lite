"""
v2 application entry point
"""
import os
from app_v2 import create_app

app = create_app(os.getenv('ENV'))

if __name__ == '__main__':
    app.run()
    