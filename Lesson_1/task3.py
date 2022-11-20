second = int(input("write second: "))
#calculate seconds
print(" sec " + str(second%60))
#calculate minute
print(" min " + str(second//60%60))
#calculate hour
print(" h " + str(second//3600%60))
#calculate day
print(" d " + str(second//86400))

