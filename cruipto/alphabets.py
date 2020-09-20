"""Alphabets carefully chosen to provide clickable, recognizable and short codes.
Dictionaries for fast lookup are also provided"""

from typing import Dict, Optional


def __getattr__(name: str) -> Optional[Dict[str, int]]:
    if name == "lookup800":
        return {char: idx for idx, char in enumerate(letters800)}
    raise AttributeError


# UTF-8, but only uses 1-2 bytes. փ
# TheIdMatrixxxx
letters800 = "0ο23456789ABCDEFGHͷJKLəNOPQRSŃUVWXYZȮbcƵËfgբŇjklmοopqƔs_uvwքyzµÀÁÂÃÄÅΊÇÈÉÊeÌÍÎÏÐÑÒÓÔtÖØÙÚÛÜÝÞßàáâãäχæçèéêëìíîïðñòóôõöøùúûüýþÿĀāĂăĄąĆćĈĉĊΊČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİμĵĶķĸĹĺĻļĽľΊςTńŅņiňŉŊŋŌōŎŏŐőŔŕŖρŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵλŷŸŹźŻżŽžſƀƁƂƃƄƅƆƇƈƉƊƋƌƍƎρƐωƒƓrƕƖƗƘƙƚƛƜƝƞƟƠơƢƣƤƥƦƧƨƩƪƫƬλƮƯưƱμƳƴdƶƷƸƹƺƻƼƽƾƿǍǎǏǐǑǒǓǔǕǖǗǘǙǚǛǜǝǞǟǠǡǢǣǦǧǨǩǪǫǬǭǮǯǰǴǵǶǸǹǼǽǾǿȀȁȂȃȄȅȆιȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘșȚțμȟȠȡ_ȥȦȧȨȩȪȫȬȭaȯȰȱȲȳȷȺȻȼɃɄɅɌɍɐɑɒɓɔɕɖɗɘMɛɜɟɠɡɢɥɦɧɩɪɫɬɯɰɱɲɳɴɵɶɷɸɹɺɻύɽɾɿʀʁʂʃʄʅʆʇρʉʊʋʌʍʎʏʐʑʒʓʘʙʛʜʝʞʟʠͶIͻͿΆpΉΊΌΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜλΞΟΠΡΣΤιΦΧΨΩΪΫάύήίΰαβoδεζηθικλμνξοπρςστυφχψoϊϋόύιϐϑϒϓϔϕϖϗϘpϚϛϜϝϰϱϲϳϴϵϷϸϹϺϻϼϽЀЁЂЃЄЅІЇЈЉЊЋЌЍЎЏАБВГДЕ_ЗИЙКЛМНОПРСТУФχЦЧpЩЪЫЬЭЮЯабвгдежзχйклмнопрстуфхцчшщъыьэюяςёђѓєѕіїјљњћќѝўџѢѣѲѳҐґҒғҔҕoҗҘҙҚқҢңπҥҪҫҬҭύүҰұҲҳҺһӀӁӂӃӄӇӈӋӌӐӑӒӓӔӕӖӗӘәӚӛӜӝӞӟӠӡӢӣӤӥӦӧӨπӪӫӬωӮӯӰӱӲӳoӵӶӷӸӹԐԑԚԛԜԝՓՕπաhգդςզοըթժիխծկհձղճմնշոչպջռսվտրցւփx"  # noqa
# ent = "ÆŗȇłȤө1ΝҮåϙƑȞӴ"
# sai = "Ίρις_πολύχpωμo"
# m = dict(zip(ent, sai))
# o = dict(zip(sai, ent))
# print(m)
# print(o)
# oldletters800 = letters800
# r = ""
# for l in letters800:
#     if l in m:
#         print("m", l, m[l])
#         x = m[l]
#     else:
#         x = l
#     r += x
# rold = r
# letters800 = rold
# print(oldletters800)
# print(letters800)

