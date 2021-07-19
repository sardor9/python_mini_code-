def outer_function():
    var = 8

    def inner_function():
        global var # non_local
        print(var)
        var = 10

    print(var)
    inner_function()
    print(var)

var = 0
print(var)
outer_function()
print(var)
