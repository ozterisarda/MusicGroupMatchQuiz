import webbrowser
ws = "https://www.youtube.com/watch?v=0mWM0S1dMro&list=PLAx1f0mne98qVZ59ZYHjUE3-hp_MIogpu"
bs = "https://www.youtube.com/watch?v=0qanF-91aJo&list=PLjbeMSuarTQMKSMVYkfUvvTG7YfTDRJRI"
bn = "https://www.youtube.com/watch?v=-nlDy6h-v9c&list=PLA424057908E96379"
ks = "https://www.youtube.com/watch?v=16cEJ-CBejA&list=PLwDmVi51SV_Hy6Kl5TrfM3fTo-_Z1a634"
ab = "https://www.youtube.com/watch?v=-crgQGdpZR0&list=PL8402127C9DE495CB"
ac = "https://www.youtube.com/watch?v=-0Oa5wvARSc&list=PLpZaq7kciiNIscD5bMLUIyesR_EHTSvxu"
su = "https://www.youtube.com/watch?v=1HiG--f604k&list=PL1F0C67883D073645"
pm = "https://www.youtube.com/watch?v=-YD5p-WoR7E&list=PLEIMU-Mdvjj_FpqhczDr8UQqLFu8dxPr1"
nr = "https://www.youtube.com/watch?v=0AJjE53Ura0&list=PLF3FE9FEB122AE2A4"
mp = "https://www.youtube.com/watch?v=1xa7NWRJjPQ&list=PLE1A0255234131C34&pp=0gcJCbAEOCosWNin"

def yt():
    if winners[0] == "Black Sabbath":
        webbrowser.open(bs)
    if winners[0] == "Bon Jovi":
        webbrowser.open(bn)
    if winners[0] == "The White Stripes":
        webbrowser.open(ws)
    if winners[0] == "Kiss":
        webbrowser.open(ks)
    if winners[0] == "ABBA":
        webbrowser.open(ab)
    if winners[0] == "AC/DC":
        webbrowser.open(ac)
    if winners[0] == "Survivor":
        webbrowser.open(su)
    if winners[0] == "Poor Man's Potion":
        webbrowser.open(pm)
    if winners[0] == "Nirvana":
        webbrowser.open(nr)
    if winners[0] == "The Mamas and the Papas":
        webbrowser.open(mp)

while True:
    # Puanları her tur sıfırlayalım.
    blacksabbath = 0
    bonjovi = 0
    kiss = 0
    abba = 0
    acdc = 0
    survivor = 0
    poormanspotion = 0
    nirvana = 0
    mamasandpapas = 0
    whitestripes = 0
    # Kullanıcıdan puan sisteminde işlemek için inputlar alalım ve inputları standardize edelim.
    print("Hangi rock müzik grubusun?")
    print("")
    input1 = input("En sevdiğin renk (Siyah, Beyaz, Mavi, Kırmızı, Sarı, Yeşil, Diğer): ")
    input1 = input1.strip().lower()
    input2 = input("En sevdiğin hayvan (Kedi, Köpek, Ayı, Tavuk, Kurt, Aslan): ")
    input2 = input2.strip().lower()
    input3 = input("En sevdiğin tatlı tipi (Şerbetli, Sütlü): ")
    input3 = input3.strip().lower()
    input4 = input("En sevdiğin mevsim (Yaz, Kış, Bahar, Sonbahar): ")
    input4 = input4.strip().lower()
    # Aldığımız inputları puan sistemimizde işleyerek gruplara puanlar verelim.
    if input1 == "siyah":
        blacksabbath += 2
        acdc += 1
    elif input1 == "beyaz":
        whitestripes += 2
        mamasandpapas += 1
    elif input1 == "mavi":
        nirvana += 2
        kiss += 1
    elif input1 == "kırmızı":
        kiss += 2
        whitestripes += 1
    elif input1 == "sarı":
        mamasandpapas += 2
        abba += 1
    elif input1 == "yeşil":
        survivor += 2
        bonjovi += 1
    elif input1 == "diğer":
        acdc += 2
        poormanspotion += 1
    else:
        print("Geçersiz renk girdiniz. Lütfen tekrar deneyin.")
        continue

    if input2 == "kedi":
        abba += 2
        bonjovi += 1
    elif input2 == "köpek":
        acdc += 2
        kiss += 1
    elif input2 == "ayı":
        poormanspotion += 2
        survivor += 1
    elif input2 == "tavuk":
        whitestripes += 2
        mamasandpapas += 1
    elif input2 == "kurt":
        nirvana += 2
        blacksabbath += 1
    elif input2 == "aslan":
        survivor += 2
        bonjovi += 1
    else:
        print("Geçersiz hayvan girdiniz. Lütfen tekrar deneyin.")
        continue

    if input3 == "sütlü":
        abba += 1
        mamasandpapas += 1
        bonjovi += 1
        whitestripes += 1
        poormanspotion += 1
    elif input3 == "şerbetli":
        blacksabbath += 1
        acdc += 1
        kiss += 1
        nirvana += 1
        survivor += 1
    else:
        print("Geçersiz tatlı türü girdiniz. Lütfen tekrar deneyin.")
        continue
    if input4 == "yaz":
        bonjovi += 2
        whitestripes += 1
    elif input4 == "kış":
        acdc += 2
        nirvana += 1
    elif input4 == "bahar":
        mamasandpapas += 2
        abba += 1
    elif input4 == "sonbahar":
        blacksabbath += 2
        survivor += 1
    else:
        print("Geçersiz mevsim girdiniz. Lütfen tekrar deneyin.")
        continue
        
    # Grupları bir sözlükte tanımlayalım.
    gruplar = {
        "Black Sabbath": blacksabbath,
        "Bon Jovi": bonjovi,
        "Kiss": kiss,
        "ABBA": abba,
        "AC/DC": acdc,
        "Survivor": survivor,
        "Poor Man's Potion": poormanspotion,
        "Nirvana": nirvana,
        "The Mamas and the Papas": mamasandpapas,
        "The White Stripes": whitestripes}
    # Sözlükteki maksimum puan değerini max() fonksiyonu ile alalım ve max_value değişkenine atayalım.
    max_value = max(gruplar.values())
    winners = []
    # Atadığımız max_value ile eşit olan grubu bulalım ve kazananlar listesine ekleyelim.
    if blacksabbath == max_value:
        winners.append("Black Sabbath")
    if bonjovi == max_value:
        winners.append("Bon Jovi")
    if kiss == max_value:
        winners.append("Kiss")
    if abba == max_value:
        winners.append("ABBA")
    if acdc == max_value:
        winners.append("AC/DC")
    if survivor == max_value:
        winners.append("Survivor")
    if poormanspotion == max_value:
        winners.append("Poor Man's Potion")
    if nirvana == max_value:
        winners.append("Nirvana")
    if mamasandpapas == max_value:
        winners.append("The Mamas and the Papas")
    if whitestripes == max_value:
        winners.append("The White Stripes")
    # Kazananlar listesinden
    print("")
    print("Sen",winners[0],"grubusun!")
    yes = input("Dinlmek ister misin? ")
    if yes == "evet" or yes == "yes" or yes =="Evet" or yes == "EVET" or yes == "YES":
        yt()
        print("-------------------------------")
        continue
    else:
        print("-------------------------------")
        continue   


    


        





