"""(**************
KULLANICI GİRİŞİ
*****************)
"""

sys_kullanıcı_adı = "extar"
sys_parola = "12345"

kullanıcı_adı=input("kullanıcı adı:")
parola = input("parola:")

if (kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola ):
    print("parola hatalı")
elif (kullanıcı_adı != sys_kullanıcı_adı and sys_parola == parola):
    print("kullanıcı adı hatalı")
elif (kullanıcı_adı != sys_kullanıcı_adı and sys_parola != parola):
    print("kullanıcı adı ve parola hatalı")
else:
    print("başarı ile giriş yapıldı")