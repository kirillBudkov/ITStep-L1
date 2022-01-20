inp_v1=input('value1 ')
inp_v2=input('value2 ')
#main(
_res=None
if inp_v1.isdigit() and inp_v2.isdigit():
    operand=input('operand ')
    inp_v1=int(inp_v1)
    inp_v2=int(inp_v2)
    if operand=='*':
        _res=inp_v1*inp_v2
        print(_res)
    elif operand=='/':
        if inp_v2==0:
            print('error')
            exit()
            _res=inp_v1/inp_v2
            print(_res)
    elif operand=='+':
        _res=inp_v1+inp_v2
        print(_res)
    elif operand =='-':
        _res = inp_v1 -inp_v2
        print(_res)
else:
    print('error')
#)
#inp_v1='1'
#inp_v2='3'
#operand='*'
#main()
#mmmm