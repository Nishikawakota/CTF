# x ≡ 32134(mod 1584891)

surplus1 = 32134
mod1 = 1584891

# x ≡ 193127(mod 3438478)

surplus2 = 193127
mod2 = 3438478

i = 0
x = 0

while 1:
    i += 1
    x = mod1 * i + surplus1
    if x % mod2 == surplus2:
        break

print(x)