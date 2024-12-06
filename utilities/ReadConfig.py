import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('general info', 'baseURL')
        return url

    @staticmethod
    def get_working_directory():
        working_dir = config.get('general info', 'workingDirectory')
        return working_dir
