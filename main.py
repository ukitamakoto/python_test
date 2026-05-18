def in_autotests_we_trust(a, b):
    if a == b:
        print('PASS')
    else:
        print('FAILED')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)
