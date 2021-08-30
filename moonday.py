from korean_lunar_calendar import KoreanLunarCalendar

def get_luna_date(year,month,day):
    calendar = KoreanLunarCalendar()
    # params : year(년), month(월), day(일)
    calendar.setSolarDate(year, month, day)
    # Lunar Date (ISO Format)
    print("양력>음력", calendar.LunarIsoFormat(), "입니다.")
    return calendar.LunarIsoFormat()

if __name__ == "__main__":
    print(type(get_luna_date(2020,8,8)))