# This commented section bellow includes PIL package and alternative alphabets.
# Not really needed by now..............................................................................................
# def pixel_width(unicode_text):
#     from PIL import Image, ImageDraw, ImageFont
#     width = len(unicode_text) * 45
#     height = 100
#     back_ground_color = (0, 0, 0)
#     font_size = 64
#     font_color = (255, 255, 255)
#
#     im = Image.new("RGB", (width, height), back_ground_color)
#     draw = ImageDraw.Draw(im)
#     unicode_font = ImageFont.truetype(
#         "./usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", font_size)
#     draw.text((0, 0), unicode_text, font=unicode_font, fill=font_color)
#     im.save("/dev/shm/text.png")
#     box = Image.open("/dev/shm/text.png").getbbox()
#     if box:
#         return box[2] - box[0]
#     return 0
#
# def find_alphabet():
#     from fontTools.ttLib import TTFont
#
#     # DejaVuSans Mono 3206 visible width-respecting characters on Konsole:
#     ttf = TTFont('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 0,
#                  verbose=0, allowVID=0, ignoreDecompileErrors=True,
#                  fontNumber=-1)
#     uni = list(chain.from_iterable([chr(y[0])
#                                     for y in x.cmap.items()]
#                                    for x in ttf["cmap"].tables))
#     valid = sorted(''.join(set(uni)))[:65534]
#     excl = [0, 8, 9, 13, 29, 173, 1557, 3761] + list(range(128, 160)) + \
#            list(range(768, 866)) + list(range(1611, 1627)) + \
#            list(range(3764, 3790))
#     usable = [l for l in valid if
#               pixel_width(l * 3) > 5 and ord(l) not in excl]
#
#     # Picking only the 1966 word chars...
#     regx = re.compile(r'\w')
#     wordchars = regx.findall(''.join(usable))
#     alphabet = ''.join(wordchars)
#     print(alphabet)
#     print(len(alphabet))
#     # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyzª²³µ¹º¼½¾ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſƀƁƂƃƄƅƆƇƈƉƊƋƌƍƎƏƐƑƒƓƔƕƖƗƘƙƚƛƜƝƞƟƠơƢƣƤƥƦƧƨƩƪƫƬƭƮƯưƱƲƳƴƵƶƷƸƹƺƻƼƽƾƿǀǁǂǃǍǎǏǐǑǒǓǔǕǖǗǘǙǚǛǜǝǞǟǠǡǢǣǦǧǨǩǪǫǬǭǮǯǰǴǵǶǸǹǼǽǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘșȚțȜȝȞȟȠȡȤȥȦȧȨȩȪȫȬȭȮȯȰȱȲȳȴȵȶȷȸȹȺȻȼȽȾȿɀɁɃɄɅɌɍɐɑɒɓɔɕɖɗɘəɚɛɜɝɞɟɠɡɢɣɤɥɦɧɨɩɪɫɬɭɮɯɰɱɲɳɴɵɶɷɸɹɺɻɼɽɾɿʀʁʂʃʄʅʆʇʈʉʊʋʌʍʎʏʐʑʒʓʔʕʖʗʘʙʚʛʜʝʞʟʠʡʢʣʤʥʦʧʨʩʪʫʬʭʮʯʰʱʲʳʴʵʶʷʸʹʻʼʽʾʿˀˁˆˇˈˉˌˍˎˏːˑˠˡˢˣˤˮʹͶͷͺͻͼͽͿΆΈΉΊΌΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫάέήίΰαβγδεζηθικλμνξοπρςστυφχψωϊϋόύώϐϑϒϓϔϕϖϗϘϙϚϛϜϝϞϟϠϡϰϱϲϳϴϵϷϸϹϺϻϼϽϾϿЀЁЂЃЄЅІЇЈЉЊЋЌЍЎЏАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяѐёђѓєѕіїјљњћќѝўџѢѣѲѳҐґҒғҔҕҖҗҘҙҚқҢңҤҥҪҫҬҭҮүҰұҲҳҺһӀӁӂӃӄӇӈӋӌӏӐӑӒӓӔӕӖӗӘәӚӛӜӝӞӟӠӡӢӣӤӥӦӧӨөӪӫӬӭӮӯӰӱӲӳӴӵӶӷӸӹԐԑԚԛԜԝԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՒՓՔՕՖՙաբգդեզէըթժիլխծկհձղճմյնշոչպջռսվտրցւփքօֆևءآأؤإئابةتثجحخدذرزسشصضطظعغـفقكلمنهوىي٠١٢٣٤٥٦٧٨٩ٴٹٺٻپٿڀڃڄچڇڑژڤکگھی۰۱۲۳۴۵۶۷۸۹ກຂຄງຈຊຍດຕຖທນບປຜຝພຟມຢຣລວສຫອຮຯະາຳაბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰჱჲჳჴჵჶჷჸჹჺჼᴂᴈᴉᴔᴖᴗᴝᴞᴟᴬᴭᴮᴰᴱᴲᴳᴴᴵᴶᴷᴸᴹᴺᴻᴼᴾᴿᵀᵁᵂᵃᵄᵅᵆᵇᵈᵉᵊᵋᵌᵍᵎᵏᵐᵑᵒᵓᵔᵕᵖᵗᵘᵙᵚᵛᵢᵣᵤᵥᵷᵸᵻᶅᶛᶜᶝᶞᶟᶠᶡᶢᶣᶤᶥᶦᶧᶨᶩᶪᶫᶬᶭᶮᶯᶰᶱᶲᶳᶴᶵᶶᶷᶹᶺᶻᶼᶽᶾᶿḀḁḂḃḄḅḆḇḈḉḊḋḌḍḎḏḐḑḒḓḘḙḚḛḜḝḞḟḠḡḢḣḤḥḦḧḨḩḪḫḬḭḰḱḲḳḴḵḶḷḸḹḺḻḼḽḾḿṀṁṂṃṄṅṆṇṈṉṊṋṌṍṔṕṖṗṘṙṚṛṜṝṞṟṠṡṢṣṨṩṪṫṬṭṮṯṰṱṲṳṴṵṶṷṸṹṼṽṾṿẀẁẂẃẄẅẆẇẈẉẊẋẌẍẎẏẐẑẒẓẔẕẖẗẘẙẛẟẠạẬậẰằẶặẸẹẼẽỆệỊịỌọỘộỚớỜờỠỡỢợỤụỨứỪừỮữỰựỲỳỴỵỸỹἀἁἂἃἄἅἆἇἈἉἊἋἌἍἎἏἐἑἒἓἔἕἘἙἚἛἜἝἠἡἢἣἤἥἦἧἨἩἪἫἬἭἮἯἰἱἲἳἴἵἶἷἸἹἺἻἼἽἾἿὀὁὂὃὄὅὈὉὊὋὌὍὐὑὒὓὔὕὖὗὙὛὝὟὠὡὢὣὤὥὦὧὨὩὪὫὬὭὮὯὰάὲέὴήὶίὸόὺύὼώᾀᾁᾂᾃᾄᾅᾆᾇᾈᾉᾊᾋᾌᾍᾎᾏᾐᾑᾒᾓᾔᾕᾖᾗᾘᾙᾚᾛᾜᾝᾞᾟᾠᾡᾢᾣᾤᾥᾦᾧᾨᾩᾪᾫᾬᾭᾮᾯᾰᾱᾲᾳᾴᾶᾷᾸᾹᾺΆᾼιῂῃῄῆῇῈΈῊΉῌῐῑῒΐῖῗῘῙῚΊῠῡῢΰῤῥῦῧῨῩῪΎῬῲῳῴῶῷῸΌῺΏῼ⁰ⁱ⁴⁵⁶⁷⁸⁹ⁿ₀₁₂₃₄₅₆₇₈₉ₐₑₒₓₔₕₖₗₘₙₚₛₜℂℍℎℏℕℙℚℝℤΩKÅⅈ⅐⅑⅓⅔⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅟↉ⱤⱭⱮⱯⱰⱵⱶⱷⱹⱺⱼⱽⱾⱿꜛꜜꜝꜞꜟꜢꜣꜤꜥꜦꜧꞋꞌꞍꞎꞐꞑꞪꟸꟹﬁﬂﭒﭓﭔﭕﭖﭗﭘﭙﭚﭛﭜﭝﭞﭟﭠﭡﭢﭣﭤﭥﭦﭧﭨﭩﭪﭫﭬﭭﭮﭯﭰﭱﭲﭳﭴﭵﭶﭷﭸﭹﭺﭻﭼﭽﭾﭿﮀﮁﮊﮋﮌﮍﮎﮏﮐﮑﮒﮓﮔﮕﮞﮟﮪﮫﮬﮭﯨﯩﯼﯽﯾﯿﹰﹱﹲﹳﹴﹶﹷﹸﹹﹺﹻﹼﹽﹾﹿﺀﺁﺂﺃﺄﺅﺆﺇﺈﺉﺊﺋﺌﺍﺎﺏﺐﺑﺒﺓﺔﺕﺖﺗﺘﺙﺚﺛﺜﺝﺞﺟﺠﺡﺢﺣﺤﺥﺦﺧﺨﺩﺪﺫﺬﺭﺮﺯﺰﺱﺲﺳﺴﺵﺶﺷﺸﺹﺺﺻﺼﺽﺾﺿﻀﻁﻂﻃﻄﻅﻆﻇﻈﻉﻊﻋﻌﻍﻎﻏﻐﻑﻒﻓﻔﻕﻖﻗﻘﻙﻚﻛﻜﻝﻞﻟﻠﻡﻢﻣﻤﻥﻦﻧﻨﻩﻪﻫﻬﻭﻮﻯﻰﻱﻲﻳﻴﻵﻶﻷﻸﻹﻺﻻﻼ𝕚𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿

