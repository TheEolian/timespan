##########################################################################
# Setting Timespan for Annual Job Run
##########################################################################

from datetime import datetime

currentYear = datetime.now().year
priorYear = currentYear - 1

start_date = f"{priorYear}-01-01"
end_date = f"{priorYear}-12-31"

##########################################################################
# Setting Timespan for Quarterly Job Run
##########################################################################

from datetime import datetime

currentMonth = datetime.now().month
currentYear = datetime.now().year
priorYear = currentYear - 1

# Q4 RUN IN Q1
if currentMonth < 4:
    start_date = f"{priorYear}-10-01"
    end_date = f"{priorYear}-12-31"
# Q1 RUN IN Q2
elif (currentMonth > 3) & (currentMonth < 7):
    start_date = f"{currentYear}-01-01"
    end_date = f"{currentYear}-03-31"
# Q2 RUN IN Q3
elif (currentMonth > 6) & (currentMonth < 10):
    start_date = f"{currentYear}-04-01"
    end_date = f"{currentYear}-06-30"
# Q3 RUN IN Q4
elif currentMonth > 9:
    start_date = f"{currentYear}-07-01"
    end_date = f"{currentYear}-10-31"
else:
    print("Error Setting Date Range")

##########################################################################
# BI-ANNUAL RUN
##########################################################################

# Run Half prior to Current Half

from datetime import datetime

currentMonth = datetime.now().month
currentYear = datetime.now().year
priorYear = currentYear - 1

if currentMonth < 7:
    start_date = f"{priorYear}-07-01"
    end_date = f"{priorYear}-12-31"
elif currentMonth > 7:
    start_date = f"{currentYear}-01-01"
    end_date = f"{currentYear}-06-30"
else:
    print("Error Setting Date Range")
