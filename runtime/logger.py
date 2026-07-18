from datetime import datetime


class RuntimeLogger:

    @staticmethod
    def line():
        print("\n" + "-" * 60)

    @staticmethod
    def title(title: str):

        RuntimeLogger.line()

        print(f"[{datetime.now().strftime('%H:%M:%S')}] {title}")

        RuntimeLogger.line()

    @staticmethod
    def info(message: str):

        print(message)