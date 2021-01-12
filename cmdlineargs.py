import ast

def process_keyval_args(glvars, argv):
    """
    python XXX.py key1=val1 key2=val2

    puts python variable called "key1" with appropriate value "val1" in the global scope, as if it were defined in the python program file itself.

    The python file must have place holder values for key1, key2 etc defined, 
    and there should be a call to 
    process_key_val_args() 
    after these values are defined.  Python will assume command line arg
    should be interpreted as same type as the place holder variables of same name.
    """
    if len(argv) > 0:
        for ii in range(len(argv)):
            print(argv[ii])
            kyval=argv[ii].split("=")

            if len(kyval) != 2:
                print("error")
            ky  = kyval[0]
            val = kyval[1]

            if type(glvars[ky]) == int:
                glvars[ky] = int(val)
            elif type(glvars[ky]) == float:
                glvars[ky] = float(val)
            elif type(glvars[ky]) == str:
                glvars[ky] = val
            elif type(glvars[ky]) == bool:
                glvars[ky] = True if (val == "True") else False
            elif type(glvars[ky]) == list:
                glvars[ky] = ast.literal_eval(val)

