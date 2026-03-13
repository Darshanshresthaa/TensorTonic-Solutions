def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    x_new= x0

    for i in range(steps):
        dy_dx =2*a*x_new+b
        x_new=x_new -lr*dy_dx

    return x_new
        
   