# Manually removing ctr+w unfriendly ones, 1927 remains.
# alphabet1927 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyzªµºÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſƀƁƂƃƄƅƆƇƈƉƊƋƌƍƎƏƐƑƒƓƔƕƖƗƘƙƚƛƜƝƞƟƠơƢƣƤƥƦƧƨƩƪƫƬƭƮƯưƱƲƳƴƵƶƷƸƹƺƻƼƽƾƿǀǁǂǃǍǎǏǐǑǒǓǔǕǖǗǘǙǚǛǜǝǞǟǠǡǢǣǦǧǨǩǪǫǬǭǮǯǰǴǵǶǸǹǼǽǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘșȚțȜȝȞȟȠȡȤȥȦȧȨȩȪȫȬȭȮȯȰȱȲȳȴȵȶȷȸȹȺȻȼȽȾȿɀɁɃɄɅɌɍɐɑɒɓɔɕɖɗɘəɚɛɜɝɞɟɠɡɢɣɤɥɦɧɨɩɪɫɬɭɮɯɰɱɲɳɴɵɶɷɸɹɺɻɼɽɾɿʀʁʂʃʄʅʆʇʈʉʊʋʌʍʎʏʐʑʒʓʔʕʖʗʘʙʚʛʜʝʞʟʠʡʢʣʤʥʦʧʨʩʪʫʬʭʮʯʰʱʲʳʴʵʶʷʸʹʻʼʽʾʿˀˁˆˇˈˉˌˍˎˏːˑˠˡˢˣˤˮʹͶͷͺͻͼͽͿΆΈΉΊΌΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫάέήίΰαβγδεζηθικλμνξοπρςστυφχψωϊϋόύώϐϑϒϓϔϕϖϗϘϙϚϛϜϝϞϟϠϡϰϱϲϳϴϵϷϸϹϺϻϼϽϾϿЀЁЂЃЄЅІЇЈЉЊЋЌЍЎЏАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяѐёђѓєѕіїјљњћќѝўџѢѣѲѳҐґҒғҔҕҖҗҘҙҚқҢңҤҥҪҫҬҭҮүҰұҲҳҺһӀӁӂӃӄӇӈӋӌӏӐӑӒӓӔӕӖӗӘәӚӛӜӝӞӟӠӡӢӣӤӥӦӧӨөӪӫӬӭӮӯӰӱӲӳӴӵӶӷӸӹԐԑԚԛԜԝԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՒՓՔՕՖՙաբգդեզէըթժիլխծկհձղճմյնշոչպջռսվտրցւփքօֆևءآأؤإئابةتثجحخدذرزسشصضطظعغـفقكلمنهوىي٠١٢٣٤٥٦٧٨٩ٴٹٺٻپٿڀڃڄچڇڑژڤکگھی۰۱۲۳۴۵۶۷۸۹ກຂຄງຈຊຍດຕຖທນບປຜຝພຟມຢຣລວສຫອຮຯະາຳაბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰჱჲჳჴჵჶჷჸჹჺჼᴂᴈᴉᴔᴖᴗᴝᴞᴟᴬᴭᴮᴰᴱᴲᴳᴴᴵᴶᴷᴸᴹᴺᴻᴼᴾᴿᵀᵁᵂᵃᵄᵅᵆᵇᵈᵉᵊᵋᵌᵍᵎᵏᵐᵑᵒᵓᵔᵕᵖᵗᵘᵙᵚᵛᵢᵣᵤᵥᵷᵸᵻᶅᶛᶜᶝᶞᶟᶠᶡᶢᶣᶤᶥᶦᶧᶨᶩᶪᶫᶬᶭᶮᶯᶰᶱᶲᶳᶴᶵᶶᶷᶹᶺᶻᶼᶽᶾᶿḀḁḂḃḄḅḆḇḈḉḊḋḌḍḎḏḐḑḒḓḘḙḚḛḜḝḞḟḠḡḢḣḤḥḦḧḨḩḪḫḬḭḰḱḲḳḴḵḶḷḸḹḺḻḼḽḾḿṀṁṂṃṄṅṆṇṈṉṊṋṌṍṔṕṖṗṘṙṚṛṜṝṞṟṠṡṢṣṨṩṪṫṬṭṮṯṰṱṲṳṴṵṶṷṸṹṼṽṾṿẀẁẂẃẄẅẆẇẈẉẊẋẌẍẎẏẐẑẒẓẔẕẖẗẘẙẛẟẠạẬậẰằẶặẸẹẼẽỆệỊịỌọỘộỚớỜờỠỡỢợỤụỨứỪừỮữỰựỲỳỴỵỸỹἀἁἂἃἄἅἆἇἈἉἊἋἌἍἎἏἐἑἒἓἔἕἘἙἚἛἜἝἠἡἢἣἤἥἦἧἨἩἪἫἬἭἮἯἰἱἲἳἴἵἶἷἸἹἺἻἼἽἾἿὀὁὂὃὄὅὈὉὊὋὌὍὐὑὒὓὔὕὖὗὙὛὝὟὠὡὢὣὤὥὦὧὨὩὪὫὬὭὮὯὰάὲέὴήὶίὸόὺύὼώᾀᾁᾂᾃᾄᾅᾆᾇᾈᾉᾊᾋᾌᾍᾎᾏᾐᾑᾒᾓᾔᾕᾖᾗᾘᾙᾚᾛᾜᾝᾞᾟᾠᾡᾢᾣᾤᾥᾦᾧᾨᾩᾪᾫᾬᾭᾮᾯᾰᾱᾲᾳᾴᾶᾷᾸᾹᾺΆᾼιῂῃῄῆῇῈΈῊΉῌῐῑῒΐῖῗῘῙῚΊῠῡῢΰῤῥῦῧῨῩῪΎῬῲῳῴῶῷῸΌῺΏῼⁱⁿₐₑₒₓₔₕₖₗₘₙₚₛₜℂℍℎℏℕℙℚℝℤΩKÅⅈⱤⱭⱮⱯⱰⱵⱶⱷⱹⱺⱼⱽⱾⱿꜛꜜꜝꜞꜟꜢꜣꜤꜥꜦꜧꞋꞌꞍꞎꞐꞑꞪꟸꟹﬁﬂﭒﭓﭔﭕﭖﭗﭘﭙﭚﭛﭜﭝﭞﭟﭠﭡﭢﭣﭤﭥﭦﭧﭨﭩﭪﭫﭬﭭﭮﭯﭰﭱﭲﭳﭴﭵﭶﭷﭸﭹﭺﭻﭼﭽﭾﭿﮀﮁﮊﮋﮌﮍﮎﮏﮐﮑﮒﮓﮔﮕﮞﮟﮪﮫﮬﮭﯨﯩﯼﯽﯾﯿﹰﹱﹲﹳﹴﹶﹷﹸﹹﹺﹻﹼﹽﹾﹿﺀﺁﺂﺃﺄﺅﺆﺇﺈﺉﺊﺋﺌﺍﺎﺏﺐﺑﺒﺓﺔﺕﺖﺗﺘﺙﺚﺛﺜﺝﺞﺟﺠﺡﺢﺣﺤﺥﺦﺧﺨﺩﺪﺫﺬﺭﺮﺯﺰﺱﺲﺳﺴﺵﺶﺷﺸﺹﺺﺻﺼﺽﺾﺿﻀﻁﻂﻃﻄﻅﻆﻇﻈﻉﻊﻋﻌﻍﻎﻏﻐﻑﻒﻓﻔﻕﻖﻗﻘﻙﻚﻛﻜﻝﻞﻟﻠﻡﻢﻣﻤﻥﻦﻧﻨﻩﻪﻫﻬﻭﻮﻯﻰﻱﻲﻳﻴﻵﻶﻷﻸﻹﻺﻻﻼ𝕚𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿'
# alphabet1927dic = {char: idx for idx, char in enumerate(alphabet1927)}

