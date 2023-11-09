
const minDigit = x => {
    let result = 9
    while(x) {
        const tmp = Math.floor(x % 10) // or (x / 10).toFixed()
        result = result < tmp ? result : tmp
        x = Math.floor(x / 10) // or (x / 10).toFixed()
    }
    return result
}