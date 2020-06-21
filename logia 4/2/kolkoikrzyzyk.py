def kk(slowo):
    return 'prawda' if abs(slowo.count('x')-slowo.count('o')) <= 1 else 'falsz'

print(
kk("xwxoxooww"),
kk("xxwowowwo"),
kk("xxoowooww")
)
