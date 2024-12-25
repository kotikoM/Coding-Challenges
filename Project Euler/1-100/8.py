digit = ("731671765313306249192251196744265747423553491949"
         "349698352031277450632623957831801698480186947885"
         "184385861560789112949495459501737958331952853208"
         "805511125406987471585238630507156932909632952274"
         "430435576689664895044524452316173185640309871112"
         "172238311362229893423380308135336276614282806444"
         "486645238749303589072962904915604407723907138105"
         "158593079608667017242712188399879790879227492190"
         "169972088809377665727333001053367881220235421809"
         "751254540594752243525849077116705560136048395864"
         "467063244157221553975369781797784617406495514929"
         "086256932197846862248283972241375657056057490261"
         "407972968652414535100474821663704844031998900088"
         "952434506585412275886668811642717147992444292823"
         "086346567481391912316282458617866458359124566529"
         "476545682848912883142607690042242190226710556263"
         "211111093705442175069416589604080719840385096245"
         "544436298123098787992724428490918884580156166097"
         "919133875499200524063689912560717606058861164671"
         "094050775410022569831552000559357297257163626956"
         "1882670428252483600823257530420752963450")

sub = 13
max = 0
digits = ""
for i in range(len(digit) - sub + 1):
    num = digit[i:i + sub]

    p = 1
    for char in num:
        p *= int(char)

    if p > max:
        max = p
        digits = num

print("Number:", max)
print("Digits:",list(digits))
print(digits)