from plyer import notification
import psutil
import time

#معلومات البطرية
battery = psutil.sensors_battery()
charging = battery.power_plugged
charge_percentage = battery.percent

#ومتغير وقت الإنتظار حتى التذكير الآخر متغير عدد تكرار 
NUM_BLINKS = 1  

# متغير لمراقبة ما اذا تم ارسال الإشعار فعلا ام لا
notification_sent = False

#دالة ارسال الرسالة 
def btr():
    notification.notify(
    title="تنبيه",
     message ="قم بفصل الشحن الآن"
    )
# كود لتكرار العملية كل ثانية
while True:
    #معلومات البطرية
    battery = psutil.sensors_battery()
    charging = battery.power_plugged
    charge_percentage = battery.percent
    
    if charging== True and charge_percentage ==80 or charge_percentage >=80:
         if notification_sent == False:
              btr()
              notification_sent = True
    else:
        notification_sent = False

    time.sleep(30)