# Manually removing small or separator-like ones, 1430 remains.
# alphabet1430 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzµÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſƀƁƂƃƄƅƆƇƈƉƊƋƌƍƎƏƐƑƒƓƔƕƖƗƘƙƚƛƜƝƞƟƠơƢƣƤƥƦƧƨƩƪƫƬƭƮƯưƱƲƳƴƵƶƷƸƹƺƻƼƽƾƿǁǂǍǎǏǐǑǒǓǔǕǖǗǘǙǚǛǜǝǞǟǠǡǢǣǦǧǨǩǪǫǬǭǮǯǰǴǵǶǸǹǼǽǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘșȚțȜȝȞȟȠȡȤȥȦȧȨȩȪȫȬȭȮȯȰȱȲȳȴȵȶȷȸȹȺȻȼȽȾȿɀɁɃɄɅɌɍɐɑɒɓɔɕɖɗɘəɚɛɜɝɞɟɠɡɢɣɤɥɦɧɨɩɪɫɬɭɮɯɰɱɲɳɴɵɶɷɸɹɺɻɼɽɾɿʀʁʂʃʄʅʆʇʈʉʊʋʌʍʎʏʐʑʒʓʔʕʖʗʘʙʚʛʜʝʞʟʠʡʢʣʤʥʦʧʨʩʪʫʬʭʮʯͶͷͻͼͽͿΆΈΉΊΌΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫάέήίΰαβγδεζηθικλμνξοπρςστυφχψωϊϋόύώϐϑϒϓϔϕϖϗϘϙϚϛϜϝϞϟϠϡϰϱϲϳϴϵϷϸϹϺϻϼϽϾϿЀЁЂЃЄЅІЇЈЉЊЋЌЍЎЏАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяѐёђѓєѕіїјљњћќѝўџѢѣѲѳҐґҒғҔҕҖҗҘҙҚқҢңҤҥҪҫҬҭҮүҰұҲҳҺһӀӁӂӃӄӇӈӋӌӐӑӒӓӔӕӖӗӘәӚӛӜӝӞӟӠӡӢӣӤӥӦӧӨөӪӫӬӭӮӯӰӱӲӳӴӵӶӷӸӹԐԑԚԛԜԝԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՒՓՔՕՖաբգդեզէըթժիլխծկհձղճմյնշոչպջռսվտրցւփքօֆև٤٥٦۲۳۴۵۶۷۸۹ກຂຄງຈຊຍດຕຖທນບປຜຝພຟມຢຣລວສຫອຮຯະາຳაბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰჱჲჳჴჵჶჷჸჹჺᴂᴈᴉᴔᴖᴗᴝᴞᴟᵷᵻᶅḀḁḂḃḄḅḆḇḈḉḊḋḌḍḎḏḐḑḒḓḘḙḚḛḜḝḞḟḠḡḢḣḤḥḦḧḨḩḪḫḬḭḰḱḲḳḴḵḶḷḸḹḺḻḼḽḾḿṀṁṂṃṄṅṆṇṈṉṊṋṌṍṔṕṖṗṘṙṚṛṜṝṞṟṠṡṢṣṨṩṪṫṬṭṮṯṰṱṲṳṴṵṶṷṸṹṼṽṾṿẀẁẂẃẄẅẆẇẈẉẊẋẌẍẎẏẐẑẒẓẔẕẖẗẘẙẛẟẠạẬậẰằẶặẸẹẼẽỆệỊịỌọỘộỚớỜờỠỡỢợỤụỨứỪừỮữỰựỲỳỴỵỸỹἀἁἂἃἄἅἆἇἈἉἊἋἌἍἎἏἐἑἒἓἔἕἘἙἚἛἜἝἠἡἢἣἤἥἦἧἨἩἪἫἬἭἮἯἰἱἲἳἴἵἶἷἸἹἺἻἼἽἾἿὀὁὂὃὄὅὈὉὊὋὌὍὐὑὒὓὔὕὖὗὙὛὝὟὠὡὢὣὤὥὦὧὨὩὪὫὬὭὮὯὰάὲέὴήὶίὸόὺύὼώᾀᾁᾂᾃᾄᾅᾆᾇᾈᾉᾊᾋᾌᾍᾎᾏᾐᾑᾒᾓᾔᾕᾖᾗᾘᾙᾚᾛᾜᾝᾞᾟᾠᾡᾢᾣᾤᾥᾦᾧᾨᾩᾪᾫᾬᾭᾮᾯᾰᾱᾲᾳᾴᾶᾷᾸᾹᾺΆᾼῂῃῄῆῇῈΈῊΉῌῐῑῒΐῖῗῘῙῚΊῠῡῢΰῤῥῦῧῨῩῪΎῬῲῳῴῶῷῸΌῺΏῼℂℍℎℏℕℙℚℝℤΩKÅⅈⱤⱭⱮⱯⱰⱵⱶⱷⱹⱺⱾⱿꜢꜤꜥꜦꜧꞍꞎꞐꞑꞪﬁﬂ'
# alphabet1430dic = {char: idx for idx, char in enumerate(alphabet1927)}

