
def check(mod, eq):
    w = mod.WordDictionary()
    w.addWord("day"); w.addWord("bay"); w.addWord("may")
    eq(w.search("say"), False)
    eq(w.search("day"), True)
    eq(w.search(".ay"), True)
    eq(w.search("b.."), True)
    eq(w.search("..."), True)
    eq(w.search(".."), False)
    eq(w.search("...."), False)
