from datetime import datetime, timedelta, UTC

from app.safety.news_blackout_manager import NewsBlackoutManager

manager = NewsBlackoutManager()

manager.add_event(

    "FOMC",

    datetime.now(UTC) + timedelta(minutes=10),

    blackout_before=30,

    blackout_after=30

)

manager.print()

print()

active, event = manager.is_blackout()

print("Trading Allowed:", not active)

print("Blocking Event :", event)