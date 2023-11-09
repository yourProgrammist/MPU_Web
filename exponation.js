const pow = (x, n) => {
    if (n === 0)
        return 1;
    if (n % 2 === 0) {
        const res = pow(x, n / 2);
        return res * res;
    } 
    return x * pow(x, n - 1);
}