def is_variable(Input_Var):
        return Input_Var.islower()
'''
 * Artificial Intelligence A Modern Approach (3rd Edition): Figure 9.1, page 328.
 *
 * <pre>
 * function UNIFY(x, y, theta) returns a substitution to make x and y identical
 *   inputs: x, a variable, constant, list, or compound
 *           y, a variable, constant, list, or compound
 *           theta, the substitution built up so far (optional, defaults to empty)
 *
 *   if theta = failure then return failure
 *   else if x = y the return theta
 *   else if VARIABLE?(x) then return UNIVY-VAR(x, y, theta)
 *   else if VARIABLE?(y) then return UNIFY-VAR(y, x, theta)
 *   else if COMPOUND?(x) and COMPOUND?(y) then
 *       return UNIFY(x.ARGS, y.ARGS, UNIFY(x.OP, y.OP, theta))
 *   else if LIST?(x) and LIST?(y) then
 *       return UNIFY(x.REST, y.REST, UNIFY(x.FIRST, y.FIRST, theta))
 *   else return failure
 *
 * ---------------------------------------------------------------------------------------------------
 *
 * function UNIFY-VAR(var, x, theta) returns a substitution
 *
 *   if {var/val} E theta then return UNIFY(val, x, theta)
 *   else if {x/val} E theta then return UNIFY(var, val, theta)
 *   else if OCCUR-CHECK?(var, x) then return failure
 *   else return add {var/x} to theta
 * </pre>
 *

'''


def is_variable(Input_Var):
    if(isinstance(Input_Var,list)):
        return False
    else:
        return  Input_Var.islower()
def unify(x,y,theta):
    if(x==y):
        return theta
    elif(is_variable(x)):
        return unify_var(x,y,theta)
    elif(is_variable(y)):
        return unify_var(y,x,theta)
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        return unify(x[1:],y[1:],unify(x[0],y[0],theta))
    else:
        return None

def unify_var(var,x,theta):
    if var in theta.keys():
        return unify(theta[var],x,theta)
    elif x in theta.keys():
        return unify(theta[var],x,theta)
    #elif occur_check(var,x):
    #    return none
    else:
        theta[var]=x
    return theta
print(unify(['John','p'],['p','x'],{}))
