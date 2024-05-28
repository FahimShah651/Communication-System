syms w u(t) x(t) r(t) h(t) y(t)
u(t) = heaviside(t);
x(t) =((-0.5*t+2).*(u(t)-u(t-4)))+((0.5*t+2).*(u(-t)-u(-t-4)));
h(t) = ((-0.5*t+1).*(u(t)-u(t-2)))+((0.5*t+1).*(u(-t)-u(-t-2)));




y(t) = int(x(w)*h(t-w), w, -inf, inf);

fplot(x(t), [-1 5])

title('x(t) = u(t-2)')

fplot(h(t), [-1 5])

title('(-t+2).*(u(t)-u(t-2))')

fplot(y(t), [-1 5])


title('y(t) = x(t)*h(t)')



