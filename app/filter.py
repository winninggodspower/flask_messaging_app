from app import app
import timeago, datetime

@app.template_filter('time_ago')
def time_ago(date):
    now = datetime.datetime.now()
    return timeago.format(date, now)
