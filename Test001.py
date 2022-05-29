ammoInput = int(input())
zombiesInput = input()
ammoList = zombieHealth = [int(x) for x in zombiesInput.split()]

zombieNum = len(ammoList)
ammoUse = 0
ammoReport=[]

for i in range(len(ammoList)): #แยกซอมบี้ออกมาจากลิส
  while zombieHealth[i] > 0 : #ตรวจว่าตัวนี้ตายหรือยัง
    if zombieHealth[i] > ammoInput: #ตรวจว่าตัวนี้เลือดมากกว่าดาเมจกระสุนหรือไม่
      ammoUse += 1 #ถ้าใช่ก้ใช้กระสุนไป๑นัด
      zombieHealth[i] -= ammoInput #เลือดซอมบี้ก็ลดลงตามดาเมจ
    elif zombieHealth[i] <= ammoInput: #ตรวจว่าตัวนี้เลือดเท่าหรือน้อยกว่าดาเมจกระสุนหรือไม่
      ammoUse += 1 #ถ้าใช่ก้ใช้กระสุนไป๑นัด
      ammoReport.append(ammoUse)#แล้วใส่ลงในลิสรายงาน

print(zombieNum)
print(ammoUse)
print(ammoReport)