# Manually removing strange characters for western readers, until 1224.
# alphabet1224 = '
# 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzµÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİĴĵĶķĸĹĺĻļĽľŁłŃńŅņŇňŉŊŋŌōŎŏŐőŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſƀƁƂƃƄƅƆƇƈƉƊƋƌƍƎƏƐƑƒƓƔƕƖƗƘƙƚƛƜƝƞƟƠơƢƣƤƥƦƧƨƩƪƫƬƭƮƯưƱƲƳƴƵƶƷƸƹƺƻƼƽƾƿǍǎǏǐǑǒǓǔǕǖǗǘǙǚǛǜǝǞǟǠǡǢǣǦǧǨǩǪǫǬǭǮǯǰǴǵǶǸǹǼǽǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘșȚțȞȟȠȡȤȥȦȧȨȩȪȫȬȭȮȯȰȱȲȳȷȺȻȼɃɄɅɌɍɐɑɒɓɔɕɖɗɘəɛɜɟɠɡɢɥɦɧɩɪɫɬɯɰɱɲɳɴɵɶɷɸɹɺɻɼɽɾɿʀʁʂʃʄʅʆʇʈʉʊʋʌʍʎʏʐʑʒʓʘʙʛʜʝʞʟʠͶͷͻͿΆΈΉΊΌΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫάέήίΰαβγδεζηθικλμνξοπρςστυφχψωϊϋόύώϐϑϒϓϔϕϖϗϘϙϚϛϜϝϰϱϲϳϴϵϷϸϹϺϻϼϽЀЁЂЃЄЅІЇЈЉЊЋЌЍЎЏАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяѐёђѓєѕіїјљњћќѝўџѢѣѲѳҐґҒғҔҕҖҗҘҙҚқҢңҤҥҪҫҬҭҮүҰұҲҳҺһӀӁӂӃӄӇӈӋӌӐӑӒӓӔӕӖӗӘәӚӛӜӝӞӟӠӡӢӣӤӥӦӧӨөӪӫӬӭӮӯӰӱӲӳӴӵӶӷӸӹԐԑԚԛԜԝՓՕՖաբգդեզէըթժիխծկհձղճմնշոչպջռսվտրցւփքօֆևᶅḀḁḂḃḄḅḆḇḈḉḊḋḌḍḎḏḐḑḒḓḘḙḚḛḜḝḞḟḠḡḢḣḤḥḦḧḨḩḪḫḬḭḰḱḲḳḴḵḶḷḸḹḺḻḼḽḾḿṀṁṂṃṄṅṆṇṈṉṊṋṌṍṔṕṖṗṘṙṚṛṜṝṞṟṠṡṢṣṨṩṪṫṬṭṮṯṰṱṲṳṴṵṶṷṸṹṼṽṾṿẀẁẂẃẄẅẆẇẈẉẊẋẌẍẎẏẐẑẒẓẔẕẖẗẘẙẟẠạẬậẰằẶặẸẹẼẽỆệỊịỌọỘộỚớỜờỠỡỢợỤụỨứỪừỮữỰựỲỳỴỵỸỹἀἁἂἃἄἅἆἇἈἉἊἋἌἍἎἏἐἑἒἓἔἕἘἙἚἛἜἝἠἡἢἣἤἥἦἧἨἩἪἫἬἭἮἯἰἱἲἳἴἵἶἷἸἹἺἻἼἽἾἿὀὁὂὃὄὅὈὉὊὋὌὍὐὑὒὓὔὕὖὗὙὛὝὟὠὡὢὣὤὥὦὧὨὩὪὫὬὭὮὯὰάὲέὴήὶίὸόὺύὼώᾀᾁᾂᾃᾄᾅᾆᾇᾈᾉᾊᾋᾌᾍᾎᾏᾐᾑᾒᾓᾔᾕᾖᾗᾘᾙᾚᾛᾜᾝᾞᾟᾠᾡᾢᾣᾤᾥᾦᾧᾨᾩᾪᾫᾬᾭᾮᾯᾰᾱᾲᾳᾴᾶᾷᾸᾹᾺΆᾼῂῃῄῆῇῈΈῊΉῌῐῑῒΐῖῗῘῙῚΊῠῡῢΰῤῥῦῧῨῩῪΎῬῲῳῴῶῷῸΌῺΏῼℎℏΩKÅⱤⱭⱮⱯⱰⱷⱹⱺꜦꜧꞍꞎꞐꞑꞪﬁﬂ'
# alphabet1224dic = {char: idx for idx, char in enumerate(alphabet1224)}
# ................................................................................................
