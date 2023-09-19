'lalala' + 'mamama' *2 #python'da stringlerde çarpılabilir toplanabilir

# 'bu' 'nlar' ifadeleri birbirleri ile aynı satırdalarsa otomatik olarak birleştirilir
'bu' 'nlar'

#bu özellik parantez içerisinde kullanıldığında çoklu satırları da birleştirir

text = ('ilk yazı bu olsun'
        'ikinci yazı bu olsun'
        'üçüncü yazı bu olsun')

text # çıktı tüm yazıları bir arada verir 
#örnek 2: 

merhaba = ('JDWQIJDWQJDOIWQJDOIWQJDIOWQJDOIQWJDOQWJODQJWD'
           'erfqojqweoıfjqweoıjewfqjoıfewqqwefqwfewqefewqfewqfewq'
           'loremmorem ahahhaahah'
           'qwefjqwefoıewqjfıqwejfoıewqfoıjwqefoı'
           'qwefopqwefjqwefoıewqf')
merhaba

#not: bu özellik yalnızca doğrudan stringlerde çalışır yani merhabanın sonuna bir şey eklemek istediğimizde hata verecektir.

merhaba 'lar'

#eğer merhaba değişkenin sonuna  sonuna lar eklemek istiyorsak + operatörünü kullanabiliriz

merhaba + 'lar'

#karakterler aynı zamanda bir dizidir ve dizi 0'dan başlar

merhaba = 'Benim adım Bera'

merhaba[0] #dizinin ilk elemanı olan B harfinin çıktısını verir

merhaba[3] # dizinin 4. elemanını verir +1 eklemeyi unutma kafanda

merhaba[-1] #dizinin son karakterini verir

merhaba[-2] #dizinin sondan ikinci karakterini verir

merhaba[-16] #bu kadar karakter olmadığı için hata verdi


#dizilerin belli kuralları var

merhaba[0:2] #ilk elemandan ikinci elemana kadar olan kısmı gösterir sonuç 'Be'

merhaba[2:5] #3.elemandan yani 2'den 5'e kadar olan kısmı gösterir (2'ye 1 eklemeyi unutma)

merhaba[:7] #başlangıçtan 7. elemana kadar olan kısmı gösterir

merhaba[4:] #4. elemandan dizinin tamamına kadar olan kısmını gösterir

merhaba[-2:] #sondan ikinci elemandan sona kadar olan kısmı gösterir

#aynı zamanda bu tarz diziler birbirleri ile toplanabilir örnek:

merhaba[:2] + merhaba[2:] #tam metni verir

merhaba[:4] + merhaba[4:] #tam metni verir

y = 'python'
y[6] # 0'dan başladığı için 6 karakter olsa bile 6. eleman boş

#len() fonksiyonu dizinin uzunluğunu verir

y = 'dört' # 4 karakter 4 eleman 0,1,2,3 indexleri
len(y)

#not: diziler aynı zamanda python'da liste olarak da adlandırılır.
