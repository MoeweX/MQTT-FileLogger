from setuptools import setup

setup(
    name="MQTT-FileLogger",
    version="0.0.1",
    python_requires='>3.6.0',
    packages=["mqtt_filelogger"],
    url="https://github.com/MoeweX/mqtt_filelogger.git",
    license="MIT",
    author="Jonathan Hasenburg",
    author_email="",
    description="Service to log mqtt messages to csv files.",
    install_requires=[
        "paho-mqtt",
        "toml"
    ]
)
