from datetime import datetime, timezone, timedelta


def hours_to_now(self, created_at):
    now = datetime.utcnow()
    return (now - created_at).seconds/3600
