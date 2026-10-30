
def check(mod, eq):
    s = mod.Solution()
    for words in (["neet","code"], ["a#b","","3#x"], [], [""], ["12#ab#","#"]):
        eq(s.decode(s.encode(words)), words)
