# A tuple that stores the months of the year, followed by another tuple that stores the summer months which are printed
# Author: Andrew Scott

months = ("January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
)

summer = months[4:7]
for month in summer:
    print(month)