n = int(input())
balance = 0
s = ""
def function(s,balance):
    if len(s) == n:
        if balance == 0:
            print(s)
        return

    function(s + "(",balance+1)
    if balance > 0:
        function(s + ")",balance-1)

function(s,balance)




    

     

