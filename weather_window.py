from PyQt5.QtWidgets import (QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

from weather_service import get_weather 

from weather_utils import kelvin_to_fahrenheit

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self )

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)


        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)


        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: futura;
            }    
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;     
            }
                           
            QPushButton#get_weather_button{
                font-size: 30px;
                
            }
            QLabel#temperature_label{
                font-size: 40px           
            }
            QLabel#emoji_label{
                font-size: 80px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 40px
            }
                           
            

    
        """)

        self.get_weather_button.clicked.connect(self.get_weather)
    
    def get_weather(self):

        city = self.city_input.text()

        try:
            data = get_weather(city)
            self.display_weather(data)

        except Exception as e:
            self.display_error(str(e))
        

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px")
        self.temperature_label.setText(message)
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 40px")
        temperature_k = data["main"]['temp']

        temperature_f = kelvin_to_fahrenheit(temperature_k)
        
        self.temperature_label.setText(f"{temperature_f:.0f}°F")

        weather_description = data["weather"][0]["description"]
        self.description_label.setText(weather_description)