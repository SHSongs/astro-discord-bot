from korean_lunar_calendar import KoreanLunarCalendar

calendar = KoreanLunarCalendar()
# params : year(년), month(월), day(일)
calendar.setSolarDate(2021, 9, 6)
# Lunar Date (ISO Format)
print("양력>음력", calendar.LunarIsoFormat(), "입니다.")
