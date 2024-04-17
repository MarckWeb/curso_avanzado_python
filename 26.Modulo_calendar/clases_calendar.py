from datetime import *
import locale
import calendar

# Usando Calendar
cal = calendar.Calendar()
print("Días de abril de 2024:")
for date in cal.itermonthdates(2024, 4):
    print(date)

# Usando TextCalendar
text_cal = calendar.TextCalendar()
print(text_cal.formatmonth(2024, 4))

# Usando HTMLCalendar
html_cal = calendar.HTMLCalendar(calendar.SUNDAY)
print(html_cal.formatmonth(2024, 4))
# Abrimos en un archivo html
# with open("calendar.html", "w") as file:
#     file.write(html_cal.formatyear(2024))


# Mostramos el calendario en español local al pais
local_calendar = calendar.LocaleTextCalendar()
print(local_calendar.formatmonth(2024, 4))


# Pra colocar el calendario en formato de algun pais(sueco)
l = locale.setlocale(locale.LC_ALL, 'sv_SE')
c = calendar.LocaleTextCalendar(locale=l)
print(c.formatmonth(2024, 4))
