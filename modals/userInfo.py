class UserInfo :
    def __init__(
        self,
        kullaniciID,
        kullaniciAdi,
        kullaniciSoyadi,
        kullaniciMail,
        kullaniciSifre
        ) :
        if(kullaniciID == None):
            kullaniciID = 0
            
        self.kullaniciID = kullaniciID
        self.kullaniciAdi = kullaniciAdi
        self.kullaniciSoyadi = kullaniciSoyadi
        self.kullaniciMail = kullaniciMail
        self.kullaniciSifre = kullaniciSifre
