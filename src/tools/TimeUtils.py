from datetime import datetime, timedelta

class TimeUtils:
    @staticmethod
    def current_time():
        """获取当前时间"""
        return datetime.now()

    @staticmethod
    def format_time(dt, format_string="%Y-%m-%d %H:%M:%S"):
        """格式化时间"""
        return dt.strftime(format_string)

    @staticmethod
    def add_days(dt, days):
        """在日期上加上指定的天数"""
        return dt + timedelta(days=days)
